from django.db import models
from django.contrib.auth.models import User

from Problems.models import Problems
from django.utils import timezone


class Contest(models.Model):
    setter = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #Judge will replace User
    contest_name = models.CharField(max_length=30, unique=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    problems = models.ManyToManyField(Problems)

    def __str__(self):
        return self.contest_name


class Tutorials(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)#Judge will replace User
    contest_name = models.OneToOneField(Contest, on_delete=models.CASCADE, null= True)
    tutorial_title = models.CharField(max_length=50)
    tutorial_text = models.FileField(upload_to='Documents/Tutorials')

    def __str__(self):
        return self.tutorial_title

