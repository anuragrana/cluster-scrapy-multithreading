from celery import Celery

app = Celery(
    'celery_main',
    broker='amqp://myuser:mypassword@rabbit:5672',
    include=['celery_main.task_receiver']
)
