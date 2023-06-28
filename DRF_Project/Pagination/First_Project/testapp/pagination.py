from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 5
    # page_query_param = 'mypage'
    page_size_query_param = 'page_size'
    last_page_strings = ('end_page',)