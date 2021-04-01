from django.db import models
from Judge.models import Judge
from Contestant.models import Contestant


class Contest(models.Model):
    # teacher_id = models.OneToOneField(Judge, on_delete=models.SET_DEFAULT, default='Teacher Left')
    contest_id = models.CharField(max_length=10, primary_key=True)
    participant_name = models.CharField(max_length=20)
    # participant_id = models.OneToOneField(Contestant, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)


class Tutorials(models.Model):
    # creator_id = models.ForeignKey(Judge, on_delete=models.SET_DEFAULT, default='Not by Teacher')
    tutorial_id = models.CharField(max_length=10)
    tutorial_title = models.CharField(max_length=50)
    tutorial_text = models.FileField(upload_to='Documents/Tutorials')


