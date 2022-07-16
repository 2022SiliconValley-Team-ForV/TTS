from django.db import models

class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=8, null=False, blank=False) # 이름 (varchar)
    birth = models.CharField(max_length=10, default='') # 생일
    tmi = models.CharField(max_length=100, default='') # tmi
    image_link = models.CharField(max_length=100, null=False, blank=False) # 프사링크