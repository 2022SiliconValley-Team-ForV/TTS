from django.db import models

# Create your models here.

class Member(models.Model): # id는 이미 장고에 있는 변수명이라 _id로 수정함
    _id = models.IntegerField(primary_key=True, null=False)  # pk
    name = models.CharField(max_length=8, null=False)
    birth = models.CharField(max_length=10)
    tmi = models.CharField(max_length=100)
    image_link = models.CharField(max_length=100, null=False)
    
class Model_link(models.Model):
    _id = models.ForeignKey(Member, on_delete=models.CASCADE, null=False)
    # test 테이블이라서 아래 부분부터는 not null 옵션을 넣지 않았습니다.
    glow_config = models.CharField(max_length=100)
    glow_pth = models.CharField(max_length=100)
    hifi_config = models.CharField(max_length=100)
    hifi_pth = models.CharField(max_length=100)