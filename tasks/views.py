from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Привязываем задачу к текущему пользователю
            task.save()
            return redirect('tasks')
        else:
            error = "Форма заполнена некорректно"
    form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form, 'error': error})

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/create_task.html'
    form_class = TaskForm
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_url = '/tasks/'