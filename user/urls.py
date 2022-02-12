from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings


from user.views import (
    FollowCreateAPIView,
    FollowDestroyAPIView,
    FollowingListView,
    FollowerListView,
    UserRetrieveAPIView,
    PasswordResetConfirmView,
    PasswordChangeView,
    PasswordResetView,
    LoginView,
    LogoutView,
    UserDetailsView,
)

urlpatterns = [
    path("<int:id>/", UserRetrieveAPIView.as_view()),
    path("<int:id>/follow", FollowCreateAPIView.as_view()),
    path("<int:id>/unfollow", FollowDestroyAPIView.as_view()),
    path("<int:id>/follwing", FollowingListView.as_view()),
    path("<int:id>/follwer", FollowerListView.as_view()),
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path(
        "password/reset/confirm/",
        PasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),
    path("login/", LoginView.as_view(), name="rest_login"),
    # URLs that require a user to be logged in with a valid session / token.
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("password/change/", PasswordChangeView.as_view(), name="rest_password_change"),
    path("", include("dj_rest_auth.registration.urls")),
    path("api-token-auth/", obtain_auth_token),
]


if getattr(settings, "REST_USE_JWT", False):
    from rest_framework_simplejwt.views import TokenVerifyView

    from dj_rest_auth.jwt_auth import get_refresh_view

    urlpatterns += [
        path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
        path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    ]
