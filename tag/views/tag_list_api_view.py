from rest_framework.generics import ListAPIView
from rest_framework import filters
from config.views import BaseView
from taggit.models import Tag
from tag.serializers import TagSerializer


class TagListAPIView(BaseView, ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["^name"]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
