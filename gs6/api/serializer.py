from rest_framework import serializers
from .models import Student


class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name', 'roll', 'city']


# modelserializer provide create update function inbuilt