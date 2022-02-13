from rest_framework import filters


class TagFilter(filters.BaseFilterBackend):
    """
    Return all objects which match any of the provided tags
    """

    def filter_queryset(self, request, queryset, view):
        tag = request.query_params.get("tag", None)
        if tag:
            queryset = queryset.filter(tags__name__iexact=tag).distinct()

        return queryset
