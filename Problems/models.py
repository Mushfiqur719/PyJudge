from django.db import models
from Contestant.models import Contestant


class Problems(models.Model):
    input = models.FileField(upload_to='Documents/TestCase/Input')
    output = models.FileField(upload_to='Documents/TestCase/Output')

    problem_id = models.CharField(max_length=10, primary_key=True)
    problem_name = models.CharField(max_length=30)
    Problem_text = models.FileField(upload_to='Documents/Problem')
    category = models.CharField(max_length=20)
    level = models.CharField(max_length=10)
    solver = models.ForeignKey(Contestant, on_delete=models.SET_DEFAULT, default='Did not solve')


class Submissions(models.Model):
    solver_id = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    sub_id = models.CharField(max_length=10)
    status = models.CharField(max_length=15)
    time = models.DateTimeField(auto_now_add=True)
    code = models.FileField(upload_to='Documents/Solution')


class Discussion(models.Model):
    problem_id = models.ForeignKey(Problems, on_delete=models.SET_DEFAULT, default='Problem Removed')
    dicussant_id = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10)
    message = models.TextField()

