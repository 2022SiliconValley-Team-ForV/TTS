'''
멤버들에 대한 정보는 최초 시행 시점부터 이미 존재하고 있어야 하므로 
데이터베이스 초기화가 필요함!
'''

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from mainApp.models import *

a = Member(id=1, name='구지혜', birth='2001/10/30', tmi='미적 감각이 뛰어난 프론트엔드 개발자', position='FRONTEND', github_link='https://github.com/jihye9549', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg')
b = Member(id=2, name='김혜진', birth='2000/02/17', tmi='개발에 집중하기 위해 "M2" Mac까지 섭렵한 프론트엔드 개발자', position='FRONTEND', github_link='https://github.com/llmeajinll', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg')
c = Member(id=3, name='배준일', birth='1998/03/15', tmi='안되면 될때까지 최선을 다해 이해하려고 노력하는 백엔드 개발자', position='BACKEND & DevOps', github_link='https://github.com/bjo6300',image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg')
d = Member(id=4, name='이수현', birth='1999/09/21', tmi='코딩을 하기 위해 새벽 5시에 Zoom에 접속하는 DevOps 개발자', position='DevOps', github_link='https://github.com/suhyeon3484', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg')
e = Member(id=5, name='최준혁', birth='1997/06/22', tmi='처음 접하는 프레임워크도 꼼꼼히 분석하는 백엔드 개발자', position='BACKEND & AI', github_link='https://github.com/hi-june', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg')

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