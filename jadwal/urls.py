from django.urls import path
from .views import index, jadwal_json

urlpatterns = [
    path('', index, name='index'),
    path('json', jadwal_json, name='json'),
    # path('add-note', add_note, name='add_note'),
    # path('note-list', note_list, name='note_list')
]
