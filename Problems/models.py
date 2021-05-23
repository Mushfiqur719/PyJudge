from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.urls import reverse
from ckeditor.fields import RichTextField
=======
from django.urls import reverse 
>>>>>>> b8c18d301da0bf66dc8a40a11809e789f62d6b2e

CATEGORY = (
    ('Basic Python', 'Basic Python'),
    ('Conditionals', 'Conditionals'),
    ('Loops & Array', 'Loops & Array'),
    ('Function', 'Function'),
    ('Class & Objects', 'Class & Objects'),
    ('File Handling', 'File Handling'),
)

LEVEL = (
    ('Easy','Easy'),
    ('Medium','Medium'),
    ('Hard','Hard'),
)

class Problems(models.Model):
    setter = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    problem_id = models.CharField(max_length=100, unique=True)
    problem_name = models.CharField(max_length=100, unique=True)
<<<<<<< HEAD
    # Problem_text = models.TextField()
    Problem_text = RichTextField(blank=True,null=True)
    
    
    
=======
    Problem_text = models.TextField()
    
    
>>>>>>> b8c18d301da0bf66dc8a40a11809e789f62d6b2e
    sample_input = models.CharField(max_length=255, null=True)
    sample_output = models.CharField(max_length=255, null=True)

    input = models.FileField(upload_to='Documents/TestCase/Input', null=True)
    output = models.FileField(upload_to='Documents/TestCase/Output', null=True)
    
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    level = models.CharField(max_length=20, choices=LEVEL, null=True)

    def __str__(self):
        return f'{self.problem_id}-{self.problem_name}'

    # def get_absolute_url(self):
    #     return reverse('solve-section', args=(str(self.id)))
