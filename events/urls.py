from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_home, name='events_home'),
    path('create', views.create_event, name = 'create_event'),
    path('<int:pk>', view.EventDetailView.)
]
