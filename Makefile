# Makefile for testapp.py

.PHONY: all run build test lint format status pull push

# Variables
COUNT ?= 10

all: test lint

# Target to run the application
run:
	@echo "Running the application..."
	@python testapp.py $(COUNT)

# Target to build the application (placeholder)
build:
	@echo "Building the application..."
	@echo "No build steps defined for this project."

# Target to run tests
test:
	@echo "Running tests..."
	@python -m unittest discover tests

# Target to lint the code
lint:
	@echo "Linting the code..."
	@flake8 .

# Target to format the code
format:
	@echo "Formatting the code..."
	@black .

# Target to show git status
status:
	@echo "Showing git status..."
	@git status

# Target to pull latest changes from git
pull:
	@echo "Pulling latest changes from git..."
	@git pull

# Target to push changes to git
push:
	@echo "Pushing changes to git..."
	@git push
