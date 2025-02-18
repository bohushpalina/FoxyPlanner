from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name = 'tasks'),
    path('create', views.create_task, name = 'create_task'),
    path('<int:pk>/update_task', views.TaskUpdateView.as_view(), name = 'task_update'),
    path('<int:pk>/delete_task', views.TaskDeleteView.as_view(), name = 'task_delete')
]