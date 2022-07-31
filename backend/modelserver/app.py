from flask import Flask, jsonify, request
from flask_cors import CORS

from test_tasks import test

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# # celery = Celery('celery',
# #              broker='amqp://tts:tts123@rabbit/tts_host',
# #              backend='rpc://',
# #              )


@app.route('/')
def hello_world():
    return {'result': 'hello world!'}


@app.route('/api/texts', methods = ['POST','GET'])
def get_text():
    if request.method == 'POST':
        params = request.get_json()
        id = params['id']
        text = params['text']
        a = test.delay(id, text)
        return {'task_id': a.id, 'task_status': a.ready()}
        
    elif request.method == 'GET':
        a = test.delay(5, '안녕하세요.')
        return {'task_id': a.id, 'task_status': a.ready()}
        

# front에서 셀러리가 일을 다 했는지 확인 -> 주기적으로 flask에 요청을 보내면서 체크 (작업이 걸리는 시간을 고려해서 작업끝나기 30초 전부터 보낸다)