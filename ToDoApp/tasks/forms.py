# tasks/forms.py
from django import forms
from .models import Task

# tasks/forms.py

# tasks/forms.py
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'day', 'category']

    # Add this method to customize the day field widget
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['day'].widget.attrs.update({'class': 'form-control'})
