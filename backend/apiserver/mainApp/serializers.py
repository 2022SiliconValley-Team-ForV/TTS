'''
Serializer는 DRF가 제공하는 클래스인데, 
DB 인스턴스를 JSON 데이터로 생성한다.
'''

from pyexpat import model
from rest_framework import serializers
from .models import Member, ModelLink, Text

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        
class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelLink
        fields = '__all__'

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'