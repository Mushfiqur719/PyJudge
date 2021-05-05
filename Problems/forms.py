from django import forms
from .models import Problems


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = '__all__'
