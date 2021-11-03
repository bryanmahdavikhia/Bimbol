from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_siswa, name='register_siswa'),
    path('home/', views.home, name='homesiswa'),
]