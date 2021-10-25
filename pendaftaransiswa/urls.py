from django.urls import path
from . import views

urlpatterns = [
    path('', views.Register_siswa, name='pendaftaransiswa'),
    path('home/', views.home, name='home'),
]