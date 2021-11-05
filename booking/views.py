from django.shortcuts import render
from django.http import response, JsonResponse
# from userauth.models import CustomUser
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from .models import Booking
# Create your views here.

# @login_required(login_url='/pendaftaransiswa/')
def daftar_guru(request):
    group = Group.objects.get(name='Guru')
    guru = group.user_set.all()
    response = {'guru': guru}
    return render(request, 'daftar_guru.html', response)

# @login_required(login_url='/pendaftaransiswa/')
def booking_guru(request):
    group = Group.objects.get(name='Guru')
    guru = group.user_set.all()
    booking_guru = BookForm()
    if request.is_ajax():
        booking_guru = BookForm(request.POST)
        guru = CustomUser.objects.get(nama_lengkap = request.POST.get("guru"))
        selesai = request.POST.get("selesai")

        booking_guru = Booking.objects.create(guru=guruu, selesai=selesai)
        booking_guru.save()
        return JsonResponse({'msg':'Success'})
    response = {'booking_guru':booking_guru, 'guru':guru}
    return render(request, 'pesan.html', response)