# **Task Management API (Django REST Framework)**  

A simple API for managing tasks with authentication, task creation, member management, and status updates.  

# **Features**
User Authentication: Register & login with token-based authentication.

Task Management: Create, retrieve, update, and delete tasks.

Task Members: Add or remove users from a task.

Task Status Updates: Change task status (Todo, Inprogress, Done).

# **Technologies Used**
Django & Django REST Framework

SQLite (default)

djangorestframework-simplejwt (for token authentication)

---

## **📌 Setup & Installation**  

1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/Sewak2001/Task-Management.git
cd Task-Management
```

2️⃣ **Create a Virtual Environment**  
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ **Install Dependencies**  
```sh
pip install -r requirements.txt
```

4️⃣ **Apply Migrations**  
```sh
python manage.py migrate
```

5️⃣ **Run the Server**  
```sh
python manage.py runserver
```
The API will be available at:  
🔗 `http://127.0.0.1:8000/`

---

## **📜 API Endpoints**  

### **🔹 Authentication**  
| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/accounts/register/` | Register a new user |
| **POST** | `/accounts/login/` | Login and get a token |

#### **Register User**
```json
{
  "username": "test",
  "email": "test@gmail.com",
  "phone_number": "1234567890",
  "password": "password123"
}
```

---

### **🔹 Task Management**  
| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/tasks/` | Create a new task |
| **GET** | `/tasks/` | Get all tasks |
| **PATCH** | `/tasks/{id}/status/` | Update task status |

#### **Create Task**
```json
{
  "title": "Project Meeting",
  "description": "Discuss project updates",
  "due_date": "2025-04-15",
  "status": "Todo"
}
```

---

### **🔹 Task Members**  
| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/tasks/{id}/members/` | Add a member to a task |
| **DELETE** | `/tasks/{id}/members/` | Remove a member from a task |

#### **Add Member**
```json
{
  "user_id": 2
}
```

#### **Remove Member**
```json
{
  "user_id": 2
}
```

---

## **🔑 Authentication & Token Usage**  
1️⃣ **Login to get a token**  
```sh
POST /accounts/login/
```
2️⃣ **Use the token in requests**  
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## **📞 Contact**  
For any questions, contact **[Sewak Ram]** at **sewak6188@gmail.com**.  

