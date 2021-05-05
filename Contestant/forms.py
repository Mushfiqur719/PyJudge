from django.contrib.auth.forms import forms
from .models import Contestant

class ContestantInfoForm(forms.ModelForm):
    class Meta:
        model = Contestant
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
        ]