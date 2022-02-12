from rest_framework.serializers import ModelSerializer

from article.models import UploadImage


class UploadImageSerializer(ModelSerializer):
    """Serializer definition for UploadImage Model."""

    class Meta:
        """Meta definition for UploadImageSerializer."""

        model = UploadImage
        fields = ["image"]
