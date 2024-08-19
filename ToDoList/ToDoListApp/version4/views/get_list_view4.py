from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics

from ToDoListApp.serializers import ToDoListSerializer


class GetList4(LoginRequiredMixin, generics.RetrieveAPIView):
    serializer_class = ToDoListSerializer

