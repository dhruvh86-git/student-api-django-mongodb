# 🚀 Student API - Postman Testing Guide

## 📥 STEP 1: Open Postman

If you don't have Postman installed:
1. Go to https://www.postman.com/downloads/
2. Download and install, OR
3. Use Postman Web (https://web.postman.com/)

---

## 🌐 STEP 2: Get Your Codespace URL

Since you're in a GitHub Codespace, you need the **public URL**:

### Find Your URL:
1. Look at the **PORTS** tab in VS Code (bottom panel)
2. Find port **8000** 
3. Right-click → **Copy Local Address** or **Make Public** first if needed
4. Your URL will look like: `https://reimagined-space-fiesta-xxxx.app.github.dev`

**OR** you can use: `http://127.0.0.1:8000` if testing locally

---

## 📝 STEP 3: Create a New Collection

1. Open Postman
2. Click **Collections** (left sidebar)
3. Click **+ New Collection**
4. Name it: **Student Management API**

---

## 🎯 STEP 4: Set Up Requests (One by One)

### ✅ Request 1: CREATE Student (POST)

1. Click your collection → **Add Request**
2. Name: `Create Student`
3. Method: **POST**
4. URL: `http://127.0.0.1:8000/students/`
   
   *OR your Codespace URL:* `https://YOUR-CODESPACE-URL.app.github.dev/students/`

5. Click **Body** tab
6. Select **raw**
7. Select **JSON** (from dropdown)
8. Paste this JSON:

```json
{
  "name": "John Doe",
  "roll_no": 101,
  "course": "Computer Science",
  "marks": 85,
  "email": "john.doe@example.com"
}
```

9. Click **Send**

**Expected Response (201 Created):**
```json
{
  "message": "Student created successfully",
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "name": "John Doe",
    "roll_no": 101,
    "course": "Computer Science",
    "marks": 85,
    "email": "john.doe@example.com"
  }
}
```

---

### ✅ Request 2: GET All Students (GET)

1. Add new request to collection
2. Name: `Get All Students`
3. Method: **GET**
4. URL: `http://127.0.0.1:8000/students/`
5. Click **Send**

**Expected Response (200 OK):**
```json
{
  "message": "Students retrieved successfully",
  "count": 1,
  "data": [
    {
      "id": "507f1f77bcf86cd799439011",
      "name": "John Doe",
      "roll_no": 101,
      "course": "Computer Science",
      "marks": 85,
      "email": "john.doe@example.com"
    }
  ]
}
```

---

### ✅ Request 3: GET Specific Student (GET)

1. Add new request
2. Name: `Get Student by Roll Number`
3. Method: **GET**
4. URL: `http://127.0.0.1:8000/students/101/`
   *(Note: 101 is the roll_no)*
5. Click **Send**

**Expected Response (200 OK):**
```json
{
  "message": "Student retrieved successfully",
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "name": "John Doe",
    "roll_no": 101,
    "course": "Computer Science",
    "marks": 85,
    "email": "john.doe@example.com"
  }
}
```

---

### ✅ Request 4: UPDATE Student (PATCH)

1. Add new request
2. Name: `Update Student Marks`
3. Method: **PATCH**
4. URL: `http://127.0.0.1:8000/students/101/`
5. Click **Body** → **raw** → **JSON**
6. Paste:

```json
{
  "marks": 95
}
```

7. Click **Send**

**Expected Response (200 OK):**
```json
{
  "message": "Student updated successfully",
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "name": "John Doe",
    "roll_no": 101,
    "course": "Computer Science",
    "marks": 95,
    "email": "john.doe@example.com"
  }
}
```

---

### ✅ Request 5: UPDATE Full Student (PUT)

1. Add new request
2. Name: `Full Update Student`
3. Method: **PUT**
4. URL: `http://127.0.0.1:8000/students/101/`
5. Click **Body** → **raw** → **JSON**
6. Paste (ALL fields required):

```json
{
  "name": "John Doe Updated",
  "roll_no": 101,
  "course": "Computer Science",
  "marks": 90,
  "email": "john.doe@example.com"
}
```

7. Click **Send**

---

### ✅ Request 6: DELETE Student (DELETE)

1. Add new request
2. Name: `Delete Student`
3. Method: **DELETE**
4. URL: `http://127.0.0.1:8000/students/102/`
5. Click **Send**

**Expected Response (200 OK):**
```json
{
  "message": "Student deleted successfully",
  "roll_no": 102
}
```

---

### ❌ Request 7: Error Test - Non-existent Student

1. Add new request
2. Name: `Error Test - Not Found`
3. Method: **GET**
4. URL: `http://127.0.0.1:8000/students/999/`
5. Click **Send**

**Expected Response (404 Not Found):**
```json
{
  "error": "Student not found",
  "details": "Student with roll number 999 does not exist"
}
```

---

### ❌ Request 8: Error Test - Duplicate Roll Number

1. First, create a student (roll_no: 101)
2. Add new request
3. Name: `Error Test - Duplicate`
4. Method: **POST**
5. URL: `http://127.0.0.1:8000/students/`
6. Body:

```json
{
  "name": "Test User",
  "roll_no": 101,
  "course": "Testing",
  "marks": 80,
  "email": "test@example.com"
}
```

7. Click **Send**

**Expected Response (400 Bad Request):**
```json
{
  "error": "Failed to create student",
  "details": "Student with this roll number already exists"
}
```

---

### ❌ Request 9: Error Test - Invalid Marks

1. Add new request
2. Name: `Error Test - Invalid Marks`
3. Method: **POST**
4. URL: `http://127.0.0.1:8000/students/`
5. Body:

```json
{
  "name": "Invalid Student",
  "roll_no": 105,
  "course": "Testing",
  "marks": 150,
  "email": "invalid@example.com"
}
```

**Expected Response (400 Bad Request):**
```json
{
  "error": "Failed to create student",
  "details": "Marks must be between 0 and 100."
}
```

---

## 🎨 STEP 5: Organize Your Collection

Your Postman collection should look like this:

```
📁 Student Management API
  ├── 📄 Create Student (POST)
  ├── 📄 Get All Students (GET)
  ├── 📄 Get Student by Roll Number (GET)
  ├── 📄 Update Student Marks (PATCH)
  ├── 📄 Full Update Student (PUT)
  ├── 📄 Delete Student (DELETE)
  ├── 📄 Error Test - Not Found (GET)
  ├── 📄 Error Test - Duplicate (POST)
  └── 📄 Error Test - Invalid Marks (POST)
```

---

## 🎬 DEMO SEQUENCE FOR INTERVIEW

Run requests in this order:

1. **Clear old data** (optional - in terminal):
   ```bash
   mongosh student_db --eval "db.students.deleteMany({})"
   ```

2. **Create Student 1** (John Doe, roll_no: 101)
   → Show 201 Created response

3. **Create Student 2** (Jane Smith, roll_no: 102)
   → Show another successful creation

4. **Get All Students**
   → Show count: 2 and both students

5. **Get Specific Student** (101)
   → Show single student retrieval

6. **Update Student** (change marks to 95)
   → Show updated data

7. **Delete Student** (102)
   → Show deletion confirmation

8. **Get All Students** again
   → Show count: 1 (only John remains)

9. **Error Tests**:
   - Try to get roll_no 999 → Show 404
   - Try to create duplicate roll_no → Show 400
   - Try invalid marks → Show validation error

---

## 💡 POSTMAN TIPS FOR INTERVIEW

### 1. Use Environment Variables (Advanced)

Create an environment:
1. Click **Environments** (left sidebar)
2. Create new environment: **Student API Local**
3. Add variable:
   - Variable: `base_url`
   - Initial Value: `http://127.0.0.1:8000`
   - Current Value: `http://127.0.0.1:8000`

4. In your requests, use: `{{base_url}}/students/`

This way you can switch between local and production easily!

---

### 2. Save Example Responses

After each successful request:
1. Click **Save Response**
2. Click **Save as Example**

This helps you show expected outputs without running the API!

---

### 3. Add Tests (Automated Validation)

In any request, click **Tests** tab and add:

```javascript
// For Create Student
pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Response has message", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.message).to.eql("Student created successfully");
});

// For Get All Students
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response has data array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.data).to.be.an('array');
});
```

---

### 4. Use Collection Runner

1. Click your collection → **Run**
2. Select all requests
3. Click **Run Student Management API**
4. Watch all tests run automatically!

Perfect for showing comprehensive testing in interviews!

---

## 📸 SCREENSHOT SUGGESTIONS

Take screenshots of:
1. ✅ Successful POST with 201 status
2. ✅ GET all showing multiple students
3. ✅ PATCH showing updated marks
4. ❌ 404 error with clear message
5. ❌ 400 validation error
6. ✅ Collection runner with all tests passing

---

## 🎤 WHAT TO SAY DURING DEMO

**Starting:**
> "I've created a Postman collection to test all API endpoints. Let me walk you through the CRUD operations."

**During POST:**
> "I'm creating a new student with POST request. Notice the 201 Created status and the returned data includes the MongoDB ObjectId."

**During GET:**
> "Here I'm retrieving all students. The response includes a count and data array. I can also get a specific student by roll number."

**During PATCH:**
> "For updates, I'm using PATCH which allows partial updates - I only need to send the fields I want to change."

**During DELETE:**
> "The delete operation returns a confirmation with the roll number that was deleted."

**During Errors:**
> "The API has robust error handling. See how it returns proper HTTP status codes - 404 for not found, 400 for validation errors - with clear, helpful error messages."

---

## 🚀 QUICK START (Interview Day)

**5 Minutes Before Demo:**

1. Open Postman
2. Check server is running:
   ```bash
   pgrep -f runserver || python manage.py runserver
   ```
3. Clear test data:
   ```bash
   mongosh student_db --eval "db.students.deleteMany({})"
   ```
4. Test one request to ensure API is responding
5. You're ready! 🎉

---

## 🎯 BONUS: Import/Export Collection

### Export Your Collection:
1. Right-click collection → **Export**
2. Choose **Collection v2.1**
3. Save the JSON file
4. Share with interviewers if needed!

### Import Pre-made Collection:
If you want to save time, I can create a JSON file for you to import directly into Postman!

---

## 🆘 TROUBLESHOOTING

### Issue: "Could not get any response"
**Fix:** 
- Check if server is running: `pgrep -f runserver`
- Check if MongoDB is running: `pgrep -x mongod`
- Try: `http://127.0.0.1:8000` instead of `localhost`

### Issue: "Certificate Error" in Codespace
**Fix:**
- Disable SSL verification: Postman Settings → General → **SSL certificate verification OFF**
- OR use the HTTP version of your Codespace URL

### Issue: "404 Not Found"
**Fix:**
- Make sure URL ends with `/` → `/students/` not `/students`
- Check you're using correct port (8000)

---

## 📚 ADDITIONAL RESOURCES

**Postman Learning:**
- https://learning.postman.com/

**API Testing Best Practices:**
- Use descriptive request names
- Organize in folders (CRUD, Error Tests)
- Save example responses
- Add tests for automation
- Use environment variables

---

**You're all set for Postman! Practice the flow 2-3 times and you'll be perfect! 🚀**
