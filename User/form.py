from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=10)

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

class UserDetailsForm(forms.Form):
    fname = forms.CharField(label='First Name',max_length=15)
    lname = forms.CharField(label='First Name',max_length=15)
    about = forms.CharField(label='About')