from django.shortcuts import render
from .models import Note

def notes(request):
    notes = Note.objects.order_by('created_at')
    return render(request, 'notes/notes.html', {'notes': notes})
