import json
from django.contrib.auth import authenticate, login 
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from userauth.models import CustomUser
from django.contrib.auth.models import Group

from pendaftaransiswa.forms import RegisterFormSiswa

@csrf_exempt
def signup_siswa(request) :
    form = RegisterFormSiswa(json.loads(request.body))
    if form.is_valid():
        user = form.save()

        username = form.cleaned_data.get('username').lower()
        raw_password = form.cleaned_data.get('password1')
        account = authenticate(username=username, password=raw_password)

        group = Group.objects.get(name='Siswa')
        account.groups.add(group)
        
        login(request, user)
        return JsonResponse({
            "status": True,
            "message": "Signup successful",
        }, status=200)
    else:
        return JsonResponse(form.errors, status = 400)



