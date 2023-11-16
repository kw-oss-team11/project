
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('chat_app/', include('chat.urls', namespace = 'chat_app')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.home_view, name='home'),  # 홈페이지 URL
    path('post/', include('post.urls')),
    path('gs25/', views.gs25, name='gs25'),
    path('seven/', views.seven, name='seven'),
    path('cu/', views.cu, name='cu'),
]
