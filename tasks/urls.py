from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name = 'tasks'),
    path('create', views.create_task, name = 'create_task'),
    path('<int:pk>/update_task', views.TaskUpdateView.as_view(), name = 'task_update')
    # path('<int:pk>/delete', views.EventDeleteView.as_view(), name = 'event_delete')
]