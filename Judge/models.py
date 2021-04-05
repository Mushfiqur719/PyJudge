from django.db import models
from django.contrib.auth.models import User


class Judge(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "Judge"
