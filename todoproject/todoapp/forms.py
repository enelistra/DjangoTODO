from django import forms
from .models import todoform

class UpdateForm(forms.ModelForm):
    class Meta:
        model = todoform
        fields = ['taskname', 'priority', 'date']
