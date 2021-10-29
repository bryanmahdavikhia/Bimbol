from django.shortcuts import render
from django.http import response
from pendaftaranguru.models import userGuru
from django.contrib.auth.models import Group
# Create your views here.

def daftar_guru(request):
    guru = userGuru.objects.all()
    response = {'guru': guru}
    return render(request, 'daftar_guru.html', response)

# def booking_guru(request):

