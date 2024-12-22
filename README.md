# Insait Application

A Flask-based application leveraging PostgreSQL and Docker for development, testing, and deployment. This project is designed with best practices, including containerization, efficient testing, and modular architecture.

---

## Table of Contents

- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Usage](#usage)
- [Testing](#testing)
- [Available Makefile Commands](#available-makefile-commands)

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone git@github.com:swallahfx/Insait.git
   cd insait
   ```
2. **Ensure Docker and Docker Compose Are Installed**
    `Docker`
    `Docker Compose`
3. **Set Up Environment Variables Create a .env file in the root of your project**
   Use the template in `sample.env`


## Environment Setup

**The project uses Docker for containerization. Follow these steps:**
1. **Build and Start the Application**
    `make build
     make up `

2. **Run Migrations Apply migrations to set up the database schema:**
     `make migrate`

3. **View Logs To monitor the running services:**
     `make logs`

4. **Stop the Application**
     `make down`


## Usage
**Once the application is running, access it via your browser:**

Development Server: `http://127.0.0.1:5001`
**You can access the `/ask` endpoint from the simple front page by asking a question**
**and click on the ask button**


## Testing
**To ensure the application is functioning as expected:**
**Make sure environment variable in the .env is set**

***Run Tests Execute the test suite:***
    `make test `

**View Test Logs Check the test logs for details:**
    `docker-compose logs test`

## Available Makefile Commands
***Description***
make build:	Builds the Docker images.
make up:	Start all services (app, database, etc.).
make migrate:	Apply database migrations.
make logs:	View logs of all running containers.
make down:	Stop and remove all running containers.
make test:	Build the test environment and execute tests.
make restart:	Restart the application services.
make shell:	Run the shell
make clean:	Clean up volumes and images
