from rest_framework.generics import CreateAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from config.views import BaseView
from django.shortcuts import get_object_or_404
from user.serializers import FollowSerializer
from user.models import User, Follow


class FollowCreateAPIView(BaseView, CreateAPIView):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    authentication_classses = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, following, *args, **kwargs):
        """POST: api/users/user/follow
        Follow 생성
        """

        following = get_object_or_404(User, username=following)
        follow, is_follow = Follow.objects.get_or_create(follower=self.current_user,
                                                         following=following)

        if not is_follow:
            return self.destroy(self, request, following, *args, **kwargs)

        return self.create(self, request, following, *args, **kwargs)



