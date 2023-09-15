from rest_framework import serializers
from .models import Student


# Validators
def start_with_r(value):
    if value[0].lower()!= 'r':
        raise serializers.ValidationError('Name should be start with R')

class Student_Serializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators = [start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.name)
        instance.city = validated_data.get('city', instance.name)
        instance.save()
        return instance
    
    
    # field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
        
    
    # Object Level Validation
    
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        
        if nm.lower() == 'vipin' and ct.lower()!='ratlam':
            raise serializers.ValidationError('City must be Ratlam')
        return (data)
            
    
    #  