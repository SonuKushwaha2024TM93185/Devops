# ACEest Fitness & Gym – DevOps Assignment

This repository contains a basic Flask web application for **ACEest Fitness & Gym**, containerized using Docker and integrated with a **CI/CD pipeline** using GitHub Actions.

The objective of this project is to demonstrate fundamental **DevOps practices**, including version control, unit testing, containerization, and automation.

---

## 🚀 How to Set Up and Run the Application Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/SonuKushwaha2024TM93185/Devops.git
   cd Devops
2. Create a virtual environment and install dependencies:
    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows
    pip install -r requirements.txt
3. Run the Flask app:
   python ACEest_Fitness.py

4. Run tests with:
   pytest
5. Build the Docker image:
   docker build -t aceest-fitness .
6. Run the container:

Project Structure

   Devops/
│-- ACEest_Fitness.py        # Flask application
│-- test_fitness_app.py      # Unit tests (Pytest)
│-- requirements.txt         # Python dependencies
│-- Dockerfile               # Docker container instructions
│-- .github/workflows/main.yml # GitHub Actions workflow
│-- README.md                # Documentation
