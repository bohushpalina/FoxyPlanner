from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

@login_required
def notes(request):
    notes = Note.objects.filter(user=request.user)
    notes = Note.objects.order_by('created_at')
    return render(request, 'notes/notes.html', {'notes': notes})

def create_note(request):
    notes = Note.objects.filter(user=request.user)
    error = ''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
        else:
            error = "Форма заполнена некорректно"
    form = NoteForm()
    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'notes/create_note.html', data)

class EditNote(UpdateView):
    model = Note
    template_name = 'notes/create_note.html'
    form_class = NoteForm
    
class DeleteNote(DeleteView):
    model = Note
    success_url = '/notes/'
    template_name = 'notes/delete_note.html'