import json
import tts_modules

"""
-- 작업 과정
init.json 구성 초안
{
    "modelFiles": [
        {
            "id": "1", 
            "bucket_urls": 
            {
                "g_check": " ", 
                "g_config": " ", 
                "g_scale_stats": " ", 
                "h_check": " ",
                "h_config": " ", 
                "h_scale_stats": " ",
            }
        },
        {
            "id": "2", 
            "bucket_urls": 
            {
                "g_check": " ", 
                "g_config": " ", 
                "g_scale_stats": " ", 
                "h_check": " ",
                "h_config": " ", 
                "h_scale_stats": " ",
            }
        },
        {
            "id": "3", 
            "bucket_urls": 
            {
                "g_check": " ", 
                "g_config": " ", 
                "g_scale_stats": " ", 
                "h_check": " ",
                "h_config": " ", 
                "h_scale_stats": " ",
            }
        },
        {
            "id": "4", 
            "bucket_urls": 
            {
                "g_check": " ", 
                "g_config": " ", 
                "g_scale_stats": " ", 
                "h_check": " ",
                "h_config": " ", 
                "h_scale_stats": " ",
            }
        },
        {
            "id": "5", 
            "bucket_urls": 
            {
                "g_check": " ", 
                "g_config": " ", 
                "g_scale_stats": " ", 
                "h_check": " ",
                "h_config": " ", 
                "h_scale_stats": " ",
            }
        }
    ]
}

tts.json 구성 초안
{
    "id": " ",
    "text": " "
}

members = set_model(jsonReq)   # return type: list

"""


# get model from google bucket and initialize
def set_model(jsonReq):
    '''
    0. syn 요청 전달받음(json)
    1. 전달받은 json으로부터 필요한 모델파일들을 가져옴(wget 통해서 서버로 다운로드)
    2. config.json 파일의 "Audio" -> "stats_path" 부분 변경
    3. 각 멤버별로 synthesizer 객체, symbols 객체 초기화
    '''
    json_object = json.loads(jsonReq)   # json String으로부터 json 객체 생성

    
    # 1. 필요한 모델파일들을 Synthesizer에 전달 후 symbol 설정
    synthesizer = Synthesizer(
        "./voice_model/glow-tts/g_checkpoint_30000.pth.tar",
        "./voice_model/glow-tts/g_config.json",
        None,
        "./voice_model/hifigan-v2/h_checkpoint_305000.pth.tar",
        "./voice_model/hifigan-v2/h_config.json",
        None,
        None,
        False,)

    symbol = synthesizer.tts_config.characters.characters  # normalize_text가 호출될 때 필요한 변수
    
    return

def get_tts():
    '''
    def get_tts: # celery에 등록
    0. tts 요청 전달받음
    1. 전달받은 json으로부터 id와 text 추출
    3. id와 매칭되는 synthesizer와 symbol로 wav '파일' 제작 or '객체' 생성
    4. 방향에 따라 달라짐!
    '''
    count = 0
    
    # 2. text를 받아와서 normalize_multiline 함수에 입력
    texts = """
    아래 문장들은 모델 학습을 위해 사용하지 않은 문장들입니다.
    이렇게 목소리를 학습시킬 수 있습니다.
    """

    for text in normalize_multiline_text(texts):
        wav = synthesizer.tts(text, None, None)
        synthesizer.save_wav(wav, f'./output/sample_{count}.wav')   # change wav to .wav file
        count+=1

'''
if __name__ == '__main__':  # command: python tasks.py
    main()
'''