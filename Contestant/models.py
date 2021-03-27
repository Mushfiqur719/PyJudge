from django.db import models


class Contestant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
