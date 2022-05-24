import random

from django.db.models import F

from content.models import Page
from content.utils import get_content_relation_names_list


class ContentDataService:
	"""Get the content of page_instance , sort by order and convert to dict"""
	def __init__(self, page_instance):
		self.page = page_instance
		self.relation_fields = get_content_relation_names_list()

	def get_content_data(self) -> list:
		"""Returned sorted or mixed content dict in list"""
		content_data = self.get_content_data_from_page_instance()
		content_data = self.sort_or_mix_content_data(content_data)
		return content_data

	def get_content_data_from_page_instance(self) -> list:
		"""Get content data as dict from page instance and return in list"""
		content_data = []
		for field in self.relation_fields:
			content_queryset = getattr(self.page, field)
			content_list = list(content_queryset.values())
			content_data += content_list
		return content_data

	def sort_or_mix_content_data(self, content_data) -> list:
		"""Sort or mix content data by order field and return in list"""
		if self.page.content_order == 1:
			content_data = sorted(
				content_data,
				key=lambda x: x.get('order')
			)
		else:
			random.shuffle(content_data)
		return content_data


class PageContentViewCounterUpdateService:
	"""This service updated all content counters from one page"""

	def __init__(self, page_pk):
		self.page = Page.objects.get(pk=page_pk)
		self.relation_fields = get_content_relation_names_list()

	def update_content_counters(self):
		"""Updating counters with F() for atomic increment"""
		for field in self.relation_fields:
			content_queryset = getattr(self.page, field)
			content_queryset.all().update(counter=F('counter') + 1)
