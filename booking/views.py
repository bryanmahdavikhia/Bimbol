from django.shortcuts import render
from django.http import response, JsonResponse, HttpResponse
from userauth.models import CustomUser
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Booking
from datetime import date
import json
# Create your views here.

@login_required(login_url='/login')
def daftar_guru(request):
    group = Group.objects.get(name='Guru')
    guru = group.user_set.all()
    response = {'guru': guru}
    return render(request, 'daftar_guru.html', response)

@login_required(login_url='/login')
def booking_guru(request):
    group = Group.objects.get(name='Guru')
    guru = group.user_set.all()
    booking_guru = BookForm()
    if request.is_ajax():
        booking_guru = BookForm(request.POST)
        guruu = CustomUser.objects.get(nama_lengkap = request.POST.get("guru"))
        selesai = request.POST.get("selesai")

        booking_guru = Booking.objects.create(guru=guruu, selesai=selesai)
        booking_guru.save()
        return JsonResponse({'msg':'Success'})
    response = {'booking_guru':booking_guru, 'guru':guru}
    return render(request, 'pesan.html', response)

@csrf_exempt
def get_guru(request):
    list_guru = []
    group = Group.objects.get(name='Guru')
    guru = group.user_set.all()
    for i in guru:
        list_guru.append({
            "nama_guru" : i.nama_lengkap,
            "mata_pelajaran" : i.mata_pelajaran,
            "jenis_kelamin" : i.jenis_kelamin
        })
    list_guru = json.dumps(list_guru)
    return HttpResponse(list_guru, content_type='application/json')

@csrf_exempt
def post_guru(request):
    data = json.loads(request.body)
    post_guru = BookForm()
    guruu = data['guru']
    selesai = date(2002, 1, 6)
    
    post_guru = Booking.objects.create(guru=guruu, selesai=selesai)
    post_guru.save()
    
    response = HttpResponse('success')
    response.status_code = 200
    return response
