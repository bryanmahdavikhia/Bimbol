from django.urls import path
from .views import daftar_guru, booking_guru, get_guru, post_guru

urlpatterns = [
    path('', daftar_guru, name='daftar guru'),
    path('pesan/', booking_guru, name='booking guru'),
    path('get_guru/', get_guru, name='get guru'),
    path('post_guru/', post_guru, name='post guru'),
]
