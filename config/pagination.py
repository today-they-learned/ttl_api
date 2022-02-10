from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = "per_page"
    max_page_size = 1000
