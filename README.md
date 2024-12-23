# Insait Application

This project is a Flask-based APP that allows users to submit questions and receive answers dynamically. It uses PostgreSQL as the database, with Alembic and Flask-Migrate for efficient database schema management and versioning. It also includes robust error handling and a seamless process for managing migrations and schema changes.

---

## Table of Contents

- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Usage](#usage)
- [Testing](#testing)
- [Available Makefile Commands](#available-makefile-commands)
- [Note](#make-issues)

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
**make sure OPENAI_API_KEY is provided in your .env for integration test to work fully**
    `make test `

**View Test Logs Check the test logs for details:**
    `docker-compose logs test`

## Available Makefile Commands
***Description***
- `make build`: Builds the Docker images.  
- `make up`: Start all services (app, database, etc.).  
- `make migrate`: Apply database migrations.  
- `make logs`: View logs of all running containers.  
- `make down`: Stop and remove all running containers.  
- `make test`: Build the test environment and execute tests.  
- `make restart`: Restart the application services.  
- `make shell`: Run the shell.  
- `make clean`: Clean up volumes and images.  

## Make Issues?
**If you get an error like `make: *No rule to make target make. Stop. `**
run
- `make -f makefile`