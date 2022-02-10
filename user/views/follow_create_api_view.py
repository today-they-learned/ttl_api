from rest_framework.generics import CreateAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from config.views import BaseView
from django.shortcuts import get_object_or_404
from user.serializers import FollowSerializer
from user.models import User, Follow


class FollowCreateAPIView(BaseView, CreateAPIView):
    """POST: api/users/user/follow
    Follow 생성 - 요청을 보내는 user(follower), follow 당하는 user(following)
    """
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, id, *args, **kwargs):
        following = get_object_or_404(User, id=id)
        Follow.objects.get_or_create(follower=self.current_user, following=following)

        return self.create(self, request, id, *args, **kwargs)



