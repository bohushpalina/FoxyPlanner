from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'is_completed']
        widgets = {
            'title': TextInput(attrs={'class': 'task-input', 'placeholder': 'Введите название задачи'}),
            'description': Textarea(attrs={'class': 'task-textarea', 'placeholder': 'Введите описание'}),
            'deadline': DateTimeInput(
                attrs={'class': 'task-input', 'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'  
            ),
        }
