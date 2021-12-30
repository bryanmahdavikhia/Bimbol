from django.contrib import admin
from django.urls import path
from forum.views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('json', json, name='json'),
    path('post/<int:id>/', postPage, name='post'),
    path('post/<int:id>/json', forumJson, name='post json'),
    path('create', createForum),
    path('reply', replyPage, name='reply'),
    path('reply/<int:id>/json', replyJson),
    path('reply/create/<int:id>', createReply)
]