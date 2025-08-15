# Mathematical Microservice API

A Python-based microservice for performing mathematical operations and logging requests.  
Built with **FastAPI**, using **SQLite** for persistence and a modular service-oriented architecture.

Developed by:  
- Lorena Buzea (`lorenabuzea`)  
- Vlad Cira (`ciravlad`)

---

## 🚀 Features

- RESTful **POST** endpoints for mathematical operations (power, factorial, Fibonacci)
- Logs each incoming request to a local SQLite database
- Asynchronous CPU-bound execution via `ProcessPoolExecutor`
- Modular structure with clear separation of concerns
- Includes unit and performance tests

---

## 🛠️ Setup Instructions

### Requirements

- Python 3.13+
- `pip` (Python package manager)
- Virtual environment (recommended)

### Installation

```bash
git clone <repository-url>
cd mathematical-microservice-api

python -m venv .venv
.venv\Scripts\activate         # On Windows
# or
source .venv/bin/activate     # On macOS/Linux

pip install -r requirements.txt
```

> The SQLite database (`requests.db`) is created automatically on first run.

---

## ▶️ Running the Service

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

Open the Swagger UI in your browser:  
**http://127.0.0.1:8000/docs**

---

## 📡 API Endpoints

> All math endpoints accept `POST` requests with JSON bodies.

### Mathematical Operations

- **`POST /pow`**  
  Compute exponentiation  
  **Request body:**  
  ```json
  { "base": 2, "exponent": 10 }
  ```

- **`POST /factorial`**  
  Compute the factorial of a number  
  **Request body:**  
  ```json
  { "number": 5 }
  ```

- **`POST /fibonacci`**  
  Compute the nth Fibonacci number  
  **Request body:**  
  ```json
  { "n": 10 }
  ```

### Logs

- **`GET /logs`**  
  Returns a list of logged requests with timestamps and execution times

### Docs

- **`GET /docs`** — Interactive Swagger UI  
- **`GET /openapi.json`** — OpenAPI specification

---

## 🧪 Testing

### Unit tests

```bash
python -m unittest discover app/tests
```

### Performance benchmark

```bash
pytest --benchmark-only
```

Optional: simulate concurrency with `scripts/stress_test.py`

---

## ⚡ Performance Notes

- For simple and fast mathematical operations (like `pow`, small factorials, or Fibonacci with low `n`), **synchronous execution performs better** due to minimal computation time and no multiprocessing overhead.
- Asynchronous execution with `ProcessPoolExecutor` is still implemented to support scalability and CPU isolation if needed, but may not yield a speed advantage for small inputs.
- You can evaluate cold vs warm performance using the stress test script in `scripts/stress_test.py`.

---

## 📄 License

Licensed under the **MIT License** and the **Endava Dava.X Programme License**.
