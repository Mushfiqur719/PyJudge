from django.db import models


class Contest(models.Model):
    contest_id = models.CharField()
    participant = models.CharField()
    approval = models.BinaryField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Tutorials(models.Model):
    tutorial_id = models.CharField()
    tutorial_title = models.CharField()
    tutorial_text = models.TextField()


