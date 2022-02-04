from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from user.views.follow_create_api_view import FollowCreateAPIView

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("", include("dj_rest_auth.registration.urls")),
    path("api-token-auth/", obtain_auth_token),
    path("<str:following>", FollowCreateAPIView.as_view()),
]
