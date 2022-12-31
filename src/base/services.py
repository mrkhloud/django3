from rest_framework.pagination import PageNumberPagination


class ApiListPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'offset'
    page_size_query_param = 'page_size'
    max_page_size = 20
