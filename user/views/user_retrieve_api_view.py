from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from config.views import BaseView
from user.models import User
from user.serializers import UserSerializer
from rest_framework.permissions import AllowAny


class UserRetrieveAPIView(BaseView, RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """GET: /api/users/:id
        User 정보
        """
        return self.retrieve(request, *args, **kwargs)
