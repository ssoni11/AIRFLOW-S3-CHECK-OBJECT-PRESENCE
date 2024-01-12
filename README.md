<!--
#DAG-WITH-S3-CHECK_OBJECT_PRESENCE
-->
# Apache Airflow - AWS S3(MinIO) Sensor Example

## Use Case

This project is specifically designed to address a scenario where our client routinely uploads files to an AWS S3 bucket, both on a daily basis and at varying times. Employing an orchestrated workflow powered by Docker and Python, the Apache Airflow Directed Acyclic Graph (DAG) implemented in DAG-WITH-S3-CHECK_OBJECT_PRESENCE.py systematically verifies the presence of the uploaded file on MinIO at predefined intervals. This meticulous validation mechanism is integral to ensuring that subsequent tasks, including file processing or transfer operations, are activated exclusively when the specified file is confirmed to be accessible. The combination of Docker and Python further enhances the robustness and reliability of this intricate design.

## Project Structure

- **`Dockerfile`:** Defines the extended Airflow Docker image with additional dependencies for amazon operators.
- **`docker-compose.yml`:** Composes the Airflow deployment without MinIO container.
- **`dags/`:** Contains Airflow DAG script for different initiatives like storage object presence.
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
  

## Airflow Connections
- Create Amazon Web Service API connection to connect with MinIO.

## DAG Execution
- The Airflow DAG script (dags/DAG-WITH-S3-CHECK_OBJECT_PRESENCE.py) checks for the presence of a specific object on MinIO before proceeding to the next task.

## Check Python Dependencies
- To check if AWS S3 dependencies are installed in the Airflow container:
```bash
# Find the container ID of the running Airflow container
docker ps

# Access the Airflow container shell
docker exec -it [airflow_scheduler_container_id] bash

# Run the following command inside the container
pip list | grep amazon*
```

- Ensure that the installed dependencies match your local installation version with the Airflow sensor API for AWS S3.

- Feel free to adjust the project structure and instructions based on your specific requirements and preferences.

