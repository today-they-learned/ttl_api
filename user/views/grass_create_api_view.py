from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from config.views import BaseView
from django.utils import timezone
from user.models import Grass
from user.serializers import GrassSerializer



class GrassCreateAPIView(BaseView, CreateAPIView):
    serializer_class = GrassSerializer
    queryset = Grass.objects.all()
    """ FollowingListView
    GET: api/users/grasses
    - 현재 유저의 Grass 모델을 생성한다.
    """
    
    def perform_create(self, serializer):
        serializer.save(user=self.current_user)

    def post(self, request, *args, **kwargs):
        if Grass.objects.filter(created_at=timezone.now(), user=self.current_user).count() > 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)        
        return self.create(request, *args, **kwargs)

        