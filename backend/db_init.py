'''
멤버들에 대한 정보는 최초 시행 시점부터 이미 존재하고 있어야 하므로 
데이터베이스 초기화가 필요함!
'''

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django
django.setup()

from mainApp.models import Member, ModelLink
Member(id=1, name='구지혜', birth='2022/07/16', tmi='휴학생', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg').save()
Member(id=2, name='김혜진', birth='2022/07/16', tmi='복학생', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg').save()
Member(id=3, name='배준일', birth='2022/07/16', tmi='4학년', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg').save()
Member(id=4, name='이수현', birth='2022/07/16', tmi='AI 부전공', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg').save()
Member(id=5, name='최준혁', birth='2022/07/16', tmi='sample 목소리 주인', image_link='http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg').save()