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
    
    # glow 경로
    locals()[str(i)+'g_pth_'] = modellink.glow_pth
    locals()[str(i)+'g_config_'] = modellink.glow_config
    locals()[str(i)+'g_scale_stats_'] = modellink.glow_scale_stats

    filedownload(locals()[str(i)+'g_pth_'], locals()[str(i)+'g_config_'], locals()[str(i)+'g_scale_stats_'], save_path)

    # hifi 경로
    save_path = '../modelserver/voice_model/hifigan-v2/' + i    # 다운받을 파일을 저장할 경로

    locals()[str(i)+'h_pth_'] = modellink.hifi_pth
    locals()[str(i)+'h_config_'] = modellink.hifi_config
    locals()[str(i)+'h_scale_stats_'] = modellink.hifi_scale_stats
   
    filedownload(locals()[str(i)+'h_pth_'], locals()[str(i)+'h_config_'], locals()[str(i)+'h_scale_stats_'], save_path)

    
    
