from celery import Celery
from pathlib import Path

lst = []
for i in range(3):
    lst.append(i)


celery = Celery('celery',
             broker='amqp://tts:tts123@rabbit/tts_host',
             backend='rpc://',
             )

@celery.task(name="add")
def add(x,y):
    result = int(x)+int(y)+lst[1]
    Path(f'./output/{result}_plz').touch()
    print(result)
    return result