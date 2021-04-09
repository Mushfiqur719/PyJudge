from django import forms
from .models import Problems


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = [
            'setter', 'problem_id', 'problem_name','Problem_text','input','output','category','level',
        ]
