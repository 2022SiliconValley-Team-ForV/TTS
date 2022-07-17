from django.db import models

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=8, null=False, blank=False) # 이름 (varchar)
    birth = models.CharField(max_length=10, default='') # 생일
    tmi = models.CharField(max_length=100, default='') # tmi
    image_link = models.CharField(max_length=100, null=False, blank=False) # 프사링크

class ModelLink(models.Model):
    id = models.OneToOneField(Member, primary_key=True, on_delete=models.CASCADE, db_column="model_id", unique=True) # 1:1 관계
    glow_config = models.CharField(max_length=100, default='') 
    glow_pth = models.CharField(max_length=100, default='')
    hifi_config = models.CharField(max_length=100, default='')
    hifi_pth = models.CharField(max_length=100, default='')