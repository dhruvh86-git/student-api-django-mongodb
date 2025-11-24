# 🌐 Using Your Codespace URL - Quick Guide

## ✅ **YOUR API IS WORKING!**

Your Codespace URL is:
```
https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev
```

---

## 🎯 **CORRECT URLS TO USE**

### **1. Welcome Page (Root)**
```
https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev/
```
**What you'll see:** API documentation with available endpoints

---

### **2. Get All Students**
```
https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev/students/
```
**Method:** GET  
**What you'll see:** List of all students

---

### **3. Get Specific Student**
```
https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev/students/101/
```
**Method:** GET  
**What you'll see:** Details of student with roll_no 101

---

### **4. Create Student**
```
https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev/students/
```
**Method:** POST  
**Body (JSON):**
```json
{
  "name": "John Doe",
  "roll_no": 101,
  "course": "Computer Science",
  "marks": 85,
  "email": "john@example.com"
}
```

---

### **5. Update Student**
```
https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev/students/101/
```
**Method:** PATCH or PUT  
**Body (JSON):**
```json
{
  "marks": 95
}
```

---

### **6. Delete Student**
```
https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev/students/101/
```
**Method:** DELETE

---

## 🚀 **FOR POSTMAN**

When setting up Postman:

1. **Import the collection** (`Student_API_Postman_Collection.json`)

2. **Replace all URLs** from:
   ```
   http://127.0.0.1:8000/students/
   ```
   
   To:
   ```
   https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev/students/
   ```

3. **Or use Environment Variables:**
   - Create environment: "Student API Codespace"
   - Variable: `base_url`
   - Value: `https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev`
   - Use in requests: `{{base_url}}/students/`

---

## 💡 **TIP: Test in Browser First**

Before using Postman, test these URLs in your browser:

1. **Welcome page:**
   ```
   https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev/
   ```
   Should show API info

2. **Get all students:**
   ```
   https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev/students/
   ```
   Should show student list

---

## ❌ **COMMON MISTAKES**

### ❌ WRONG:
```
https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev
```
**Problem:** No `/students/` at the end → 404 or welcome page

### ✅ CORRECT:
```
https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev/students/
```
**Result:** API works!

---

## 🔒 **IF YOU GET CERTIFICATE ERRORS IN POSTMAN**

1. Go to Postman **Settings**
2. **General** tab
3. Turn **OFF**: "SSL certificate verification"
4. Try again

---

## 🎬 **QUICK DEMO TEST**

**In your browser, visit:**
```
https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev/students/
```

**You should see:**
```json
{
  "message": "Students retrieved successfully",
  "count": 2,
  "data": [...]
}
```

**If you see this, your API is working perfectly! 🎉**

---

## 📱 **SHARE WITH INTERVIEWER**

You can share this URL directly:
```
https://improved-umbrella-g4rpxjr9q4xxcr9j-8000.app.github.dev/students/
```

Anyone can access it while your Codespace is running!

---

## 🆘 **IF IT STOPS WORKING**

Check if server is still running:
```bash
pgrep -f runserver
```

If not running, restart:
```bash
python manage.py runserver
```

---

**You're all set! The API is live and accessible via your Codespace URL! 🚀**
