from django.urls import path, include
from . import views

urlpatterns = [
    path("chat/search/", views.search, name="search"),
    path("chat/addfriend/<str:name>", views.addFriend, name="addFriend"),
    path("chat/<str:username>", views.chat, name="chat"),
    path('chat/api/messages/<int:sender>/<int:receiver>',
         views.message_list, name='message-detail'),
    path('chat/api/messages', views.message_list, name='message-list'),
]
