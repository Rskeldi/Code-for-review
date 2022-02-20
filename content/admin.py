from django.contrib import admin

from content import models
from content.utils import get_content_relation_names_list


class ContentAdminMixin:
	readonly_fields = ('counter',)
	extra = 1


class VideoAdminInline(ContentAdminMixin, admin.TabularInline):
	model = models.Video


class AudioAdminInline(ContentAdminMixin, admin.TabularInline):
	model = models.Audio


class TextAdminInline(ContentAdminMixin, admin.TabularInline):
	model = models.Text


@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
	search_fields = ['^title']
	inlines = (
		VideoAdminInline, AudioAdminInline, TextAdminInline,
	)

	def get_search_fields(self, request):
		"""Add all page related fields in search"""
		relation_fields = get_content_relation_names_list()
		relation_search_fields = [
			'^%s__title' % field
			for field in relation_fields
		]
		return self.search_fields + relation_search_fields
