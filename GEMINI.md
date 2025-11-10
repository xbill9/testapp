# Gemini Code Assistant Context

This document provides context to the Gemini code assistant to help it generate code that is consistent with the project's standards and conventions.

## Project Overview

This project is a Python application that generates Fibonacci sequences. The main logic is in `fibonacci_generator.py`.

## Tech Stack

- Python 3.x

## Project Structure

- `fibonacci_generator.py`: The main application file.
- `tests/`: Directory for unit tests.
- `requirements.txt`: A file listing the project's dependencies.
- `GEMINI.md`: This file.

## Coding Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
- Use type hints for all function signatures.
- Use f-strings for string formatting.
- Write clear and concise comments for complex logic.

## Testing

- Use the `unittest` framework for writing tests.
- Place all tests in the `tests/` directory.
- Test files should be named `test_*.py`.
- Run tests using the command: `python -m unittest discover tests`

## Dependencies

- Manage dependencies using `pip` and a `requirements.txt` file.
- To install dependencies, run: `pip install -r requirements.txt`
- To add a new dependency, add it to `requirements.txt` and then run the install command.

## Environment Variables

- Do not hardcode sensitive information or configuration values in the code.
- Use environment variables for configuration.
- Create a `.env` file for local development and load it using a library like `python-dotenv`.
- The `.env` file should be added to `.gitignore` to avoid committing it to the repository.

## Linting and Formatting

- Use `flake8` for linting to enforce PEP 8 compliance.
- Use `black` for automatic code formatting.
- Configuration for these tools should be in a `pyproject.toml` or `setup.cfg` file.
- Run linting with: `flake8 .`
- Run formatting with: `black .`

## Commits

- Follow the [Conventional Commits](httpss://www.conventionalcommits.org/en/v1.0.0/) specification.
- Example commit messages:
  - `feat: Add new feature`
  - `fix: Correct a bug`
  - `docs: Update documentation`
  - `style: Format code`
  - `refactor: Refactor code`
  - `test: Add or improve tests`
  - `chore: Update build scripts or other non-code changes`

## CI/CD

- A CI/CD pipeline is set up to automatically run tests, linting, and formatting on every push to the main branch.
- The pipeline is defined in a `.github/workflows/main.yml` file (for GitHub Actions).
