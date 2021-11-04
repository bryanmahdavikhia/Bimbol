from django.urls import path
from .views import index, jadwal_json, add_jadwal

urlpatterns = [
    path('', index, name='index'),
    path('json', jadwal_json, name='json'),
    path('add', add_jadwal, name='add_jadwal'),
    # path('note-list', note_list, name='note_list')
]
