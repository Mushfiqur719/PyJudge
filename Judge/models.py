from django.db import models
from django.contrib.auth.models import User


class Judge(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.TextField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    privilege = models.CharField(max_length=10)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
