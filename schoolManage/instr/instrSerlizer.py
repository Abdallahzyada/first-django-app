from rest_framework import serializers
from .models import *

class InstrSerlizer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=10)
    
    def create(self, validated_data):
        print(validated_data)
        return Instructor.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name')
        instance.save()