from django.contrib import admin
from django.urls import include, path
from forum.views import index

urlpatterns = [
    path('', index, name='uji coba'),
]