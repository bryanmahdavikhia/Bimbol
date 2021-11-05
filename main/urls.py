from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login_request, name="login"),
    path('logout', views.logout_request, name="logout"),
    path('json', views.json, name='json'),
]