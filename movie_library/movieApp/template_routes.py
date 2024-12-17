from django.urls import path
from . import template_views
from .template_views import verify_view, auth_view, home_view

template_routes = [
    path('', template_views.landing_page, name='landing_page'),
    path('movies/', template_views.movies, name='movies'),
    path('movie/<int:movie_id>/', template_views.movie_detail,
         name='movie_detail'),
    path('tv-shows/', template_views.tv_shows, name='tv_shows'),
    # 
    path('tv-shows-by-country/', template_views.tv_shows_by_country,
         name='tv_shows_by_country'),
    path('tv-shows-of-country/<int:cntry_id>/', template_views.tv_shows_of_country,
         name='tv_shows_of_country'),
    # path('tv-show/<int:tv_show_id>/', template_views.tv_show_detail,
    # name='tv_show_detail'),
    path('about/', template_views.about, name='about'),
    path('community/', template_views.community, name='community'),
    path('movies-by-country/', template_views.movies_by_country,
         name='movies_by_country'),
    path('movies-of-country/<int:cntry_id>/', template_views.movies_of_country,
         name='movies_of_country'),
    path('cast-and-crew/', template_views.cast_and_crew, name='cast_and_crew'),
    path('register/', template_views.register, name='register'),
    path('sign-in/', template_views.sign_in, name='sign_in'),

    # 2FA PATHS VERIF
    path('', home_view, name='home_view'),
    path('verify/', verify_view, name='verify_view'),
    path('login/', auth_view, name='auth_view'),
]
