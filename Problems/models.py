from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

CATEGORY = (
    ('Basic Python', 'Basic Python'),
    ('Conditionals', 'Conditionals'),
    ('Loops & Array', 'Loops & Array'),
    ('Function', 'Function'),
    ('Class & Objects', 'Class & Objects'),
    ('File Handling', 'File Handling'),
)

LEVEL = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
)


class Problems(models.Model):
    setter = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    problem_id = models.CharField(max_length=100, unique=True)
    problem_name = models.CharField(max_length=100, unique=True)
    Problem_text = RichTextField(blank=True, null=True)
    sample_input = models.CharField(max_length=255, null=True)
    sample_output = models.CharField(max_length=255, null=True)
    input = models.FileField(upload_to='Documents/TestCase/Input', null=True)
    output = models.FileField(upload_to='Documents/TestCase/Output', null=True)
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    level = models.CharField(max_length=20, choices=LEVEL, null=True)

    def __str__(self):
        return f'{self.problem_id}-{self.problem_name}'


class Submissions(models.Model):
    user = models.CharField(max_length=100, unique=True)
    problem_id = models.CharField(max_length=100)
    problem_name = models.CharField(max_length=100)
    submission_time = models.CharField(max_length=100, unique=True)
    verdict = models.CharField(max_length=50)
    run_time = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.problem_name}-{self.user}'
