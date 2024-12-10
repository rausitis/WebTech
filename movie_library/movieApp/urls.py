from django.urls import path, include
from .template_routes import template_routes
from .api_routes import urlpatterns as api_routes

app_name = 'movieApp'


urlpatterns = [
    path('', include(template_routes)),
    path('', include(api_routes)),
]
