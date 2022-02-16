from rest_framework.generics import DestroyAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from config.views import BaseView
from user.serializers import UserSerializer
from user.models import User


class UserDestoryAPIView(BaseView, DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        return self.current_user

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
