from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)
    country = forms.CharField(max_length=10)
    institution = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'country',
            'institution',
            'password1',
            'password2',
        ]
