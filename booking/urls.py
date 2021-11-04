from django.urls import path
from .views import daftar_guru

urlpatterns = [
    path('', daftar_guru, name='daftar guru')
]
