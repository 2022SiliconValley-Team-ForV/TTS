from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    path('members/', MemberList.as_view()),
    path('members/<int:pk>/', MemberDetail.as_view()),
    path('models/', ModelList.as_view()),
    path('models/<int:pk>', ModelDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)