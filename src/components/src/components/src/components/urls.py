from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
    path('add_video/', views.add_video, name='add_video'),
    path('video/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('register/', views.register_user, name='register_user'),
]