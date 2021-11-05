from django.shortcuts import render
from django.http import response, JsonResponse
from userauth.models import CustomUser
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import BookForm
# Create your views here.

def daftar_guru(request):
    group = Group.objects.get(name='Guru')
    guru = group.user_set.all()
    response = {'guru': guru}
    return render(request, 'daftar_guru.html', response)

def booking_guru(request):
    booking_guru = BookForm()
    if request.is_ajax():
        booking_guru = BookForm(request.POST)
        if booking_guru.is_valid() and request.method == 'POST':
            booking_guru.save()
            return JsonResponse({'msg':'Success'})
    response = {'booking_guru':booking_guru}
    return render(request, 'pesan.html', response)