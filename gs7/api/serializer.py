from rest_framework import serializers
from .models import Student


class Student_Serializer(serializers.ModelSerializer):
    
    # name = serializers.CharField(read_only = True)
    class Meta:
        model = Student
        fields = ['id','name', 'roll', 'city']
        read_only_fields = ['name', 'city']
        
        # extra_kwargs = {'name':{'read_only': True}}

# modelserializer provide create update function inbuilt


