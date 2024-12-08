from django.urls import path, include
from .template_routes import template_routes
from .api_routes import urlpatterns as api_routes

app_name = 'movieApp'


urlpatterns = [
    path('', include(template_routes)),
    path('api/', include(api_routes)),
<<<<<<< HEAD
]
=======
] 
>>>>>>> 1041b518188f6002e4d1e9f7fc24d7445090c852
