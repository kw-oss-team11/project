# urls.py
from django.urls import path, include
from . import views
from .views import post_list, add_post, delete_post, increase_likes

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/new/', add_post, name='add_post'),
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('chat/', include('chat.urls')),
    path('increase_likes/<int:post_id>/', increase_likes, name='increase_likes'),
]
