from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from config.views import BaseView
from user.serializers import FollowSerializer
from user.models import User


class FollowingListView(BaseView, ListAPIView):
    """ FollowingListView
    GET: api/users/user/follwing
    - 현재 유저가 Following(create) 목록(list)이 반환된다.
    """
    serializer_class = FollowSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get(self, request, id, *args, **kwargs):
        user = get_object_or_404(User, id=id)
        queryset = self.filter_queryset(self.get_queryset(follower=user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FollowerListView(BaseView, ListAPIView):
    """ FollowerListView
    GET: api/users/user/follwing
    - 현재 유저의 Follower(create) 목록(list)이 반환된다.
    """
    serializer_class = FollowSerializer
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, id, *args, **kwargs):
        user = get_object_or_404(User, id=id)
        queryset = self.filter_queryset(self.get_queryset(following=user))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
