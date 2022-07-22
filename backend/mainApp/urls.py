from django.urls import include, path
from .views import *
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'modellinks', ModelLinkViewSet)
router.register(r'texts', TextViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='TTS',
        default_version='v1', # API 버전
        description=
        '''
        텍스트를 입력하면 팀원 5명의 목소리로 읽어주는 서비스
        (Text to Speech)

        ''',
        terms_of_service='',
        contact=openapi.Contact(name='팀명', email='Team ForV'),
        license=openapi.License(name='MIT License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
]

# API 작성에 필요한 url 경로
urlpatterns += [
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]