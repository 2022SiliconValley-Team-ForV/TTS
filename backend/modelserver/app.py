from email import message
import time
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

#from test_tasks import test
#from simple_task import add

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def hello_world():
    return {'result': 'hello world!'}


@app.route('/api/texts', methods = ['POST','GET'])
def get_text():
    from test_tasks import test
    if request.method == 'POST':
        params = request.get_json()
        
        uuid = params['uuid']
        member_id = params['member_id']
        text = params['text']
        
        a = test.delay(uuid, member_id, text)

        while True:
            if a.ready() == False:
                time.sleep(5)
                continue
            else:
                # 프론트에 완료됐다고 전달
                # url =f'http://127.0.0.1:3000/detail/{member_id}'
                message = {'uuid': uuid, 'id': member_id}
                # requests.post(url, message)
                return message
                
        
        
    elif request.method == 'GET':
        txt = """
        안녕하세요.
        반갑습니다.
        """
        uuid = '022db29c-d0e2-11e5-bb4c-60f81dca7676'
        a = test.delay(uuid, 5, txt)
        #a = add.delay(5, 15)
        return {'task_id': a.id, 'task_status': a.ready()}
        

# front에서 셀러리가 일을 다 했는지 확인 -> 주기적으로 flask에 요청을 보내면서 체크 (작업이 걸리는 시간을 고려해서 작업끝나기 30초 전부터 보낸다)

