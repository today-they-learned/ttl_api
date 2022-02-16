from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from article.models import UploadImage
from article.serializers import UploadImageSerializer
from config.views import BaseView


class UploadImageCreateAPIView(BaseView, CreateAPIView):
    serializer_class = UploadImageSerializer
    queryset = UploadImage.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            {
                "url": serializer.data["image"],
                "public_url": serializer.data["image"],
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
