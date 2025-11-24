# Student Management API - Django REST Framework with MongoDB

A complete REST API for managing student records built with Django REST Framework and MongoDB. This API provides full CRUD (Create, Read, Update, Delete) functionality for student data.

## 🚀 Features

- ✅ Full CRUD operations for student management
- ✅ MongoDB integration using Djongo
- ✅ RESTful API endpoints
- ✅ JSON request/response format
- ✅ Data validation and error handling
- ✅ Unique roll number and email constraints
- ✅ Detailed API responses with proper HTTP status codes
- ✅ Easy to test with Postman or cURL

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- MongoDB 4.0 or higher (running locally on port 27017)
- pip (Python package installer)
- virtualenv (recommended)

## 🛠️ Installation & Setup (Codespace/Cloud Environment)

### Quick Setup (Automated)

```bash
# Run the automated setup script
./setup.sh
```

This will:
- Install and start MongoDB
- Install Python dependencies
- Run Django migrations
- Set up the project

Then start the server:
```bash
python manage.py runserver
```

---

### Manual Setup

### 1. Install MongoDB in Codespace

MongoDB has been pre-installed! To start it:

```bash
# Create data directory
sudo mkdir -p /data/db
sudo chown -R $USER:$USER /data/db

# Start MongoDB
mongod --dbpath /data/db --fork --logpath /data/db/mongodb.log
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Start the Development Server

```bash
# Foreground (you'll see logs)
python manage.py runserver

# Or background
nohup python manage.py runserver > server.log 2>&1 &
```

---

### Option B: Using MongoDB Atlas (Cloud MongoDB)

If you prefer cloud-hosted MongoDB:

1. Create a free account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register)
2. Create a cluster and get your connection string
3. Set the environment variable:

```bash
export MONGODB_URI="mongodb+srv://username:password@cluster.mongodb.net/"
```

4. Follow steps 2-4 from Manual Setup above

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional - for Admin Panel)

```bash
python manage.py createsuperuser
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000/` or your Codespace forwarded port URL

## 📚 API Endpoints

### Base URL
```
http://127.0.0.1:8000/students/
```

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/students/` | Create a new student |
| GET | `/students/` | Get all students |
| GET | `/students/{roll_no}/` | Get a specific student by roll number |
| PUT | `/students/{roll_no}/` | Update a student's details (full update) |
| PATCH | `/students/{roll_no}/` | Partially update a student's details |
| DELETE | `/students/{roll_no}/` | Delete a student |

## 📝 Student Model Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Auto-generated, Primary Key | Unique identifier |
| name | String | Required, Max 200 chars | Student's full name |
| roll_no | Integer | Required, Unique, Positive | Student's roll number |
| course | String | Required, Max 100 chars | Course name |
| marks | Integer | Required, 0-100 | Marks obtained |
| email | String | Required, Unique, Valid email | Student's email |

## 🧪 Testing with Postman/cURL

### Quick Test (Automated)

Run the included test script to test all endpoints:

```bash
./test_api.sh
```

This will automatically test:
- Creating students
- Listing all students
- Getting a specific student
- Updating student data
- Deleting a student
- Error handling

---

### Manual Testing

### 1. Create a Student (POST)

**Request:**
```bash
curl -X POST http://127.0.0.1:8000/students/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "roll_no": 101,
    "course": "Computer Science",
    "marks": 85,
    "email": "john.doe@example.com"
  }'
```

**Response (201 Created):**
```json
{
  "message": "Student created successfully",
  "data": {
    "id": 1,
    "name": "John Doe",
    "roll_no": 101,
    "course": "Computer Science",
    "marks": 85,
    "email": "john.doe@example.com"
  }
}
```

### 2. Get All Students (GET)

**Request:**
```bash
curl -X GET http://127.0.0.1:8000/students/
```

**Response (200 OK):**
```json
{
  "message": "Students retrieved successfully",
  "count": 2,
  "data": [
    {
      "id": 1,
      "name": "John Doe",
      "roll_no": 101,
      "course": "Computer Science",
      "marks": 85,
      "email": "john.doe@example.com"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "roll_no": 102,
      "course": "Data Science",
      "marks": 92,
      "email": "jane.smith@example.com"
    }
  ]
}
```

### 3. Get Student by Roll Number (GET)

**Request:**
```bash
curl -X GET http://127.0.0.1:8000/students/101/
```

**Response (200 OK):**
```json
{
  "message": "Student retrieved successfully",
  "data": {
    "id": 1,
    "name": "John Doe",
    "roll_no": 101,
    "course": "Computer Science",
    "marks": 85,
    "email": "john.doe@example.com"
  }
}
```

### 4. Update Student (PUT)

**Request:**
```bash
curl -X PUT http://127.0.0.1:8000/students/101/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe Updated",
    "roll_no": 101,
    "course": "Computer Science",
    "marks": 90,
    "email": "john.doe@example.com"
  }'
```

**Response (200 OK):**
```json
{
  "message": "Student updated successfully",
  "data": {
    "id": 1,
    "name": "John Doe Updated",
    "roll_no": 101,
    "course": "Computer Science",
    "marks": 90,
    "email": "john.doe@example.com"
  }
}
```

### 5. Partial Update Student (PATCH)

**Request:**
```bash
curl -X PATCH http://127.0.0.1:8000/students/101/ \
  -H "Content-Type: application/json" \
  -d '{
    "marks": 95
  }'
```

**Response (200 OK):**
```json
{
  "message": "Student updated successfully",
  "data": {
    "id": 1,
    "name": "John Doe Updated",
    "roll_no": 101,
    "course": "Computer Science",
    "marks": 95,
    "email": "john.doe@example.com"
  }
}
```

### 6. Delete Student (DELETE)

**Request:**
```bash
curl -X DELETE http://127.0.0.1:8000/students/101/
```

**Response (200 OK):**
```json
{
  "message": "Student deleted successfully",
  "roll_no": 101
}
```

### 7. Error Handling Examples

**Student Not Found (404):**
```json
{
  "error": "Student not found",
  "details": "Student with roll number 999 does not exist"
}
```

**Validation Error (400):**
```json
{
  "error": "Failed to create student",
  "details": "Marks must be between 0 and 100."
}
```

**Duplicate Roll Number (400):**
```json
{
  "error": "Failed to create student",
  "details": "Student with this roll_no already exists."
}
```

## 🎯 Postman Collection

You can import this collection to Postman for easier testing:

1. Create a new collection in Postman
2. Add the following requests:
   - **Create Student**: POST `http://127.0.0.1:8000/students/`
   - **Get All Students**: GET `http://127.0.0.1:8000/students/`
   - **Get Student**: GET `http://127.0.0.1:8000/students/101/`
   - **Update Student**: PUT `http://127.0.0.1:8000/students/101/`
   - **Partial Update**: PATCH `http://127.0.0.1:8000/students/101/`
   - **Delete Student**: DELETE `http://127.0.0.1:8000/students/101/`

## 📂 Project Structure

```
student-api-django-mongodb/
├── manage.py
├── requirements.txt
├── README.md
├── student_api/
│   ├── __init__.py
│   ├── settings.py      # Django settings with MongoDB config
│   ├── urls.py          # Main URL routing
│   ├── wsgi.py
│   └── asgi.py
└── students/
    ├── __init__.py
    ├── admin.py         # Admin panel configuration
    ├── apps.py
    ├── models.py        # Student model definition
    ├── serializers.py   # Data validation & serialization
    ├── views.py         # API view logic (ViewSet)
    ├── urls.py          # App-level URL routing
    └── tests.py
```

## 🔧 Configuration Details

### Database Configuration (settings.py)

This project uses a hybrid approach:
- **SQLite** for Django's internal tables (auth, sessions, admin)
- **MongoDB** (via PyMongo) for student data

```python
# Django's internal database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# MongoDB connection (used directly in views)
MONGODB_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
```

### REST Framework Settings

```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
}
```

## 🐛 Troubleshooting

### Codespace-Specific Issues

**Port Forwarding:**
- Codespace automatically forwards port 8000
- Click the "Ports" tab in VS Code to see the forwarded URL
- Use that URL instead of `localhost:8000` for external testing

**MongoDB Connection Issues in Codespace:**
- If MongoDB fails to start: `sudo systemctl restart mongod`
- Check MongoDB status: `sudo systemctl status mongod`
- View MongoDB logs: `sudo journalctl -u mongod`

### MongoDB Connection Issues

**Error:** `Connection refused`
- Ensure MongoDB is running: `sudo systemctl status mongod`
- Check if MongoDB is listening on port 27017: `netstat -tuln | grep 27017`
- For Codespace, try restarting: `sudo systemctl restart mongod`

**MongoDB Atlas Connection Issues:**
- Verify your connection string is correct
- Check if your IP is whitelisted (use 0.0.0.0/0 for testing)
- Ensure username/password are URL-encoded

### Python Package Issues

**Error:** Module import errors
- Make sure you're using Python 3.8+
- Reinstall requirements: `pip install -r requirements.txt`
- Try using a virtual environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

### Port Already in Use

**Error:** `Error: That port is already in use`
- Kill the existing process: `pkill -f runserver`
- Or use a different port: `python manage.py runserver 8001`

## 📖 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Djongo Documentation](https://www.djongomapper.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)

## 🤝 Contributing

Feel free to submit issues, create pull requests, or fork the repository to improve the project.

## 📄 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

Created as a demonstration of Django REST Framework with MongoDB integration.

## 🎉 Success!

Your Student Management API is now ready to use! Start making requests and managing student data through the RESTful endpoints.

For any questions or issues, please refer to the troubleshooting section or create an issue in the repository.