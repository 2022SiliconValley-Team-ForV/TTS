from time import sleep
import time
from tkinter.tix import Tree
from celery import Celery
from django.shortcuts import render
import requests

# 세부 페이지 설명부분을 위해 일단 Member 테이블만 추가했습니다.
# 모델 파일에 대한 테이블은 추후에 추가할 예정
from .serializers import MemberSerializer, ModelSerializer, TextSerializer
from .models import Member, ModelLink, Text
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
celery = Celery('celery',
             broker='amqp://tts:tts123@rabbit/tts_host',
             backend='rpc://',
             )

# ViewSet : Post, Get, Put, Delete 기본기능 내장
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()  
    serializer_class = MemberSerializer  

class ModelLinkViewSet(viewsets.ModelViewSet):
    queryset = ModelLink.objects.all()  
    serializer_class = ModelSerializer

class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all()  
    serializer_class = TextSerializer

    # def update(self,request, pk=None):
    #     id = request.data['id']
    #     text = request.data['text']
    #     # print(id, text)

        # try :
            
        #     url = 'http://172.20.0.2:5000/api/texts'
        #     params = {'id': id, 'text':text}
        #     print(id, text)
        #     requests.post(url, json=params)
        #     return requests.Response
        # except:
        #     print('except')
        