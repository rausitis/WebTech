from django.urls import path, include
from . import template_views
from . import api_views
from .api_routes import urlpatterns as api_routes

app_name = 'movieApp'

# Template URL patterns
template_patterns = [
    path('', template_views.index, name='index'),
    path('movies/', template_views.movies, name='movies'),
    path('movie/<int:movie_id>/', template_views.movie_detail, name='movie_detail'),
]

urlpatterns = [
    path('', include(template_patterns)),
    path('api/', include(api_routes)),
] 