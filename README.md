# Wallet User Identity Service Makefile

This Makefile provides a set of commands to help with building, running, and managing the Wallet User Identity Service.

## Prerequisites

Before using this Makefile, make sure you have the following dependencies installed:

- Docker

## Usage

### Set Environment Variables

Before running the service, ensure that the necessary environment variables are set. These can be configured in the Makefile or directly in your shell.
```
export FLASK_APP=src/app/app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_PORT=8083
export PYTHONPATH=$(shell pwd)
export JWT_SECRET=CREATE_RANDOM_SECRET_KEY
```

### Available Commands

- make start: Run the Flask application in development mode.

- make clean: Clean up any cached files (e.g., __pycache__).

- make build: Build the Docker image for the service.

- make run: Run the Docker container using the built image.

- make stop: Stop and remove the running Docker container.

- make db-migrate: Apply database migrations (assuming a SQL migration file is available at src/infra/db/database/migration.sql).

## Docker Image and Container Naming

- Docker Image Name: wallet_user_identity_service_image

- Docker Container Name: wallet_user_identity_service_container

## API Design Documentation

The Swagger file for this service is located at `docs/open_api/swagger.yaml`. It contains the API documentation and can be used with tools like Swagger UI to interact with the service.

## Additional Notes

- Remember to replace CREATE_RANDOM_SECRET_KEY with your actual JWT secret key.
