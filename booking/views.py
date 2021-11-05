from django.shortcuts import render
from django.http import response
from userauth.models import CustomUser
from django.contrib.auth.models import Group
# Create your views here.

def daftar_guru(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name == 'Guru':
        guru = CustomUser.objects.all()
    response = {'guru': guru}
    return render(request, 'daftar_guru.html', response)

def booking_guru(request):
    return render(request, 'pesan.html', {})