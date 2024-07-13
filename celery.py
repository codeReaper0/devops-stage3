import os
from messaging.tasks import log_message
from celery import Celery

# Set the broker to RabbitMQ
broker_url = os.environ.get('CELERY_BROKER_URL', 'amqp://guest@localhost//')

app = Celery('messaging_system', broker=broker_url,
             backend='rpc://')

# Register tasks with the app
app.register_task(log_message)
