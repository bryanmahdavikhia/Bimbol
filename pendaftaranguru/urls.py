from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_guru, name='pendaftaranguru'),
    path('home/', views.home, name='homeguru'),
]