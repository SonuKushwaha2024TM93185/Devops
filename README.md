# DevOps Assignment 2 – End-to-End CI/CD Pipeline

This repository contains the complete source code, automation scripts, Docker configuration, testing setup, and Jenkins CI/CD pipeline for **Assignment 2** as per the DevOps course requirements.

## Project Overview

The project is a Python-based application for tracking fitness activities with a Tkinter-based GUI. The repository has been extended to support:

Automated testing using **Pytest**
Code quality scanning using **SonarQube**
Packaged deployment using **Docker**
CI/CD via **Jenkins** with build → test → scan → dockerize → deploy stages

## Repository Structure

Devops/
├── ACEest_FitnessV11.py
├── ACEest_FitnessV12.py
├── ACEest_FitnessV13.py
├── ACEest_FitnessV121.py
├── ACEest_FitnessV122.py
├── ACEest_FitnessV123.py
│── tests/
│    └── test_app.py
│── docker/
│    ├── Dockerfile
│    └── docker-compose.yml
│── jenkins/
│    └── Jenkinsfile
│── sonar/
│    └── sonar-project.properties
│── requirements.txt
│── README.md
│── .gitignore
## Technologies Used

Python 3.12
Tkinter GUI Framework
Pytest for unit testing
SonarQube for static analysis
Docker for containerization
Jenkins for CI/CD
Git & GitHub for version control

## Testing Setup (Pytest)

Unit tests are located inside the `tests/` directory.

### Run tests locally:
pytest -v

Tests are executed automatically during the Jenkins pipeline.

## Docker Setup

A docker image is built using the Dockerfile located in `/docker`.

Build the docker image manually:

docker build -t fitness-app:latest -f docker/Dockerfile .

Run the container:
docker run -p 5000:5000 fitness-app:latest
SonarQube Code Quality Scan
The pipeline includes SonarQube analysis.
A sample configuration file is under:
sonar/sonar-project.properties

SonarQube server must be added in Jenkins under:
Manage Jenkins → Configure System → SonarQube Servers
CI/CD Pipeline (Jenkins)

The Jenkinsfile automates the full lifecycle:

Pipeline Stages

1. Checkout Code from GitHub
2. Install Dependencies using pip
3. Run Unit Tests with Pytest
4. SonarQube Analysis for code quality
5. Build Docker Image
6. Push Image to DockerHub (optional)
7. Deploy the Container

You can find the Jenkinsfile under:

jenkins/Jenkinsfile
Environment Requirements

Ensure the following are installed:

* Python 3.x
* Pip
* Jenkins
* Docker
* SonarQube Server (Locally or Remote)
git clone <repository-url>
cd Devops

Switch to the assignment 2 branch:

git checkout Assignment-2-Devops

Developed By
Sonu Kushwaha