from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("", include("dj_rest_auth.registration.urls")),
    path("api-token-auth/", obtain_auth_token),
]
