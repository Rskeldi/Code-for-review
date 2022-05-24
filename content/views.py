from rest_framework.generics import ListAPIView, RetrieveAPIView

from content.models import Page
from content.paginators import PagePagination
from content.serializers import PageListSerializer, PageDetailSerializer
from content.utils import get_content_relation_names_list


class PageListApiView(ListAPIView):
	queryset = Page.objects.all()
	serializer_class = PageListSerializer
	pagination_class = PagePagination


class PageDetailApiView(RetrieveAPIView):
	serializer_class = PageDetailSerializer

	def get_queryset(self):
		"""Get queryset with all relations"""
		relation_fields = get_content_relation_names_list()
		queryset = Page.objects.all().prefetch_related(*relation_fields)
		return queryset
