from django.shortcuts import render

# CRUD 기능 구현을 위한 라이브러리 import
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

# 세부 페이지 설명부분을 위해 일단 Member 테이블만 추가했습니다.
# 모델 파일에 대한 테이블은 추후에 추가할 예정
from .serializers import MemberSerializer, ModelSerializer
from .models import Member, ModelLink

# Create your views here.
class MemberList(APIView):  # 멤버들의 목록을 보여줌
    def get(self, request): # 리스트 보여줄 때
        members = Member.objects.all()
        
        serializer = MemberSerializer(members, many=True)   # 여러 개 객체 serialize하려면 many=True
        return Response(serializer.data)

    def post(self, request):    # 세 맴버 추가 시
        serializer = MemberSerializer(data=request.data)    # request.data는 사용자 입력 데이터
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MemberDetail(APIView):
    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):    # Member detail 보기
        member = self.get_object(pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):    # Member detail 수정하기
        member = self.get_object(pk)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():   # 유효성 검사
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None): # Member 삭제
        member = self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
##############################################################################################################
class ModelList(APIView):  # 모델들의 목록을 보여줌
    def get(self, request): # 리스트 보여줄 때
        models = ModelLink.objects.all()
        
        serializer = ModelSerializer(models, many=True)   # 여러 개 객체 serialize하려면 many=True
        return Response(serializer.data)

    def post(self, request):    # 세 맴버 추가 시
        serializer = ModelSerializer(data=request.data)    # request.data는 사용자 입력 데이터
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ModelDetail(APIView):
    def get_object(self, pk):
        try:
            return ModelLink.objects.get(pk=pk)
        except ModelLink.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):    # Model detail 보기
        model = self.get_object(pk)
        serializer = ModelSerializer(model)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):    # Model detail 수정하기
        model = self.get_object(pk)
        serializer = MemberSerializer(model, data=request.data)
        if serializer.is_valid():   # 유효성 검사
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None): # Model 삭제
        model = self.get_object(pk)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)