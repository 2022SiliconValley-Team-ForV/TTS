import datetime
from django.db import models

# Create your models here.

class Member(models.Model): # id는 이미 장고에 있는 변수명이라 _id로 수정함
    id = models.AutoField(primary_key=True)  # pk
    name = models.CharField(max_length=8, null=False)
    birth = models.CharField(max_length=10, null=False)
    tmi = models.CharField(max_length=100, default='')
    position = models.CharField(max_length=100, default='')
    github_link = models.CharField(max_length=100, default='')
    image_link = models.CharField(max_length=100, null=False)
    # created_at = models.DateTimeField(default=datetime.now) # 해당 레코드 생성시 현재 시간 자동저장
    # updated_at = models.DateTimeField(auto_now=True) # 해당 레코드 갱신시 현재 시간 자동저장
    
class ModelLink(models.Model):
    id = models.OneToOneField(Member, primary_key=True, on_delete=models.CASCADE, db_column="id")
    # test 테이블이라서 아래 부분부터는 not null 옵션을 넣지 않았습니다.
    glow_config = models.CharField(max_length=100, default='', null=False)
    glow_pth = models.CharField(max_length=100, default='', null=False)
    glow_scale_stats = models.CharField(max_length=100, default='', null=False)
    hifi_config = models.CharField(max_length=100, default='', null=False)
    hifi_pth = models.CharField(max_length=100, default='', null=False)
    hifi_scale_stats = models.CharField(max_length=100, default='', null=False)
    # created_at = models.DateTimeField(default=datetime.now) # 해당 레코드 생성시 현재 시간 자동저장
    # updated_at = models.DateTimeField(auto_now=True) # 해당 레코드 갱신시 현재 시간 자동저장

class Text(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=100, default='')
    text = models.CharField(max_length=100, default='')
    created_at = models.CharField(max_length=100, default='')
    # updated_at = models.DateTimeField(auto_now=True) # 해당 레코드 갱신시 현재 시간 자동저장