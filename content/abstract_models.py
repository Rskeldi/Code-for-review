from django.db import models


class TitleAbstractModel(models.Model):
	"""Abstract model with title field"""
	title = models.CharField(max_length=200)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


class ContentAbstractModel(TitleAbstractModel):
	"""Abstract with common fields for content"""
	counter = models.PositiveIntegerField(default=0)
	order = models.PositiveIntegerField(default=0)
	page = models.ForeignKey(
		'Page', on_delete=models.CASCADE, related_name='%(class)ss'
	)

	class Meta:
		abstract = True
