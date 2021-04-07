from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Input-Output', 'Input-Output'),
    ('String', 'String'),
    ('Math', 'Math'),
    ('Set', 'Set'),
)

LEVEL = (
    ('Easy','Easy'),
    ('Medium','Medium'),
    ('Hard','Hard'),
)

class Problems(models.Model):
    setter = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    problem_id = models.CharField(max_length=20, unique=True)
    problem_name = models.CharField(max_length=30, unique=True)
    Problem_text = models.FileField(upload_to='Documents/Problem')
    
    input = models.FileField(upload_to='Documents/TestCase/Input', null=True)
    output = models.FileField(upload_to='Documents/TestCase/Output')
    
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    level = models.CharField(max_length=20, choices=LEVEL, null=True)

    def __str__(self):
        return f'{self.problem_id}-{self.problem_name}'
