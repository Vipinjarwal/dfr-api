from rest_framework import serializers
from .models import Student




class Student_Serializer(serializers.ModelSerializer):
    # Validators
    def start_with_r(value):
        if value[0].lower()!= 'r':
            raise serializers.ValidationError('Name should be start with R')
    
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        
    
    # field level validation
    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError('Seat Full')
    #     return value
        
    
    # Object Level Validation
    
    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
        
    #     if nm.lower() == 'sonali' and ct.lower()!='mumbai':
    #         raise serializers.ValidationError('City must be mumbai')
    #     return (data)
            
    
