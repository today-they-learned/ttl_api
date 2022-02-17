from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from user.views import (
    FollowCreateAPIView,
    FollowDestroyAPIView,
    FollowingListView,
    FollowerListView,
    UserRetrieveAPIView,
    GrassListAPIView,
    UserDestoryAPIView,
    UserRepositoryUpdateApiView,
    UserSubscribeMailUpdateApiView,
    UserVelogUsernameUpdateApiView,
)

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("", include("dj_rest_auth.registration.urls")),
    path("user/destroy/", UserDestoryAPIView.as_view()),
    path("api-token-auth/", obtain_auth_token),
    path("<int:id>/", UserRetrieveAPIView.as_view()),
    path("<int:id>/follow/", FollowCreateAPIView.as_view()),
    path("<int:id>/unfollow/", FollowDestroyAPIView.as_view()),
    path("<int:id>/follwing/", FollowingListView.as_view()),
    path("<int:id>/follwer/", FollowerListView.as_view()),
    path("<int:id>/grasses/", GrassListAPIView.as_view()),
    path("user/repository/", UserRepositoryUpdateApiView.as_view()),
    path("user/subscribe_mail/", UserSubscribeMailUpdateApiView.as_view()),
    path("user/velog_username/", UserVelogUsernameUpdateApiView.as_view()),
]
