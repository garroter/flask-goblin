from .celery import celery
from celery.utils.log import get_task_logger
from modules.invoice_proxy.models.send import Send
from modules.invoice_proxy.models.header import Header
from modules.invoice_proxy.models.invoice import Invoice
import httpx
import json
from flask import current_app as app

logger = get_task_logger(__name__)


@celery.task(queue="queue-test", bind=True, acks_late=True)
def run_queue(self, data):
    pass