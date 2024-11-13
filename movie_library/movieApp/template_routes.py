from django.urls import path
from . import template_views

template_routes = [
    path('', template_views.landing_page, name='landing'),
    path('movies/', template_views.movies, name='movies'),
    path('movie/<int:movie_id>/', template_views.movie_detail, name='movie-detail'),
    path('tv-shows/', template_views.tv_shows, name='tv-shows'),
    path('about/', template_views.about, name='about'),
    path('community/', template_views.community, name='community'),
    path('movies-by-country/', template_views.movies_by_country, name='movies-by-country'),
    path('country-movies/', template_views.country_movies, name='country-movies'),
    path('register/', template_views.register, name='register'),
    path('sign-in/', template_views.sign_in, name='sign-in'),
]
