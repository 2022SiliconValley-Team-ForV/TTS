from __future__ import absolute_import
from rabbitcelery.celery import app
import time
from celery import shared_task
# tasks 모듈
# 모듈화된 AI 함수를 여기에 대입
# 밑에는 예시(run_tasks도 수정해야함)

@shared_task
def longtime_add(x, y):
    print('long time task begins')
    # sleep 5 seconds
    time.sleep(5)
    print ('long time task finished')
    return x + y