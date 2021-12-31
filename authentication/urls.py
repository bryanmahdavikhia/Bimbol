from django.urls import path
from django.urls import path
from .views import signup_siswa

urlpatterns = [
    path('signup-siswa', signup_siswa, name='signup-siswa'),
]

