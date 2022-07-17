from django.shortcuts import render

from .models import Member, ModelLink
from .serializers import MemberSerializer, ModelLinkSerializer
from rest_framework import viewsets

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()  
    serializer_class = MemberSerializer  

class ModelLinkViewSet(viewsets.ModelViewSet):
    queryset = ModelLink.objects.all()  
    serializer_class = ModelLinkSerializer
