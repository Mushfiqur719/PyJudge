from django.db import models
from Contestant.models import Contestant


class Problems(models.Model):
    input = models.FileField(upload_to='Documents/TestCase/Input')
    output = models.FileField(upload_to='Documents/TestCase/Output')

    problem_id = models.CharField(max_length=20, unique=True)
    problem_name = models.CharField(max_length=30, unique=True)
    Problem_text = models.FileField(upload_to='Documents/Problem')
    category = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    solver = models.ForeignKey(Contestant, on_delete=models.SET_DEFAULT, default='Did not solve')


class Submissions(models.Model):
    solver_id = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    status = models.CharField(max_length=15)
    time = models.DateTimeField(auto_now_add=True)
    code = models.FileField(upload_to='Documents/Solution')


class Discussion(models.Model):
    problem_id = models.ForeignKey(Problems, on_delete=models.CASCADE, default='Problem Removed')
    dicussant = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20)
    message = models.TextField()

