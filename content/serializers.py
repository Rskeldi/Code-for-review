from rest_framework import serializers

from content.models import Page
from content.services import ContentDataService
from content.tasks import update_content_counters


class PageListSerializer(serializers.ModelSerializer):
	page_url = serializers.SerializerMethodField()
	content_order = serializers.SerializerMethodField()

	class Meta:
		model = Page
		fields = '__all__'

	def get_page_url(self, instance) -> str:
		"""Generate url to detail of page"""
		request = self.context.get('request')
		url = instance.get_absolute_url()
		return request.build_absolute_uri(url)

	def get_content_order(self, instance) -> str:
		"""Return the human-readable choice for content order"""
		return instance.get_content_order_display()


class PageDetailSerializer(serializers.ModelSerializer):
	content = serializers.SerializerMethodField()

	class Meta:
		model = Page
		fields = '__all__'

	def get_content(self, instance) -> list:
		"""Update all content counters for this instance
		and return in list with content objects as dict"""
		update_content_counters.delay(instance.pk)
		content = ContentDataService(instance)
		return content.get_content_data()
