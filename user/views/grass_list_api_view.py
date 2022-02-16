from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from config.views import BaseView
from user.models import Grass, User
from user.serializers import GrassSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny


class GrassListAPIView(BaseView, ListAPIView):
    serializer_class = GrassSerializer
    queryset = Grass.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, id):
        """FollowingListView
        GET: /users/:id/grasses
        - id에 해당하는 유저(User)의 Grass 목록이 반환된다.
        """
        user = get_object_or_404(User, id=id)
        queryset = self.get_queryset().filter(user=user)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
