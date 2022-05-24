from django.test import TestCase

from content.models import Page, Video
from content.utils import get_content_relation_names_list


class AuthorListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Create 3 pages and 3 videos for first pages"""
        number_of_authors = 3
        for page_num in range(number_of_authors):
            Page.objects.create(title='Page #%s' % page_num)
        page = Page.objects.first()
        for num in range(3):
            Video.objects.create(
                title='Video %s' % num,
                subtitle_file_url='subtitle-%s.com' % num,
                video_url='video-%s.com' % num,
                page=page
            )

    def test_page_list_api(self):
        """Page list api worked test"""
        resp = self.client.get('/api/v1/')
        self.assertEqual(resp.status_code, 200)

    def test_page_detail_api(self):
        """Page detail api worked test"""
        resp = self.client.get('/api/v1/1/')
        self.assertEqual(resp.status_code, 200)

    def test_page_content(self):
        """Test for the correct filling of content on the page"""
        page = Page.objects.first()
        content_count = 0
        for field in get_content_relation_names_list():
            content_queryset = getattr(page, field).all()
            content_count += content_queryset.count()
        resp = self.client.get('/api/v1/%s/?format=json' % page.pk)
        content = resp.json().get('content')
        self.assertEqual(len(content), content_count)
