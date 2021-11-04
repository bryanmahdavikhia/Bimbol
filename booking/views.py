from django.shortcuts import render
from django.http import response
from userauth.models import CustomUser
from django.contrib.auth.models import Group
# Create your views here.

def daftar_guru(request):
    guru = CustomUser.objects.all()
    response = {'guru': guru}
    return render(request, 'daftar_guru.html', response)

# def booking_guru(request):

