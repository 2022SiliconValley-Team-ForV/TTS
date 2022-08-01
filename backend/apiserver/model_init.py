import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from mainApp.models import ModelLink
import wget


def filedownload(url1, url2, url3, path):
    wget.download(url1, path)
    wget.download(url2, path)
    wget.download(url3, path)

for i in range(1,6):

    i = str(i)
    save_path = '../modelserver/voice_model/glow-tts/' + i   # 다운받을 파일을 저장할 경로
    modellink = ModelLink.objects.get(id=i)

    filedownload(modellink.glow_pth, modellink.glow_config, modellink.glow_scale_stats, save_path)

    # hifi 경로
    save_path = '../modelserver/voice_model/hifigan-v2/' + i    # 다운받을 파일을 저장할 경로

    filedownload(modellink.hifi_pth, modellink.hifi_config, modellink.hifi_scale_stats, save_path)

    
    
