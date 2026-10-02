# ☕ chaiMenu

A simple **read-only REST API for a chai shop menu**, built while learning **FastAPI and Pydantic**.

The API provides menu items, supports filtering by category, and allows individual menu items to be retrieved by their ID.

> 🎯 **Purpose:** This project was built as a learning project to understand the fundamentals of building APIs with FastAPI.

---

## 🚀 Features

* 📋 Get the complete chai menu
* 🔎 Filter menu items by category
* 🔢 Get a specific menu item by ID
* ✅ Request/response validation using Pydantic
* ⚠️ HTTP exception handling for invalid requests
* 🧩 FastAPI `Query` parameters
* 📦 Structured API responses using Pydantic models
* 📖 Automatic API documentation with Swagger UI

---

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **Pydantic**
* **Uvicorn**

---

## 📁 Project Structure

```text
chaiMenu/
│
├── main.py
├── models.py
├── data.py
├── requirements.txt
└── .gitignore
```



# 🔄 How the API Works

The basic flow is:

```text
Client
  │
  │ HTTP Request
  ▼
FastAPI
  │
  ├── Query Parameter / Path Parameter
  │
  ▼
Endpoint Function
  │
  ├── Search / Filter menu data
  │
  ├── Handle exceptions
  │
  ▼
Pydantic Response Model
  │
  ▼
JSON Response
```

For example:

```text
GET /menu?category=chai
        │
        ▼
FastAPI receives category
        │
        ▼
Filter menu_items
        │
        ▼
Create MenuResponse
        │
        ▼
Return JSON
```

---

# ⚙️ Getting Started

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd chaiMenu
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the server

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

You can use Swagger UI to test the API endpoints directly from your browser.

---


# 📚 What I Learned

Through this project, I practiced:

* FastAPI application setup
* Creating API routes
* HTTP GET requests
* Path parameters
* Query parameters
* `Query()` in FastAPI
* Pydantic `BaseModel`
* Pydantic validation
* Response models
* Nested Pydantic models
* Python type hints
* Optional parameters
* List filtering
* FastAPI exception handling
* `HTTPException`
* FastAPI's dependency injection concepts
* Automatic API documentation
* Running APIs with Uvicorn

---

# 🔮 Future Improvements

Possible improvements for future versions:

* Add `POST` endpoint to create menu items
* Add `PUT/PATCH` to update items
* Add `DELETE` endpoint
* Connect a real database
* Add database models with SQLAlchemy
* Add request validation for creating/updating items
* Add authentication and authorization
* Add pagination
* Add automated tests
* Deploy the API

---

## 👨‍💻 Author

**Rathod Umesh**

Built as part of my journey learning **FastAPI, backend development, and REST APIs**.
