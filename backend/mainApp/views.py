from django.shortcuts import render

# CRUD 기능 구현을 위한 라이브러리 import
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

# 세부 페이지 설명부분을 위해 일단 Member 테이블만 추가했습니다.
# 모델 파일에 대한 테이블은 추후에 추가할 예정
from .serializers import MemberSerializer
from .models import Member

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
    
''' sample json data!!
    {
        "_id": 1,
        "name": "구지혜",
        "birth": "2022/07/16",
        "tmi": "휴학생",
        "image_link": "http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg"
    },
    {
        "_id": 2,
        "name": "김혜진",
        "birth": "2022/07/16",
        "tmi": "복학생",
        "image_link": "http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg"
    },
    {
        "_id": 3,
        "name": "배준일",
        "birth": "2022/07/16",
        "tmi": "4학년",
        "image_link": "http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg"
    },
    {
        "_id": 4,
        "name": "이수현",
        "birth": "2022/07/16",
        "tmi": "AI를 부전공",
        "image_link": "http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg"
    },
    {
        "_id": 5,
        "name": "최준혁",
        "birth": "2022/07/16",
        "tmi": "sample 목소리 주인",
        "image_link": "http://storage.googleapis.com/forv_bucket/seulgi_sample.jpeg"
    }
'''