from django.db import models


class Judge(models.Model):
    judge_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
