from celery import Celery

app = Celery('celery',
             broker='amqp://tts:tts123@rabbit/tts_host',
             #broker='amqp://tts:tts123@rabbitmq3:5672/tts_host',
             backend='rpc://',
             include=['test_tasks'],
             )

'''
RABBITMQ_HOST=os.environ.get('RABBITMQ_HOST')
RABBITMQ_PORT=os.environ.get('RABBITMQ_PORT')
RABBITMQ_USER=os.environ.get('RABBITMQ_USER')
RABBITMQ_PASSWORD=os.environ.get('RABBITMQ_PASSWORD')

RBMQ_CONNECTION_URI=f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}//'

environment:
        - RABBITMQ_DEFAULT_USER=tts
        - RABBITMQ_DEFAULT_PASS=tts123
        - RABBITMQ_DEFAULT_VHOST=tts_host
'''