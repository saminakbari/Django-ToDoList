from rest_framework import serializers
from rest_framework.response import Response

from ToDoListApp.models import Task, ToDoList


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "deadline", "priority", "attachment"]

    def create(self, validated_data):
        user = self.context["user"]
        to_do_list = self.context["to_do_list"]
        if user != to_do_list.owner:
            raise Exception("You don't own this list.")
        validated_data["owner"] = user
        validated_data["to_do_lists"] = [
            to_do_list,
        ]
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if instance.owner != self.context["user"]:
            raise Exception("You don't own this task.")
        else:
            return super().update(instance, validated_data)


class TaskSerializerForList(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title"]


class ToDoListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializerForList(many=True, read_only=True)

    class Meta:
        model = ToDoList
        fields = ["id", "title", "tasks"]

    def create(self, validated_data):
        validated_data["owner"] = self.context["user"]
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if instance.owner != self.context["user"]:
            raise Exception("You don't own this task.")
        return super().update(instance, validated_data)
