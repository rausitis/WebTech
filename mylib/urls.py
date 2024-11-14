from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from djangoProject import settings
from . import views
urlpatterns = [
   path("",views.MainView.as_view(), name="main"),
   path("Movies/",views.MoviesView.as_view(),name="movies"),
   path("Movie/<int:id>/",views.MovieDetail,name="movie"),
   path("TvShows/",views.TVShowsView.as_view(),name="tvshows"),
   path("crew/",views.CrewView.as_view(),name="crew"),
   path("about/",views.AboutPage.as_view(),name="about"),
   path("Moviesbycountry/",views.MoviesbyCountry.as_view(),name="moviesbycountry"),
   #login i register
   path("signin/",views.login_view,name="signin"),
   path("register",views.register,name="register")
]