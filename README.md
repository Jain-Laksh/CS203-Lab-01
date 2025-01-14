# CS203_Lab_01

## Installation
### Prerequisites

- Docker installed: [Get Docker](https://www.docker.com/get-started)
- Docker Compose installed: Docker Compose is included with Docker Desktop for Windows/Mac. For Linux, follow the instructions [here](https://docs.docker.com/compose/install/).

  
## Running Jaeger Locally

1. **Clone the repository** (if you haven't already):

    ```bash
    git clone https://github.com/Jain-Laksh/CS203-Lab-01.git
    cd .\CS203-Lab-01\
    ```

2. **Build the Docker containers**:

    Run the following command to build the images for the services defined in your `docker-compose.yml`:

    ```bash
    docker-compose build
    ```

    This will download the necessary images and build any other services defined.

3. **Start the containers**:

    Run the following command to start the services:

    ```bash
    docker-compose up
    ```

    This will start the Jaeger container and the flask app container. `16686`.

4. **Access the Jaeger UI**:

    Open your browser and visit [http://localhost:16686](http://localhost:16686) to access the Jaeger UI. You can then see the traces that are being sent from your application.

    Run your application on port 5000 [http://localhost:5000](http://localhost:5000) and make some requests. These can be tracked using Jaeger.


Example: Submitting the add courses form without filling in the required details flashes an error on the UI
The traces for this are captured on jaeger
![image](https://github.com/user-attachments/assets/fb7d557d-7487-465d-aec0-436bb47aab12)

![image](https://github.com/user-attachments/assets/407e8a17-652c-4985-a00d-0dd8ef2fbc29)


Screenshots
![image](https://github.com/user-attachments/assets/f19fc5cb-762b-4b69-9772-cca0f1539c1d)
![image](https://github.com/user-attachments/assets/de79b290-eb40-45cf-a518-ec6d7f74fdc6)
As you can see above image shows traces for Get request on the "/" route 

If clicked on the `Explore Course Catalog` button you are redirected to the `/catalog` route
![image](https://github.com/user-attachments/assets/d17a56a0-b42c-4fce-b66b-eb4da4cc0e4f)

The `catalog` trace has 3 spans as shown below
![image](https://github.com/user-attachments/assets/ec8d6d38-5120-45db-901a-627e5f0ed39f)



If clicked on the `Add course` button you are redirected to the `/add_course` route
The `add_courses` trace has 2 spans as shown below
![image](https://github.com/user-attachments/assets/5f359d24-83a4-4666-97dc-819a14677ed7)


Metrics are added in the spans as attribute
![image](https://github.com/user-attachments/assets/8a4d03b4-6ac4-46bd-b795-077099e8a338)



More SS
![image](https://github.com/user-attachments/assets/751333fb-2179-4219-9401-db9ba63d57d8)

![image](https://github.com/user-attachments/assets/c1dc45d6-0ba3-4d43-ad19-d3e4fb4f881f)

![image](https://github.com/user-attachments/assets/d0b404f5-befe-4380-8d78-505aa8c1d80c)
![image](https://github.com/user-attachments/assets/ef00e51d-414f-4bd2-9bc0-45f8c199fca2)
![image](https://github.com/user-attachments/assets/bcdc2005-8cf6-4e20-810b-9d72b9b45fee)
![image](https://github.com/user-attachments/assets/0f5ab50f-bf62-40b6-9f4c-83f4fc1ba42d)


LOGS
![image](https://github.com/user-attachments/assets/7c212ea2-7525-443e-9e96-87376a79be7a)
![image](https://github.com/user-attachments/assets/d5c3e968-d826-4a0f-8bf8-d89c69ea31c0)


Spans in console
![image](https://github.com/user-attachments/assets/d21747ec-53d7-4d32-84c0-0ac1348d6de8)

