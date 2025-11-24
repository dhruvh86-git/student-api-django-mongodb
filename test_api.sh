#!/bin/bash

# Test script for Student API

BASE_URL="http://127.0.0.1:8000/students"

echo "========================================="
echo "Testing Student Management API"
echo "========================================="
echo

echo "1. Creating Student 1 (John Doe)..."
curl -X POST $BASE_URL/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "roll_no": 101, "course": "Computer Science", "marks": 85, "email": "john.doe@example.com"}'
echo -e "\n"

echo "2. Creating Student 2 (Jane Smith)..."
curl -X POST $BASE_URL/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Smith", "roll_no": 102, "course": "Data Science", "marks": 92, "email": "jane.smith@example.com"}'
echo -e "\n"

echo "3. Getting all students..."
curl -X GET $BASE_URL/
echo -e "\n"

echo "4. Getting student by roll number (101)..."
curl -X GET $BASE_URL/101/
echo -e "\n"

echo "5. Updating student marks (101)..."
curl -X PATCH $BASE_URL/101/ \
  -H "Content-Type: application/json" \
  -d '{"marks": 95}'
echo -e "\n"

echo "6. Getting updated student..."
curl -X GET $BASE_URL/101/
echo -e "\n"

echo "7. Testing error handling (non-existent student)..."
curl -X GET $BASE_URL/999/
echo -e "\n"

echo "8. Deleting student (102)..."
curl -X DELETE $BASE_URL/102/
echo -e "\n"

echo "9. Verifying deletion..."
curl -X GET $BASE_URL/
echo -e "\n"

echo "========================================="
echo "Tests completed!"
echo "========================================="
