Here is a **clean, professional README.md** you can directly upload to **GitHub** ✅
(Simple English, beginner-friendly, industry style)

---

# 🚀 FastAPI + MongoDB + React (Full Stack Basics)

This project demonstrates a **basic full-stack flow** where:

* React frontend sends data
* FastAPI backend receives it
* MongoDB stores the data

This repo is ideal for **beginners learning backend + frontend integration**.

---

## 🧠 Tech Stack

### Frontend

* React (Vite)
* JavaScript
* Fetch API

### Backend

* Python
* FastAPI
* Motor (Async MongoDB driver)

### Database

* MongoDB (Local)

---

## 📁 Project Structure

### Frontend (React)

```
frontend/
│── App.jsx
│── main.jsx
│── index.css
│── App.css
│
└── components/
    ├── Name.jsx
    └── Name.css
```

### Backend (FastAPI)

```
backend/
│── main.py
```

---

## ⚙️ Backend Setup (FastAPI + MongoDB)

### 1️⃣ Install dependencies

```bash
pip install fastapi uvicorn motor
```

### 2️⃣ Start MongoDB

Make sure MongoDB is running locally:

```bash
mongod
```

MongoDB URL used:

```
mongodb://localhost:27017
```

---

### 3️⃣ Backend Code (`main.py`)

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

# Enable CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["user_db"]
collection = db["users"]

# Schema
class UserName(BaseModel):
    name: str

# POST API
@app.post("/submit-name")
async def submit_name(user: UserName):
    result = await collection.insert_one({"name": user.name})
    return {
        "message": "Data saved successfully",
        "id": str(result.inserted_id)
    }
```

---

### 4️⃣ Run Backend

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🎨 Frontend Setup (React)

### 1️⃣ Install dependencies

```bash
npm install
```

### 2️⃣ Start React App

```bash
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 🔄 Data Flow (Easy Explanation)

```
User enters name
      ↓
React sends POST request
      ↓
FastAPI receives JSON
      ↓
MongoDB stores data
      ↓
Backend sends response
      ↓
Frontend shows alert
```

---

## 🧪 API Testing (Without Frontend)

### Endpoint

```
POST /submit-name
```

### Body (JSON)

```json
{
  "name": "Siddu"
}
```

---

## 🗄️ MongoDB Output

After first insert, MongoDB will automatically create:

```
user_db
 └── users
      └── { "_id": ObjectId(...), "name": "Siddu" }
```

> ⚠️ MongoDB creates databases **only after data insertion**

---

## ❗ Common Issues & Fixes

### ❌ OPTIONS 404 Error

✔ Fixed by enabling **CORS middleware**

### ❌ Database not visible

✔ Insert at least one document

### ❌ Frontend not connecting

✔ Ensure:

* Backend runs on `8000`
* Frontend runs on `5173`

---

## 📌 Key Learnings

* FastAPI POST APIs
* Pydantic schemas
* Async / await
* MongoDB insert
* CORS handling
* React → Backend communication

---

## 👤 Author

**Gururaj Kondaguli**
Learning Full Stack Development 🚀

---

## ⭐ Future Improvements

* GET API to fetch users
* Update & Delete APIs
* Environment variables
* Authentication
* Deployment

---
 
