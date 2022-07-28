from celery import Celery

app = Celery('config',
             broker='amqp://tts:tts123@rabbit/tts_host',
             backend='rpc://',
             include=['config.tasks'])

if __name__ == '__main__':
    app.start()
