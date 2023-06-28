from rest_framework.pagination import LimitOffsetPagination , CursorPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit =10

class MyCursorPagination(CursorPagination):
    ordering = '-esal'
    page_size = 5