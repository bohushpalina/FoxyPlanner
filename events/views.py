from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm
from django import DetailView

def events_home(request):
    events = Articles.objects.order_by('published_date')
    return render(request, 'events/events_home.html', {'events': events})

class EventDetailView(DetailView):
    model = Articles
    template_name = 'events/detail_view.html'
    context_object_name = 'event'

def create_event(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_home')
        else:
            error = "Форма заполнена некорректно"
    form = ArticleForm()
    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'events/create_event.html', data)
