from django.shortcuts import render

# 세부 페이지 설명부분을 위해 일단 Member 테이블만 추가했습니다.
# 모델 파일에 대한 테이블은 추후에 추가할 예정
from .serializers import MemberSerializer, ModelSerializer, TextSerializer
from .models import Member, ModelLink, Text
from rest_framework import viewsets

# Create your views here.

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