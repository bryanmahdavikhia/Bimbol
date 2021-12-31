from django.urls import path
from .views import jadwal, filter_jadwal, get_jadwals, get_jadwal, create_jadwal, update_jadwal

urlpatterns = [
    # path('', index, name='index'),
    path('filter-jadwal', filter_jadwal, name='json'),
    path('', jadwal, name='add_jadwal'),
    path('<str:pk>/', jadwal, name='jadwal'),
    # path('api', jadwal_json, name='api'),
    path('api/get/', get_jadwals, name='get_jadwals'),
    path('api/get/<str:pk>/', get_jadwal, name='get_jadwal'),
    path('api/create/', create_jadwal, name='create_jadwal'),
    path('api/update/<str:pk>/', update_jadwal, name='update_jadwal')
]
