import logging
import time
from django.contrib.auth import get_user_model

from config import celery_app

User = get_user_model()
logger = logging.getLogger(__name__)


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()


@celery_app.task()
def get_publishing_task(self):
    time.sleep(5)
    data = {'success': 'publishing task complete'}
    logger.info('--------------------------------------')
    logger.info(data)
    logger.info('--------------------------------------')
    return data


@celery_app.task()
def get_task_1():
    time.sleep(5)
    data = {'success': 'task 1 complete'}
    logger.info('--------------------------------------')
    logger.info(data)
    logger.info('--------------------------------------')
    return data


@celery_app.task()
def get_task_2():
    time.sleep(60)
    data = {'success': 'task 2 complete'}
    logger.info('--------------------------------------')
    logger.info(data)
    logger.info('--------------------------------------')
    return data
