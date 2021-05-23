from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    TYPE = [
        ('Contestant','Contestant'),
        ('Judge','Judge'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
    first_name = models.CharField(max_length=50, null= True)
    last_name = models.CharField(max_length=50, null= True)
    institution = models.CharField(max_length=200,null= True)
    email = models.CharField(max_length=50,null=True)
    image = models.ImageField(default='default-profile.png', upload_to='Profile_Pictures', null=True)
    user_type = models.CharField(max_length=20, choices=TYPE, null=True)

    def __str__(self):
        return f'{self.user.username}-Profile'