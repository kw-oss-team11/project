from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
        path('room_list/', views.room_list, name = 'room_list'),
        path('index/', views.index, name = 'index'),
        path('create_room/', views.create_room, name='create_room'),
        path("<str:room_name>/", views.room, name = "room"),
        path('delete_room/<str:room_name>/', views.delete_room, name='delete_room'),
]
