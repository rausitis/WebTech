from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('katamaran/', admin.site.urls),
    path('', include('movieApp.urls')),
]
