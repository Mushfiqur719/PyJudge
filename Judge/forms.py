from django.contrib.auth.forms import forms
from .models import Judge

class ContestantInfoForm(forms.ModelForm):
    class Meta:
        model = Judge
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
        ]