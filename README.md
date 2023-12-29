# Personalized Learning Assistant for Educational Equity (PLEA)

## Overview
PLEA is a Flask-based backend system designed to provide personalized learning experiences to users. It tracks user progress and suggests the next learning steps.

## Setup
- Install Python and pip.
- Clone this repository.
- Run `pip install -r requirements.txt` to install dependencies.

## Running the Application
- Execute `python app.py` to start the Flask server.
- Access the API at `localhost:5000/api/user/<username>/progress`.

## API Endpoints
- `GET /api/user/<username>/progress`: Retrieves the user's learning progress.
- `POST /api/user/<username>/progress`: Updates the user's learning progress.

## Contributions
We welcome contributions to PLEA. Please read `CONTRIBUTING.md` for details on code of conduct, and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.
