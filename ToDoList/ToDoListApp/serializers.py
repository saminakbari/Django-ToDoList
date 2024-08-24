from django.contrib.auth.models import User
from rest_framework import serializers

from ToDoListApp.models import Task, ToDoList


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "deadline", "priority", "attachment"]


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ["id", "title", "tasks"]
        tasks = serializers.ReadOnlyField(source="tasks")
        id = serializers.ReadOnlyField(source="id")


class UserSerializer:
    class Meta:
        model = User
        fields = ["username"]
