import time
from flask import Flask, jsonify, request
from flask_cors import CORS

#from test_tasks import test

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
        created_at = params['created_at']
        
        a = test.delay(uuid, member_id, text, created_at)

        while True:
            if a.ready() == False:
                time.sleep(5)
                continue
            else:
                return {'uuid': uuid, 'member_id': member_id, 'created_at': created_at}
                
    # elif request.method == 'GET':   # 이 부분은 테스트용입니다. 필요 없으시면 주석 처리하시고 쓰시면 됩니다!
        
    #     uuid = '302db29c-d0e2-11e5-bb4c-60f81dca7676'
    #     member_id = '5'
    #     text = '안녕하세요? 저희는 for voice 팀입니다!'
    #     created_at = '2022-08-02-18-44-33'

    #     a = test.delay(uuid, member_id, text, created_at)
        
    #     while True:
    #         if a.ready() == False:
    #             time.sleep(5)
    #             continue
    #         else:
    #             return {'uuid': uuid, 'id': member_id}

