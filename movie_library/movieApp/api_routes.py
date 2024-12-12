from .api_views import UserInfoViewset
from .api_views import ContentViewset
from .api_views import CastMembersViewset
from .api_views import FavoriteContentViewset
from .api_views import MovieMakersViewset
from django.views.generic import TemplateView
from .template_views import verify_view, auth_view, home_view

from django.urls import path


urlpatterns = [
    # REST APIs - interacting with DB
    path('users/', UserInfoViewset.as_view()),
    path('users/<int:id>/', UserInfoViewset.as_view()),

    path('content/', ContentViewset.as_view()),
    path('content/<int:id>/', ContentViewset.as_view()),

    path('castmembers/', CastMembersViewset.as_view()),
    path('castmembers/<int:id>/', CastMembersViewset.as_view()),

    path('favoritecontent/', FavoriteContentViewset.as_view()),
    path('favoritecontent/<int:id>/', FavoriteContentViewset.as_view()),

    path('moviemakers/', MovieMakersViewset.as_view()),
    path('moviemakers/<int:id>/', MovieMakersViewset.as_view()),


    # Add Login and Verify Routes for 2FA
    path('login/', auth_view, name='auth_view'),
    path('verify/', verify_view, name='verify_view'),
    path('', home_view, name='home_view'),
]
