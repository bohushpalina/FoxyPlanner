from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, DeleteView

@login_required
def events_home(request):
    events = Articles.objects.filter(user=request.user)
    return render(request, 'events/events_home.html', {'events': events})

class EventDetailView(DetailView):
    model = Articles
    template_name = 'events/detail_view.html'
    context_object_name = 'event'
    
class EventUpdateView(UpdateView):
    model = Articles
    template_name = 'events/create_event.html'
    form_class = ArticleForm
    
class EventDeleteView(DeleteView):
    model = Articles
    success_url = '/events/'
    template_name = 'events/delete_event.html'

def create_event(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)  # Не сохраняем сразу
            event.user = request.user  # Присваиваем пользователя
            event.save()
            return redirect('events_home')
        else:
            error = "Форма заполнена некорректно"
    form = ArticleForm()
    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'events/create_event.html', data)
