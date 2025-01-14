# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Set the environment variable to indicate Flask is running in production
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV JAEGER_AGENT_HOST=jaeger

# Expose the port Flask will run on
EXPOSE 5000

# Run the Python application
CMD ["flask", "run", "--host=0.0.0.0"]