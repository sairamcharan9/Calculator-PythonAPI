# Python Calculator API

A simple calculator application with automated testing and CI/CD.

## Assignment Overview

This project demonstrates:
- **Python Project Setup** - Virtual environment configuration in VSCode
- **Calculator Functions** - Basic arithmetic operations (add, subtract, multiply, divide)
- **Unit Testing** - Comprehensive test suite using pytest
- **CI/CD Integration** - GitHub Actions runs tests automatically on every push

## Project Structure

```
Python_Project/
├── calculator.py        # Calculator functions
├── test_calculator.py   # Pytest test suite
├── requirements.txt     # Dependencies
├── .github/workflows/   # GitHub Actions CI config
└── venv/                # Virtual environment
```

## Running Locally

```bash
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest -v
```

## CI/CD

Tests run automatically via GitHub Actions on:
- Push to `main` branch
- Pull requests to `main` branch
