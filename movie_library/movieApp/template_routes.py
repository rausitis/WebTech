from django.urls import path
from . import template_views

template_routes = [
    path('', template_views.landing_page, name='landing_page'),
    path('movies/', template_views.movies, name='movies'),
    path('movie/<int:movie_id>/', template_views.movie_detail, name='movie_detail'),
    path('tv-shows/', template_views.tv_shows, name='tv_shows'),
    # path('tv-show/<int:tv_show_id>/', template_views.tv_show_detail, name='tv_show_detail'),
    path('about/', template_views.about, name='about'),
    path('community/', template_views.community, name='community'),
    path('movies-by-country/', template_views.movies_by_country, name='movies_by_country'),
    path('country-movies/', template_views.country_movies, name='country_movies'),
    path('cast-and-crew/', template_views.cast_and_crew, name='cast_and_crew'),
    path('register/', template_views.register, name='register'),
    path('sign-in/', template_views.sign_in, name='sign_in'),
]
