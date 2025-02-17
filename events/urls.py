from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_home, name='events_home'),
    path('create', views.create_event, name = 'create_event'),
    path('<int:pk>', views.EventDetailView.as_view(), name = 'event_detail'),
    path('<int:pk>/update', views.EventUpdateView.as_view(), name = 'event_update'),
    path('<int:pk>/delete', views.EventDeleteView.as_view(), name = 'event_delete')
]
