from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('events/', include ('events.urls')),
    path('tasks/', include ('tasks.urls')),
    path('notes/', include ('notes.urls')),
    path("users/", include("users.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
