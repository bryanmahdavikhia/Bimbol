from django.urls import path
from django.conf.urls import url
from forum.views import index

from testimoni import views

urlpatterns = [
    path('tes', index, name='testing'),
    path('json', views.testimoni_json, name='testimoni_json'),
    path('add-testi-flutter', views.add_testi_flutter, name='add_testi_flutter'),
    url(r'^$', views.testimoni, name='testimoni_display'),
    url(r'^create/$', views.testimoni_create, name='testimoni_create'),
    url(r'^(?P<pk>\d+)/update/$', views.testimoni_update, name='testimoni_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.testimoni_delete, name='testimoni_delete'),
    url(r'^$', views.testimoni, name='testimoni_display'),
]