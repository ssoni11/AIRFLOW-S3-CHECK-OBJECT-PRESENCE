#DAG-WITH-S3-CHECK_OBJECT_PRESENCE

# Apache Airflow - AWS S3(MinIO) Sensor Example

This project demonstrates using Apache Airflow to check the presence of a specific storage object on MinIO, a rootless Docker container serving as an AWS S3-compatible storage solution. The project includes the creation of an extended Airflow Docker image and orchestrating the Airflow deployment with Docker Compose.

## Use Case

The use case for this project is when a client uploads a file to an AWS S3 bucket daily and at any time. The Airflow DAG, implemented in minio_sensor_dag.py, checks for the presence of this file on MinIO at specified time intervals before proceeding to the next task. This ensures that other tasks, such as processing or transferring the file, are triggered only when the specified file is available.

## Project Structure

- **`Dockerfile`:** Defines the extended Airflow Docker image with additional dependencies.
- **`docker-compose.yml`:** Composes the Airflow deployment with MinIO container.
- **`dags/`:** Contains Airflow DAG script for MinIO sensor.
- **`data/`:** Sample data for uploading to MinIO.
- **`requirements.txt`:** Lists Python dependencies for the extended Airflow image.

## Docker Image Creation

To create the extended Airflow Docker image with necessary dependencies:

```bash
# Clone Apache Airflow repository
git clone https://github.com/apache/airflow.git

# Navigate to the Airflow repository
cd airflow

# Create a requirements file with necessary dependencies
echo "boto3==1.18.73" > requirements-extended.txt

# Build the extended Airflow Docker image
docker build -t extended-airflow -f Dockerfile .

# Navigate back to your project directory
cd ..
```

## MinIO Setup

- Create a bucket on MinIO with read/write access.
- Upload a sample file from the /data directory to the MinIO bucket.

## Airflow Initialization
Use Docker Compose to initialize Apache Airflow along with MinIO:
```bash
# Launch Apache Airflow and MinIO containers
docker-compose up -d
```

## DAG Execution
- The Airflow DAG script (dags/minio_sensor_dag.py) checks for the presence of a specific object on MinIO before proceeding to the next task.

## Check Python Dependencies
- To check if AWS S3 dependencies are installed in the Airflow container:
```bash
# Find the container ID of the running Airflow container
docker ps

# Access the Airflow container shell
docker exec -it [container_id] bash

# Run the following command inside the container
pip list | grep amazon*
```

- Ensure that the installed dependencies match your local installation version with the Airflow sensor API for AWS S3.

- Feel free to adjust the project structure and instructions based on your specific requirements and preferences.

