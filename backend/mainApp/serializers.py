'''
Serializer는 DRF가 제공하는 클래스인데, 
DB 인스턴스를 JSON 데이터로 생성한다.
'''

from pyexpat import model
from rest_framework import serializers
from .models import Member, Model_link

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('_id', 'name', 'birth', 'tmi', 'image_link')
        
class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model_link
        fields = ('_id', 'glow_config', 'glow_pth', 'hifi_config', 'hifi_pth')