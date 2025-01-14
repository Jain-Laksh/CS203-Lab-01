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

