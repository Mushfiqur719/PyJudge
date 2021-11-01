from django import forms
from .models import Problems, Submissions


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = '__all__'

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = '__all__'
