from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import UsernameValidationView, EmailValidationView

urlpatterns = [
    path('', views.register_siswa, name='register_siswa'),
    path('home/', views.home, name='homesiswa'),
    path('validate-username/', csrf_exempt(UsernameValidationView.as_view()),name="validate-username"),
    path('validate-email/', csrf_exempt(EmailValidationView.as_view()),name="validate-email"),
]