# urls.py
from django.urls import path
from .views import post_list, add_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('add/', add_post, name='add_post'),
    # 다른 URL 패턴도 필요하다면 추가 가능
]
