from rest_framework.serializers import ModelSerializer

from user.models import Grass

class GrassSerializer(ModelSerializer):
    """Serializer definition for Grass Model."""

    class Meta:
        """Meta definition for GrassSerializer."""

        model = Grass
        fields = [
            "user",
            "study_count",
            "write_count",
            "edit_count",
            "created_at"
        ]
        read_only_fields = [
           "user",
            "study_count",
            "write_count",
            "edit_count",
        ]

