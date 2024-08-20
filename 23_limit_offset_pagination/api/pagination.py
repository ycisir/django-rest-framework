# for specific view class
from rest_framework.pagination import LimitOffsetPagination

class MyPagination(LimitOffsetPagination):
	default_limit = 5
	# limit_query_param = 'limit'
	# offset_query_param = 'my-offset'
	# max_limit = 5