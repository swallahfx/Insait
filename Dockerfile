# Dockerfile
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app
ENV FLASK_ENV=development

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Ensure .env is recognized by Flask
RUN pip install python-dotenv

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]


## Use the official Python base image
#FROM python:3.8
#
## Set the working directory
#WORKDIR /app
#
## Copy the requirements.txt and install dependencies
#COPY requirements.txt /app/
#RUN pip install --no-cache-dir -r requirements.txt
#
## Copy the application code into the container
#COPY . /app/
#
## Make entrypoint.sh executable and set the entrypoint
#RUN chmod +x /app/entrypoint.sh
#
## Set the default entrypoint for the container
#ENTRYPOINT ["/app/entrypoint.sh"]


#FROM python:3.9-slim
#
## Install PostgreSQL client utilities
#RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*
#
## Set the working directory
#WORKDIR /app
#
## Install Python dependencies
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
#
## Copy application code
#COPY . .
#
## Entrypoint
#ENTRYPOINT ["/app/entrypoint.sh"]
#
## Default command
#CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
