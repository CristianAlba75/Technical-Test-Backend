from rest_framework import serializers
from .models import Task


# Serializer of task model
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'owner']
