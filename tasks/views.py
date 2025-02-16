from django.shortcuts import render
from .models import Task

def tasks(request):
    tasks = Task.objects.order_by("is_completed")  # Получаем все задачи из базы данных
    return render(request, 'tasks/tasks.html', {'tasks': tasks})
