from django.db import models
from Judge.models import Judge
from Contestant.models import Contestant


class Contest(models.Model):
    teacher = models.OneToOneField(Judge, on_delete=models.CASCADE)
    contest_name = models.CharField(max_length=30, unique=True)
    participant = models.ManyToManyField(Contestant)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contest_name


class Tutorials(models.Model):
    creator = models.ForeignKey(Judge, on_delete=models.CASCADE)
    contest_name = models.OneToOneField(Contest, on_delete=models.CASCADE)
    tutorial_title = models.CharField(max_length=50)
    tutorial_text = models.FileField(upload_to='Documents/Tutorials')


