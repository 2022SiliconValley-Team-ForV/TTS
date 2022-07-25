from django.contrib import admin
from .models import Member, ModelLink  # 각 테이블에 대한 관리자 등록

# Register your models here.
admin.site.register(Member)
admin.site.register(ModelLink)

'''
사용자 이름: super
이메일 주소: TTS@ForV.com
Password: Team_ForV
'''