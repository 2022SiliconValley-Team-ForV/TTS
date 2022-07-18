from django.db import models

# Create your models here.

class Member(models.Model): # id는 이미 장고에 있는 변수명이라 _id로 수정함
    id = models.AutoField(primary_key=True)  # pk
    name = models.CharField(max_length=8, null=False)
    birth = models.CharField(max_length=10, default='')
    tmi = models.CharField(max_length=100, default='')
    image_link = models.CharField(max_length=100, null=False, default='')
    
class ModelLink(models.Model):
    id = models.OneToOneField(Member, primary_key=True, on_delete=models.CASCADE, db_column="id", unique=True)
    # test 테이블이라서 아래 부분부터는 not null 옵션을 넣지 않았습니다.
    glow_config = models.CharField(max_length=100, default='')
    glow_pth = models.CharField(max_length=100, default='')
    hifi_config = models.CharField(max_length=100, default='')
    hifi_pth = models.CharField(max_length=100, default='')