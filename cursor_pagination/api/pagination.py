# for specific view class
from rest_framework.pagination import CursorPagination

class MyPagination(CursorPagination):
	page_size = 3
	ordering = 'name'
	cursor_query_param = 'cu'