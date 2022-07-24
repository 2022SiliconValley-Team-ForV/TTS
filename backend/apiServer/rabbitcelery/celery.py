from __future__ import absolute_import
from celery import Celery

app = Celery('rabbitcelery',
             # broker: //userid:password@hostname:port/virtual_host
             # RabbitMQ의 URL은 amqp://localhost
             # local : hostname=localhost
             # 도커 개발환경 : hostname=rabbit
             broker='amqp://tts:tts123@rabbit/tts_host',
             # rpc는 결과를 AMQP 메시지로 보내는 것을 의미
             # task를 실행하고 난 뒤 결과물을 파일로 저장가능 // 다른 옵션
             backend='rpc://',
             # include 인수는 Celery Worker를 시작할 때 가져올 모듈의 리스트를 지정
             include=['rabbitcelery.tasks'])
