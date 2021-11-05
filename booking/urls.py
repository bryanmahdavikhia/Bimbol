from django.urls import path
from .views import daftar_guru, booking_guru

urlpatterns = [
    path('', daftar_guru, name='daftar guru'),
    path('pesan/', booking_guru, name='booking guru')
]
