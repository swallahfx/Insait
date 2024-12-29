MAKE = docker-compose

up:
	$(MAKE) up

# Build containers without starting them
build:
	$(MAKE) build

migrate:
	$(MAKE) exec app flask db upgrade

# Run tests
test:
	$(MAKE) exec app pytest -s -v

# Stop and remove containers, networks, volumes, and images
down:
	$(MAKE) down

# Clean up volumes and images
clean:
	$(MAKE) down --volumes --rmi all

# Restart the containers
restart:
	$(MAKE) restart

# View logs of all containers
logs:
	$(MAKE) logs -f

# Execute a bash shell inside the app container (replace app with the service name)
shell:
	$(MAKE) exec app bash

# Show the status of containers
status:
	$(MAKE) ps

downgrade:
	$(MAKE) exec app flask db downgrade base
