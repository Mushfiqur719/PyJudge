from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     about = models.CharField(max_length=200)
#     profile_picture = models.ImageField(default='Document/Pro_pics/default-profile.jpg',upload_to='Document/Pro_pics')