'''
멤버들에 대한 정보는 최초 시행 시점부터 이미 존재하고 있어야 하므로 
데이터베이스 초기화가 필요함!
'''

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

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
ModelLink(id=e, 
          glow_config='http://storage.googleapis.com/forv_bucket/g_config.json', 
          glow_pth='http://storage.googleapis.com/forv_bucket/g_checkpoint_30000.pth.tar', 
          hifi_config='http://storage.googleapis.com/forv_bucket/h_config.json', 
          hifi_pth='http://storage.googleapis.com/forv_bucket/h_checkpoint_305000.pth.tar').save()

Text(id=e,text="경찰청창살 쇠창살").save()