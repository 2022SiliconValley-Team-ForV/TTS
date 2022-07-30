'''
cd /content
!git clone --depth 1 https://github.com/sce-tts/TTS.git -b sce-tts
!git clone --depth 1 https://github.com/sce-tts/g2pK.git

cd /content/TTS
!pip install -q --no-cache-dir -e .

cd /content/g2pK
!pip install -q --no-cache-dir "konlpy" "jamo" "nltk" "python-mecab-ko"
!pip install -q --no-cache-dir -e .
'''
from celery import Celery
from flask import Flask, jsonify, request
from importlib_metadata import method_cache
import requests
# from konlpy.tag import Mecab
# import g2pk
from flask_cors import CORS
# from test_tasks import test
from simple_task import add


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
celery = Celery('celery',
             broker='amqp://tts:tts123@rabbit/tts_host',
             backend='rpc://',
             )

# mecab = Mecab()
# gp = g2pk.G2p()


@app.route('/')
def hello_world():
    return {'result': 'hello world!'}


@app.route('/api/texts', methods = ['POST','GET'])
def get_text():
    if request.method == 'POST':
        params = request.get_json()
        print(params)
        id = params['id']
        print(id)
        text = params['text']
        print(text)
        a = add.delay(id, text)
        # print(a.id)
        return (params)
        
    elif request.method == 'GET':
        
        return('get')
        

# front에서 셀러리가 일을 다 했는지 확인 -> 주기적으로 flask에 요청을 보내면서 체크 (작업이 걸리는 시간을 고려해서 작업끝나기 30초 전부터 보낸다)

# @app.route('/mecab')
# def get_mecab():
#     k_str = request.args.get('q', u'영등포구청역에 있는 맛집 좀 알려주세요.')
#     morphs = mecab.morphs(k_str)
#     nouns = mecab.nouns(k_str)
#     pos = mecab.pos(k_str)
#     return {'morphs': morphs, 'nouns': nouns, 'pos': pos}


# @app.route('/g2pk')
# def run_g2pk():
#     k_str = request.args.get('q', u'신을 신고 얼른 동사무소에 가서 혼인 신고 해라')
#     print(k_str)
#     res = gp(k_str)
#     return {'result': res}