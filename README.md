# Mathematical Microservice API

A Python-based microservice for performing mathematical operations and logging requests. Built with FastAPI, using SQLite for persistence.
Team members includes Lorena Buzea (lorenabuzea) and Vlad Cira (ciravlad)

## Features

- Exposes RESTful endpoints for mathematical operations (e.g., power calculation).
- Logs each request to a database.
- Modular structure: controllers, services, models, and views.

## Directory Structure
mathematical-microservice-api/ 
├── app/
│ ├── controllers/
│ ├── models/
│ ├── services/
│ ├── views/
│ ├── main.py
│ └── config.py
├── requirements.txt
├── requests.db
├── README.md

## Prerequisites

- Python 3.13+
- pip (Python package manager)

## Setup

1. **Clone the repository:**
  git clone <repository-url> cd mathematical-microservice-api

2. **Create a virtual environment (optional but recommended):**
  python -m venv venv venv\Scripts\activate

3. **Install dependencies:**
  pip install -r requirements.txt

4. **Initialize the database:**
   The database (`requests.db`) is created automatically on first run.

## Running the Service

Start the Flask application:
  python app/main.py

The API will be available at `http://localhost:5000`.

## API Endpoints

### Mathematical Operations

- **POST /math/pow**
  - Request: `{ "base": <number>, "exponent": <number> }`
  - Response: `{ "result": <number> }`

### Logs

- **GET /logs**
  - Returns a list of logged requests.

## Testing

Unit tests are located in `app/tests/`. To run tests:
  python -m unittest discover app/tests

## Project Structure Overview

- `app/controllers/`: Handles HTTP requests and routes.
- `app/services/`: Business logic for math operations and logging.
- `app/models/`: Database models and session management.
- `app/views/`: Request/response schemas.
- `app/main.py`: Entry point for the Flask app.
- `requirements.txt`: Python dependencies.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## License

This project is licensed under the MIT License & Endava Dava.X programme License.

---

For any questions, contact your supervisor or check the code comments for guidance.
