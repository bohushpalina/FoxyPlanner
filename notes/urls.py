from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes, name = 'notes'),
    path('create', views.create_note, name = 'create_note'),
    path('<int:pk>/edit', views.EditNote.as_view(), name = "edit_note"),
    path('<int:pk>/delete', views.DeleteNote.as_view(), name = "delete_note"),
]