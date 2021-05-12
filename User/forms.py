from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]

class ProfileUpdateForm(forms.ModelForm):
    TYPE = [
        ('Contestant','Contestant'),
        ('Judge','Judge'),
    ]
    image = forms.ImageField(required=False)
    user_type = forms.CharField(widget=forms.Select(choices=TYPE))
    class Meta:
        model = Profile
        fields = [
            'institution',
            'image',
            'user_type',
        ]