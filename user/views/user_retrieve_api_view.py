from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from config.views import BaseView
from article.models import Article
from user.models import User
from user.serializers import UserSerializer


class UserRetrieveAPIView(BaseView, RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = Article.objects.all()

    def retrieve(self, request, id, *args, **kwargs):
        """GET: /api/users/:id
        User 정보
        """
        instance = self.get_object(User, id=id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
