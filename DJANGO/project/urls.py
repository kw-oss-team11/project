
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.home_view, name='home'),  # 홈페이지 URL
    path('hello/', views.hello_view, name='hello'),
]
