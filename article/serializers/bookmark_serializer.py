from rest_framework.serializers import ModelSerializer

from article.models import Bookmark

class BookmarkSerializer(ModelSerializer):
    """"Serializer definition for Bookmark Model."""
    
    class Meta:
        """"Meta definition for BookmarkSerializer."""
        
        model = Bookmark
        fields = [
            "user",
            "article",
            "created_at"
        ]
        read_only_fields = [
            "user",
            "created_at",
            "article",
        ]
