from django.db import models


class Problems(models.Model):
    class Meta:
        test_cases = (('input', 'output'),)

    input = models.FileField(upload_to='')
    output = models.FileField(upload_to='')

    problem_id = models.IntegerField(primary_key=True)
    problem_name = models.TextField()
    Problem_text = models.FileField(upload_to='')
    category = models.CharField(max_length=10)
    level = models.CharField(max_length=10)


class Submissions(models.Model):
    sub_id = models.CharField()
    status = models.CharField()
    time = models.DateTimeField()
    code = models.FileField(upload_to='')

class Discussion(models.Model):
    dicuss_id = models.CharField()
    user_type = models.CharField()
    message = models.TextField()

