from .views import UserInfoViewset
from .views import ContentViewset
from .views import CastMembersViewset
from .views import FavoriteContentViewset
from .views import MovieMakersViewset
from django.views.generic import TemplateView

from django.urls import path
from .views import RegisterUser


urlpatterns = [

    # REST APIs - interacting with DB
    path('userinfo/', UserInfoViewset.as_view()),
    path('userinfo/<int:id>/', UserInfoViewset.as_view()),

    path('content/', ContentViewset.as_view()),
    path('content/<int:id>/', ContentViewset.as_view()),

    path('castmembers/', CastMembersViewset.as_view()),
    path('castmembers/<int:id>/', CastMembersViewset.as_view()),

    path('favoritecontent/', FavoriteContentViewset.as_view()),
    path('favoritecontent/<int:id>/', FavoriteContentViewset.as_view()),

    path('moviemakers/', MovieMakersViewset.as_view()),
    path('moviemakers/<int:id>/', MovieMakersViewset.as_view()),

    # APIs - LOADS PAGES
    path('movies/', TemplateView.as_view(template_name="Movies.html"),
         name="movies-page"),

    path('about/', TemplateView.as_view(template_name="About.html"),
         name="about-page"),

    path('actors/', TemplateView.as_view(template_name="Actors.html"),
         name="actors-page"),

    path('castandcrew/',
         TemplateView.as_view(template_name="CastAmdCrew.html"),
         name="cast-and-crew-page"),

    path('community/', TemplateView.as_view(template_name="Community.html"),
         name="community-page"),

    path('countrymovies/',
         TemplateView.as_view(template_name="Country_movies.html"),
         name="country-movies-page"),

    path('forgotpassword/',
         TemplateView.as_view(template_name="ForgotPassword.html"),
         name="forgot-password-page"),

    path('landingpagebackup/',
         TemplateView.as_view(template_name="LandingPage_backup.html"),
         name="landing-page-backup"),

    path('landingpage/',
         TemplateView.as_view(template_name="LandingPage.html"),
         name="landing-page"),

    path('movie/', TemplateView.as_view(template_name="Movie.html"),
         name="movie-page"),

    path('moviesbycountry/',
         TemplateView.as_view(template_name="MoviesByCountry.html"),
         name="movies-by-country-page"),

    path('register/', RegisterUser, name="registration-page"),

    path('signin/', TemplateView.as_view(template_name="SignIn.html"),
         name="sign-in-page"),

    path('tvshows/', TemplateView.as_view(template_name="TVShows.html"),
         name="tv-shows-page"),
]
