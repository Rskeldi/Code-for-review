from django.db import models
from django.urls import reverse

from content.abstract_models import TitleAbstractModel, ContentAbstractModel

# Choice for content order in page
Order_choice = (
    (1, 'By order'),
    (2, 'Mix')
)


class Page(TitleAbstractModel):
    """Page model"""
    content_order = models.PositiveSmallIntegerField(
        choices=Order_choice, default=1
    )

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'pk': self.pk})


class Video(ContentAbstractModel):
    """Video content model for Page"""
    video_url = models.URLField()
    subtitle_file_url = models.URLField()

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'


class Audio(ContentAbstractModel):
    """Audio content model for Page"""
    bitrate = models.PositiveIntegerField(verbose_name='Bitrate (bit/s)')

    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audios'


class Text(ContentAbstractModel):
    """Text content model for Page"""
    text = models.TextField()

    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'
