from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from pymongo import MongoClient
from bson import ObjectId
import os
from .serializers import StudentSerializer


# MongoDB Connection
MONGODB_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGODB_URI)
db = client['student_db']
students_collection = db['students']

# Create unique indexes
students_collection.create_index('roll_no', unique=True)
students_collection.create_index('email', unique=True)


class StudentViewSet(viewsets.ViewSet):
    """
    ViewSet for Student model providing CRUD operations using PyMongo directly.
    
    Endpoints:
    - POST /students/ - Create a new student
    - GET /students/ - List all students
    - GET /students/{roll_no}/ - Retrieve a specific student by roll number
    - PUT /students/{roll_no}/ - Update a student's details
    - PATCH /students/{roll_no}/ - Partially update a student's details
    - DELETE /students/{roll_no}/ - Delete a student
    """
    
    lookup_field = 'roll_no'
    
    def create(self, request, *args, **kwargs):
        """
        Create a new student with validation.
        """
        serializer = StudentSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            
            # Check if roll_no already exists
            if students_collection.find_one({'roll_no': serializer.validated_data['roll_no']}):
                return Response(
                    {
                        'error': 'Failed to create student',
                        'details': 'Student with this roll number already exists'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Check if email already exists
            if students_collection.find_one({'email': serializer.validated_data['email']}):
                return Response(
                    {
                        'error': 'Failed to create student',
                        'details': 'Student with this email already exists'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Insert into MongoDB
            result = students_collection.insert_one(serializer.validated_data)
            
            # Get the created student
            student = students_collection.find_one({'_id': result.inserted_id})
            student['id'] = str(student.pop('_id'))
            
            return Response(
                {
                    'message': 'Student created successfully',
                    'data': student
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {
                    'error': 'Failed to create student',
                    'details': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def list(self, request, *args, **kwargs):
        """
        List all students.
        """
        students = list(students_collection.find())
        # Convert ObjectId to string
        for student in students:
            student['id'] = str(student.pop('_id'))
        
        return Response(
            {
                'message': 'Students retrieved successfully',
                'count': len(students),
                'data': students
            },
            status=status.HTTP_200_OK
        )
    
    def retrieve(self, request, roll_no=None, *args, **kwargs):
        """
        Retrieve a specific student by roll number.
        """
        try:
            roll_no_int = int(roll_no)
            student = students_collection.find_one({'roll_no': roll_no_int})
            
            if not student:
                return Response(
                    {
                        'error': 'Student not found',
                        'details': f'Student with roll number {roll_no} does not exist'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            student['id'] = str(student.pop('_id'))
            
            return Response(
                {
                    'message': 'Student retrieved successfully',
                    'data': student
                },
                status=status.HTTP_200_OK
            )
        except ValueError:
            return Response(
                {
                    'error': 'Invalid roll number',
                    'details': 'Roll number must be an integer'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def update(self, request, roll_no=None, *args, **kwargs):
        """
        Update a student's details (full update).
        """
        try:
            roll_no_int = int(roll_no)
            student = students_collection.find_one({'roll_no': roll_no_int})
            
            if not student:
                return Response(
                    {
                        'error': 'Student not found',
                        'details': f'Student with roll number {roll_no} does not exist'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = StudentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            # Update in MongoDB
            students_collection.update_one(
                {'roll_no': roll_no_int},
                {'$set': serializer.validated_data}
            )
            
            # Get updated student
            updated_student = students_collection.find_one({'roll_no': roll_no_int})
            updated_student['id'] = str(updated_student.pop('_id'))
            
            return Response(
                {
                    'message': 'Student updated successfully',
                    'data': updated_student
                },
                status=status.HTTP_200_OK
            )
        except ValueError:
            return Response(
                {
                    'error': 'Invalid roll number',
                    'details': 'Roll number must be an integer'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    'error': 'Failed to update student',
                    'details': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def partial_update(self, request, roll_no=None, *args, **kwargs):
        """
        Partially update a student's details.
        """
        try:
            roll_no_int = int(roll_no)
            student = students_collection.find_one({'roll_no': roll_no_int})
            
            if not student:
                return Response(
                    {
                        'error': 'Student not found',
                        'details': f'Student with roll number {roll_no} does not exist'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # For partial update, we don't need all fields
            serializer = StudentSerializer(data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            
            # Update only provided fields
            students_collection.update_one(
                {'roll_no': roll_no_int},
                {'$set': serializer.validated_data}
            )
            
            # Get updated student
            updated_student = students_collection.find_one({'roll_no': roll_no_int})
            updated_student['id'] = str(updated_student.pop('_id'))
            
            return Response(
                {
                    'message': 'Student updated successfully',
                    'data': updated_student
                },
                status=status.HTTP_200_OK
            )
        except ValueError:
            return Response(
                {
                    'error': 'Invalid roll number',
                    'details': 'Roll number must be an integer'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    'error': 'Failed to update student',
                    'details': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def destroy(self, request, roll_no=None, *args, **kwargs):
        """
        Delete a student by roll number.
        """
        try:
            roll_no_int = int(roll_no)
            student = students_collection.find_one({'roll_no': roll_no_int})
            
            if not student:
                return Response(
                    {
                        'error': 'Student not found',
                        'details': f'Student with roll number {roll_no} does not exist'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # Delete from MongoDB
            students_collection.delete_one({'roll_no': roll_no_int})
            
            return Response(
                {
                    'message': 'Student deleted successfully',
                    'roll_no': roll_no_int
                },
                status=status.HTTP_200_OK
            )
        except ValueError:
            return Response(
                {
                    'error': 'Invalid roll number',
                    'details': 'Roll number must be an integer'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
