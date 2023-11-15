from django.forms import ModelForm, DateTimeInput

from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'due_date': DateTimeInput(attrs={'type': 'date'}, format=('%Y-%m-%d')),
        }