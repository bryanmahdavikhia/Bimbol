from django.urls import path
from . import views

urlpatterns = [
    path('', views.Register_guru, name='pendaftaranguru'),
    path('home/', views.home, name='home'),
]