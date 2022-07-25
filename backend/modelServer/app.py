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
from flask import Flask, request
from konlpy.tag import Mecab
import g2pk


app = Flask(__name__)

mecab = Mecab()
gp = g2pk.G2p()


@app.route('/')
def hello_world():
    return {'result': 'hello world!'}


@app.route('/mecab')
def get_mecab():
    k_str = request.args.get('q', u'영등포구청역에 있는 맛집 좀 알려주세요.')
    morphs = mecab.morphs(k_str)
    nouns = mecab.nouns(k_str)
    pos = mecab.pos(k_str)
    return {'morphs': morphs, 'nouns': nouns, 'pos': pos}


@app.route('/g2pk')
def run_g2pk():
    k_str = request.args.get('q', u'신을 신고 얼른 동사무소에 가서 혼인 신고 해라')
    print(k_str)
    res = gp(k_str)
    return {'result': res}