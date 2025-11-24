from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    """
    Serializer for Student data with validation.
    """
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=200, required=True)
    roll_no = serializers.IntegerField(required=True)
    course = serializers.CharField(max_length=100, required=True)
    marks = serializers.IntegerField(required=True)
    email = serializers.EmailField(required=True)
    
    def validate_roll_no(self, value):
        """
        Validate that roll_no is positive.
        """
        if value <= 0:
            raise serializers.ValidationError("Roll number must be a positive integer.")
        return value
    
    def validate_marks(self, value):
        """
        Validate that marks are within valid range (0-100).
        """
        if value < 0 or value > 100:
            raise serializers.ValidationError("Marks must be between 0 and 100.")
        return value
    
    def validate_email(self, value):
        """
        Validate email format and uniqueness.
        """
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value.lower()
    
    def validate_name(self, value):
        """
        Validate that name is not empty.
        """
        if not value or not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value.strip()
