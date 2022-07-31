from xml.etree.ElementInclude import include
from celery import Celery

app = Celery('celery',
             broker='amqp://tts:tts123@rabbit/tts_host',
             backend='rpc://',
             include=['simple_task'],
             )