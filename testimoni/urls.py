from django.urls import path, include
from django.conf.urls import url
# from forum.views import index
from testimoni import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
# router.register('json', views.Testimoni)

urlpatterns = [
    path('json', views.Testimoni),
    path('add-testi-flutter', views.add_testi_flutter, name='add_testi_flutter'),
    url(r'^$', views.testimoni, name='testimoni_display'),
    url(r'^create/$', views.testimoni_create, name='testimoni_create'),
    url(r'^(?P<pk>\d+)/update/$', views.testimoni_update, name='testimoni_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.testimoni_delete, name='testimoni_delete'),
]