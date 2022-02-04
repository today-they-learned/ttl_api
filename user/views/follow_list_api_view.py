from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from config.views import BaseView
from user.serializers import FollowSerializer
from user.models import Follow


class FollowingListView(BaseView, ListAPIView):
    """ FollowingListView
    - 현재 유저가 Following(create) 목록(list)이 반환된다.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    authentication_classses = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Follow.objects.filter(follower=self.current_user) # 현재 유저가 아닌 접근한 유저이어야하는데..?

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FollowerListView(BaseView, ListAPIView):
    """ FollowerListView
    - 현재 유저의 Follower(create) 목록(list)이 반환된다.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    authentication_classses = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Follow.objects.filter(following=self.current_user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
