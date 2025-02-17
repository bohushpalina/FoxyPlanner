from .models import Note
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(attrs={'class': 'event-input', 'placeholder': 'Введите название события'}),
            'description': Textarea(attrs={'class': 'event-textarea', 'placeholder': 'Введите описание'})
        }