from django.contrib.auth.models import User
from rest_framework import serializers

from ToDoListApp.models import Task, ToDoList


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority', 'attachment']


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['title', 'tasks']


class UserSerializer:
    class Meta:
        model = User
        fields = ['username']
