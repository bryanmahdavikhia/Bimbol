from django.urls import path

from forum.views import index
from .views import add_testimoni, index, testimoni

urlpatterns = [
    path('', add_testimoni, name='tambahkantestimoni'),
    path('tes', index, name='testing'),
    path('display', testimoni, name='testimonisiswa')
]