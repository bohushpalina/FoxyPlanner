from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.views.generic import DetailView, UpdateView, DeleteView

def tasks(request):
    tasks = Task.objects.order_by("is_completed")  # Получаем все задачи из базы данных
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = "Форма заполнена некорректно"
    form = TaskForm()
    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'tasks/create_task.html', data)