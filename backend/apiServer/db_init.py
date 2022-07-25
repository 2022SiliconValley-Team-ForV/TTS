'''
멤버들에 대한 정보는 최초 시행 시점부터 이미 존재하고 있어야 하므로 
데이터베이스 초기화가 필요함!
'''

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from mainApp.models import *

a = Member(id=1, name='구지혜', birth='2022/07/16', tmi='휴학생', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg')
b = Member(id=2, name='김혜진', birth='2022/07/16', tmi='복학생', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg')
c = Member(id=3, name='배준일', birth='2022/07/16', tmi='4학년', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg')
d = Member(id=4, name='이수현', birth='2022/07/16', tmi='AI 부전공', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg')
e = Member(id=5, name='최준혁', birth='2022/07/16', tmi='sample 목소리 주인', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg')

a.save()
b.save()
c.save()
d.save()
e.save()


# ModelLink의 id에는 Model 객체가 전달되어야 함!
ModelLink(id=a, 
          glow_config='http://storage.googleapis.com/forv_bucket/5g_config.json', 
          glow_pth='http://storage.googleapis.com/forv_bucket/5g_checkpoint_30000.pth.tar',
          glow_scale_stats = 'http://storage.googleapis.com/forv_bucket/5g_config.json',
          hifi_config='http://storage.googleapis.com/forv_bucket/5h_config.json', 
          hifi_pth='http://storage.googleapis.com/forv_bucket/5h_checkpoint_305000.pth.tar',
          hifi_scale_stats = 'http://storage.googleapis.com/forv_bucket/5h_config.json'
          ).save()

ModelLink(id=b, 
          glow_config='http://storage.googleapis.com/forv_bucket/5g_config.json', 
          glow_pth='http://storage.googleapis.com/forv_bucket/5g_checkpoint_30000.pth.tar',
          glow_scale_stats = 'http://storage.googleapis.com/forv_bucket/5g_config.json',
          hifi_config='http://storage.googleapis.com/forv_bucket/5h_config.json', 
          hifi_pth='http://storage.googleapis.com/forv_bucket/5h_checkpoint_305000.pth.tar',
          hifi_scale_stats = 'http://storage.googleapis.com/forv_bucket/5h_config.json'
          ).save()

ModelLink(id=c, 
          glow_config='http://storage.googleapis.com/forv_bucket/5g_config.json', 
          glow_pth='http://storage.googleapis.com/forv_bucket/5g_checkpoint_30000.pth.tar',
          glow_scale_stats = 'http://storage.googleapis.com/forv_bucket/5g_config.json',
          hifi_config='http://storage.googleapis.com/forv_bucket/5h_config.json', 
          hifi_pth='http://storage.googleapis.com/forv_bucket/5h_checkpoint_305000.pth.tar',
          hifi_scale_stats = 'http://storage.googleapis.com/forv_bucket/5h_config.json'
          ).save()

ModelLink(id=d, 
          glow_config='http://storage.googleapis.com/forv_bucket/5g_config.json', 
          glow_pth='http://storage.googleapis.com/forv_bucket/5g_checkpoint_30000.pth.tar',
          glow_scale_stats = 'http://storage.googleapis.com/forv_bucket/5g_config.json',
          hifi_config='http://storage.googleapis.com/forv_bucket/5h_config.json', 
          hifi_pth='http://storage.googleapis.com/forv_bucket/5h_checkpoint_305000.pth.tar',
          hifi_scale_stats = 'http://storage.googleapis.com/forv_bucket/5h_config.json'
          ).save()

ModelLink(id=e, 
          glow_config='http://storage.googleapis.com/forv_bucket/5g_config.json', 
          glow_pth='http://storage.googleapis.com/forv_bucket/5g_checkpoint_30000.pth.tar',
          glow_scale_stats = 'http://storage.googleapis.com/forv_bucket/5g_config.json',
          hifi_config='http://storage.googleapis.com/forv_bucket/5h_config.json', 
          hifi_pth='http://storage.googleapis.com/forv_bucket/5h_checkpoint_305000.pth.tar',
          hifi_scale_stats = 'http://storage.googleapis.com/forv_bucket/5h_config.json'
          ).save()

Text(id=a,text="1").save()
Text(id=b,text="2").save()
Text(id=c,text="3").save()
Text(id=d,text="4").save()
Text(id=e,text="경찰청창살 쇠창살").save()