from content.models import Page


def get_content_relation_names_list() -> list:
	"""Returned list with content relation names as str in list of Page model"""
	fields = Page._meta.get_fields()
	relation_fields = [
		field.name
		for field in fields
		if field.is_relation
	]
	return relation_fields
