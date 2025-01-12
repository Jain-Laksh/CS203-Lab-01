import json
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
import logging

# Flask App Initialization
app = Flask(__name__)
app.secret_key = 'secret'   
COURSE_FILE = 'course_catalog.json'

# Creates spans for each request
FlaskInstrumentor().instrument_app(app)

# OpenTelemetry Setup- capturing traces
resource = Resource.create({"service.name": "course-catalog-service"})
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

# Jaeger Exporter
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",  # Ensure Jaeger is accessible at this address
    agent_port=6831,
)
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

#Python logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',)
logger = logging.getLogger(__name__)

# Utility Functions
def load_courses():
    """Load courses from the JSON file."""
    with tracer.start_as_current_span("load_courses") as span:
        span.set_attribute("file.path", COURSE_FILE)
        span.set_attribute("file.exists", os.path.exists(COURSE_FILE))
        logger.info("Loading courses from file")
        if not os.path.exists(COURSE_FILE):
            logger.warning("Course file not found, returning empty list")
            return []  # Return an empty list if the file doesn't exist
        with open(COURSE_FILE, 'r') as file:
            courses = json.load(file)
            logger.info(f"Courses loaded successfully! Total number of courses: {len(courses)}")
            span.set_attribute("courses.count", len(courses))
            return courses


def save_courses(data):
    """Save new course data to the JSON file."""
    with tracer.start_as_current_span("save_courses") as span:
        courses = load_courses()  # Load existing courses
        courses.append(data)  # Append the new course
        with open(COURSE_FILE, 'w') as file:
            json.dump(courses, file, indent=4)
            logger.info(f"Saved course: {data['name']} to file")


# Routes
@app.route('/')
def index():
    with tracer.start_as_current_span("index") as span:
        span.set_attribute("http.method", request.method)
        span.set_attribute("http.url", request.url) 
        span.set_attribute("http.route", request.url_rule)  
        span.set_attribute("http.host", request.host)
        span.set_attribute("user.ip", request.remote_addr)   
        logger.info("Home page accessed")

    return render_template('index.html')

@app.route('/catalog')
def course_catalog():
    with tracer.start_as_current_span("index") as span:
        span.set_attribute("http.method", request.method)
        span.set_attribute("http.url", request.url)
        span.set_attribute("http.route", request.url_rule)
        span.set_attribute("http.host", request.host)
        span.set_attribute("user.ip", request.remote_addr)
        logger.info("Course catalog accessed")
        courses = load_courses()
        return render_template('course_catalog.html', courses=courses)


@app.route('/course/<code>')
def course_details(code):
    courses = load_courses()
    course = next((course for course in courses if course['code'] == code), None)
    with tracer.start_as_current_span("course_details") as span:
        span.set_attribute("course.code", code)
        span.set_attribute("http.method", request.method)
        span.set_attribute("http.url", request.url)
        span.set_attribute("http.route", request.url_rule)
        span.set_attribute("http.host", request.host)
        span.set_attribute("user.ip", request.remote_addr)
        logger.info(f"Course details accessed for course: {code}")
        if not course:
            span.set_attribute("error", f"No course found with code '{code}'")
            logger.error(f"No course found with code '{code}'")
            flash(f"No course found with code '{code}'.", "error")
            return redirect(url_for('course_catalog'))
        span.set_attribute("course found", course['name'])
        logger.info(f"Course found: {course['name']}")
        return render_template('course_details.html', course=course)

@app.route('/add-course', methods=['GET', 'POST'])
def add_course():
    with tracer.start_as_current_span("add_course") as span:
        span.set_attribute("http.method", request.method)
        span.set_attribute("http.url", request.url)
        span.set_attribute("http.route", request.url_rule)
        span.set_attribute("http.host", request.host)
        span.set_attribute("user.ip", request.remote_addr)
        logger.info("Add course page accessed")
        if request.method == 'POST':
            course = {
            "code": request.form.get('code'),
            "name": request.form.get('name'),
            "instructor": request.form.get('instructor'),
            "semester": request.form.get('semester'),
            "schedule": request.form.get('schedule'),   
            "classroom": request.form.get('classroom'),
            "prerequisites": request.form.get('prerequisites'),
            "grading": request.form.get('grading'),
            "description": request.form.get('description')
            }
            
            for key, value in course.items():
                if not value:
                    span.set_attribute("error", f"Please provide a value for '{key}'")
                    logger.error(f"Please provide a value for '{key}'")
                    flash(f"Please provide a value for '{key}'.", "error")
                    return redirect(url_for('add_course'))
                
            span.set_attribute("Form submitted", course)
            logger.info(f"Form submitted: {course}")  
            save_courses(course)
            logger.info(f"Course '{course['name']}' added successfully.")
            flash(f"Course '{course['name']}' added successfully.", "success")
            return redirect(url_for('course_catalog'))
        return render_template('add_course.html')

if __name__ == '__main__':
    app.run(debug=True)
