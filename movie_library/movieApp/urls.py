from .views import UserInfoViewset
from django.urls import path


urlpatterns = [
    path('movieApp/', UserInfoViewset.as_view()),
    path('movieApp/<int:id>', UserInfoViewset.as_view()),
    path('movieApp/getAll', UserInfoViewset.as_view())
]
