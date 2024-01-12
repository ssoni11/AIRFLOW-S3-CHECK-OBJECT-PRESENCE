<!--
#DAG-WITH-S3-CHECK_OBJECT_PRESENCE
-->
# Apache Airflow - AWS S3(MinIO) Sensor Example

This project demonstrates using Apache Airflow to check the presence of a specific storage object on MinIO, a rootless Docker container serving as an AWS S3-compatible storage solution. The project includes the creation of an extended Airflow Docker image and orchestrating the Airflow deployment with Docker Compose.

## Use Case

The use case for this project is when a client uploads a file to an AWS S3 bucket daily and at any time. The Airflow DAG, implemented in minio_sensor_dag.py, checks for the presence of this file on MinIO at specified time intervals before proceeding to the next task. This ensures that other tasks, such as processing or transferring the file, are triggered only when the specified file is available.

## Project Structure

- **`Dockerfile`:** Defines the extended Airflow Docker image with additional dependencies for amazon operators.
- **`docker-compose.yml`:** Composes the Airflow deployment without MinIO container.
- **`dags/`:** Contains Airflow DAG script for object check for storage object.
- **`data/`:** Sample data for uploading to MinIO.
- **`requirements.txt`:** Lists Python dependencies for the extended Airflow image.

## Build and Run Docker Image Instructions

To build the Docker image and run the example Python script:

```bash
git clone https://github.com/ssoni11/AIRFLOW-S3-CHECK-OBJECT-PRESENCE.git
cd AIRFLOW-S3-CHECK-OBJECT-PRESENCE

# Create a requirements file with necessary dependencies
echo "apache-airflow-providers-amazon==8.15.0" > requirements-extended.txt

# Build the extended Airflow Docker image
docker build -t extended-airflow:[choose version] -f Dockerfile .

# Initialize Airflow
docker-compose up airflow-init

# Run flow in detached mode
docker-compose up -d

```
<!--
# Pulling from Docker Hub
docker pull sagarsonidockerhub/docker-python-venv-executable
-->

## MinIO Setup

- Here we use MinIO as an object storage solution that provides Amazon Web Services S3-compatible API and supports all core s3 features. Here we have deployed rootless docker image for MinIO container. As it is AWS S3 compatible you can use Aws S3 API to connect MinIO.
```bash
docker run \
   -p 9000:9000 \
   -p 9001:9001 \
   --name minio1 \
   --security-opt "credentialspec=file://path/to/file.json"
   -e "MINIO_ROOT_USER=ROOTUSER" \
   -e "MINIO_ROOT_PASSWORD=CHANGEME123" \
   -v D:\data:/data \
   quay.io/minio/minio server /data --console-address ":9001"
```
- Create a bucket on MinIO with read/write access.
- Upload a sample file from the /data directory to the MinIO bucket.
- 

## Airflow Initialization
Use Docker Compose to initialize Apache Airflow along with MinIO:
```bash
# Launch Apache Airflow and MinIO containers
docker-compose up -d
```
## Airflow Connections
- Create Amazon Web Service connection to connect with MinIO.


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

