from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'description', 'published_date']
        widgets = {
            'title': TextInput(attrs={'class': 'event-input', 'placeholder': 'Введите название события'}),
            'description': Textarea(attrs={'class': 'event-textarea', 'placeholder': 'Введите описание'}),
            'published_date': DateTimeInput(attrs={'class': 'event-input', 'type': 'datetime-local'}),
        }