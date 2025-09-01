
# TaskBuddy ✅

TaskBuddy is a simple Task Management API built with **Django REST Framework**.  
It allows users to create, update, delete, and manage tasks, with authentication using JWT.  
The project is designed to be clean, efficient, and production-ready.

---

## 🚀 Features
- User authentication with JWT (login & registration).
- CRUD operations for tasks.
- Mark tasks as complete or incomplete.
- Admin panel for managing users and tasks.
- Built with **Django ORM** for database interactions.
- Can be deployed on **Heroku** or **PythonAnywhere**.

---

## 🛠️ Tech Stack
- Python 3.13.7
- Django 5.2.5
- Django REST Framework
- SimpleJWT (for authentication)
- SQLite (default, but can be switched to Postgres/MySQL in production)

---

## 📂 Project Structure
```
taskbuddy/
│── manage.py
│── taskbuddy_project/        # Project settings
│── tasks/            # Task app (CRUD + endpoints)
│── requirements.txt  # Dependencies
│── .venv              # Environment variables (not pushed to GitHub)
│── README.md         # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/taskbuddy.git
cd taskbuddy
```

### 2️⃣ Create & activate virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scriptsctivate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Run development server
```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔑 Authentication
We use **JWT** for authentication.

### Get Token
**POST** `/api/token/`
```json
{
  "username": "your-username",
  "password": "your-password"
}
```

### Refresh Token
**POST** `/api/token/refresh/`

### Protected Endpoints
When accessing protected endpoints, include the token:
```
Authorization: Bearer your_access_token
```

---

## 📌 API Endpoints

### Auth
- `POST /api/token/` → Get JWT token
- `POST /api/token/refresh/` → Refresh token

### Tasks
- `GET /api/tasks/` → List all tasks
- `POST /api/tasks/` → Create a new task
- `GET /api/tasks/{id}/` → Get task by ID
- `PUT /api/tasks/{id}/` → Update a task
- `DELETE /api/tasks/{id}/` → Delete a task

---

## 🧪 Testing with Postman
1. Obtain token using `/api/token/`
2. Copy **access token**
3. In Postman, under **Authorization**, choose **Bearer Token** and paste your token.
4. Send requests to `/api/tasks/`.

---

## 🚀 Deployment
Can be deployed on:
- **Heroku**
- **PythonAnywhere**

Steps involve:
1. Setting up Postgres DB
2. Configuring `ALLOWED_HOSTS` and `DEBUG`
3. Using Gunicorn for production

---

## 👨‍💻 Author
**Samuel Praise**  
Entry-level Backend Developer | UI/UX Designer | Tech Enthusiast

---

## 📄 License
This project is licensed under the MIT License.
