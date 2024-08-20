from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from rest_framework import generics

from ToDoListApp.serializers import UserSerializer


class ShareTask4(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

