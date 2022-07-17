from rest_framework import serializers

from .models import Member, ModelLink


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        db_table = 'member' # db 테이블에서 보이는 이름
        fields = ['id','name', 'birth', 'tmi', 'image_link']

    def __str__(self): # 관리자페이지에서 보이는 단어
        return self.name

class ModelLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelLink
        db_table = 'modellink' # db 테이블에서 보이는 이름
        fields = '__all__'

    def __str__(self): # 관리자페이지에서 보이는 단어
        return self.id