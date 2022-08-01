from flask import jsonify
from celery_app import app

import os
from google.cloud import storage

from tts_modules import normalize_multiline_text
from TTS.TTS.utils.synthesizer import Synthesizer

############################################################################################################
print('synthesizer start!')
synthesizer = Synthesizer(
    f"./voice_model/glow-tts/5/5g_checkpoint_30000.pth.tar",
    f"./voice_model/glow-tts/5/5g_config.json",
    None,
    f"./voice_model/hifigan-v2/5/5h_checkpoint_305000.pth.tar",
    f"./voice_model/hifigan-v2/5/5h_config.json",
    None,
    None,
    False,)
symbol = synthesizer.tts_config.characters.characters  # normalize_text가 호출될 때 필요한 변수
print('synthesizer finished!')

############################################################################################################
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./micro-handler.json" # wav gcp bucket 업로드를 위한 key path

bucket_name = 'forv_bucket'    # 서비스 계정 생성한 bucket 이름 입력
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)

# source_file_name = ''    # GCP에 업로드할 파일 절대경로
# destination_blob_name = ''    # 업로드할 파일을 GCP에 저장할 때의 이름
# blob = bucket.blob(destination_blob_name)
# blob.upload_from_filename(source_file_name)

############################################################################################################
@app.task(name="test")
def test(uuid, id, text):
    count = 0
    for text in normalize_multiline_text(text, symbol):
        wav_file = f'{uuid}_{id}_sample_{count}.wav'
        wav = synthesizer.tts(text, None, None)
        synthesizer.save_wav(wav, f'./temp/{wav_file}')   # change wav to .wav file
        
        blob = bucket.blob(wav_file)
        blob.upload_from_filename(f'./temp/{wav_file}') # upload wav file to gcp bucket
        count+=1
    return True #jsonify({'uuid': uuid, 'id': id, 'count': count})