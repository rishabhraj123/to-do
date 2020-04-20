from django import forms
from .models import Task,Taskheading

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title','complete']


class TaskHeadForm(forms.ModelForm):
    
    class Meta:
        model = Taskheading
        fields = ['heading']