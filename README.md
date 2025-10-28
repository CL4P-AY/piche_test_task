## Banking System API

This project is a Banking System API implemented in Python using FastAPI as part of a technical assignment.
The API allows users to create accounts, manage funds, and perform basic user operations such as registration and authentication.

## 🧩 Framework Choice

Although the original assignment suggested using Flask, I confirmed with HR that I could use FastAPI instead.
I chose FastAPI because it provides more built-in tools for rapid API development — including automatic validation, schema generation, and interactive documentation — which made it the most efficient choice for this particular task.

✅ All core and optional requirements from the original assignment were implemented (except for the use of Flask, as approved by HR).

While I have experience with both Django and FastAPI, I decided to use FastAPI because Django would have been unnecessarily heavy for the required functionality.
FastAPI offered a clean and concise way to demonstrate my skills while staying focused on the assignment goals.

## 🚀 Running the Application

To run the project:

Create a virtual environment and install dependencies from requirements.txt:

- `pip install -r requirements.txt`


Start the FastAPI application:

- `uvicorn main:app --reload`


The application will be available at http://127.0.0.1:8000
.

### 📘 API Documentation

You can explore and test all endpoints directly via the built-in Swagger UI:

👉 http://127.0.0.1:8000/docs#/

## 🧠 Implemented Endpoints

### 🏦 **Accounts**

**GET endpoints**
- `GET /accounts/` — Get all accounts  
- `GET /accounts/{account_id}` — Get account details by ID  
- `GET /accounts/transactions` — Get all transactions (logging system)

**POST endpoints**
- `POST /accounts/create_account` — Create a new account  
- `POST /accounts/withdraw` — Withdraw funds from an account  
- `POST /accounts/transfer` — Transfer funds between accounts  

---

### 👤 **Users**

**POST endpoints**
- `POST /users/register` — Register a new user  
- `POST /users/login` — Log in an existing user  

**GET endpoints**
- `GET /users/me` — Retrieve current user information  

---

## ⚙️ Technologies Used

- Python 3.x

- FastAPI

- Uvicorn — ASGI server

- Pydantic — for request/response validation

### 🧾 Notes

- By default, the application has a limit of 10 requests per minute, just for demonstration purposes, which can be changed in `settings.py`.
- The API can be tested via Swagger UI without external tools.
Error handling and input validation are implemented for key operations.