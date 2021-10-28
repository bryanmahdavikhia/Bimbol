from django.urls import path
from . import views

urlpatterns = [
    path('', views.Register_guru, name='pendaftaran guru'),
    path('home/', views.home, name='home'),
]