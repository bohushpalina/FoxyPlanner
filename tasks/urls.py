from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name = 'tasks'),
    path('create', views.create_task, name = 'create_task')
    # path('<int:pk>', views.EventDetailView.as_view(), name = 'event_detail'),
    # path('<int:pk>/update', views.EventUpdateView.as_view(), name = 'event_update'),
    # path('<int:pk>/delete', views.EventDeleteView.as_view(), name = 'event_delete')
]