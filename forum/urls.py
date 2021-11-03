from django.contrib import admin
from django.urls import path
from forum.views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('post/<int:id>/', postPage, name='post'),
    path('post/<int:id>/json', postPageJson, name='post json'),
    path('reply', replyPage, name='reply'),
    path('json', json, name='json'),
]