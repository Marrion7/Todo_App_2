from django import forms
from .models import Task



class TaskEdit(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        
