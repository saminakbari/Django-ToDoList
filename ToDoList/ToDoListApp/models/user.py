from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=50, primary_key=True, unique=True)
    password = models.CharField(max_length=50)
