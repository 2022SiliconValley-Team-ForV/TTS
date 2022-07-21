from django.urls import include, path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'modellinks', ModelLinkViewSet)
router.register(r'texts', TextViewSet)


urlpatterns = [
    path('', include(router.urls)),
]