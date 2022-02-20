from celery import shared_task

from content.services import PageContentViewCounterUpdateService


@shared_task
def task_for_test(num1, num2):
	"""Easy task for celery test"""
	return num1 + num2


@shared_task
def update_content_counters(page_pk):
	"""This task starting service for updating content counters from one page"""
	service = PageContentViewCounterUpdateService(page_pk)
	service.update_content_counters()
	return 'Counters updated'
