from django.contrib import admin
from django.urls import include, path
from markus.views import index

urlpatterns = [
    path('', index, name='uji coba'),
]