from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response

from config.views import BaseView
from user.models import Grass,User
from user.serializers import GrassSerializer
from django.shortcuts import get_object_or_404

class GrassListAPIView(BaseView, ListAPIView):
    serializer_class = GrassSerializer
    queryset = Grass.objects.all()
    
    def get(self, request, id, *args, **kwargs):
        """ FollowingListView
        GET: api/users/:id/grasses
        - id에 해당하는 유저(User)의 Grass 목록이 반환된다.
        """
        user = get_object_or_404(User, id=id)
        queryset = Grass.objects.filter(user=user)
        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
