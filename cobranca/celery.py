import os

from celery import Celery
from kombu import Queue, Exchange

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cobranca.settings')

app = Celery('cobranca', broker=f'pyamqp://guest:guest@{os.environ.get("RABBIT_SERVER")}//')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

default_exchange = Exchange('status_pagamento_pedido', type='direct')

app.conf.task_queues = (
    Queue('status_pagamento_pedido', default_exchange, routing_key='status_pagamento_pedido'),
)

app.conf.task_default_queue = 'status_pagamento_pedido'
app.conf.task_default_exchange = 'status_pagamento_pedido'
app.conf.task_default_routing_key = 'status_pagamento_pedido'

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

