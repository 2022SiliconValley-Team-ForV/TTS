from flask import jsonify
from celery_app import app

import os
from google.cloud import storage

from tts_modules import normalize_text
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
def test(uuid, member_id, text, create_at):
    wav_file = f'{member_id}_{uuid}_{create_at}_voice.wav'
    wav_path = f'./temp/{wav_file}'
    n_text = normalize_text(text, symbol)
    
    wav = synthesizer.tts(n_text, None, None)
    synthesizer.save_wav(wav, wav_path)   # change wav to .wav file
    
    blob = bucket.blob(wav_file)
    blob.upload_from_filename(wav_path) # upload wav file to gcp bucket

    if os.path.isfile(wav_path):
        os.remove(wav_path)

    return True