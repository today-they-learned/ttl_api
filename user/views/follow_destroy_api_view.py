from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from config.views import BaseView
from django.shortcuts import get_object_or_404
from user.serializers import FollowSerializer
from user.models import User, Follow


class FollowDestroyAPIView(BaseView, DestroyAPIView):
    """delete: api/users/user/unfollow
    Follow 삭제 - 요청을 보내는 user(follower), follow 당하는 user(following)
    """

    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, id, *args, **kwargs):
        following = get_object_or_404(User, id=id)
        follow = get_object_or_404(
            Follow, follower=self.current_user, following=following
        )
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
