from django.urls import path
from .views import jadwal_json, jadwal, filter_jadwal

urlpatterns = [
    # path('', index, name='index'),
    path('filter-jadwal', filter_jadwal, name='json'),
    path('', jadwal, name='add_jadwal'),
    path('<str:pk>/', jadwal, name='update_jadwal')
    # path('note-list', note_list, name='note_list')
]
