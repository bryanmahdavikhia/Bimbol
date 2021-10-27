from django.urls import path

from forum.views import index
from .views import index

urlpatterns = [
    path('', index, name='index')
]