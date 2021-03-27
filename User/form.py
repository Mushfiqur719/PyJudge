from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User





class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	First_Name =forms.CharField(max_length=10)
	Last_Name = forms.CharField(max_length=10)
	Institution = forms.CharField(max_length=20)
	Country = forms.CharField(max_length=10)

	class Meta:
		model = User
		fields = ["username",
				  "email",
				  "First_Name",
				  "Last_Name",
				  "Institution",
				  "Country",
				  "password1",
				  "password2",
				  "Institution",
				  ]

