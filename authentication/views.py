import json
from django.contrib.auth import authenticate, login 
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from userauth.models import CustomUser

from pendaftaransiswa.forms import RegisterFormSiswa

@csrf_exempt
def signup_siswa(request) :
    print(request.method)
    print(request.body)
    form = RegisterFormSiswa(json.loads(request.body))
    if form.is_valid():
        print("kesini ga")
        user = form.save()

        group = Group.objects.get(name='Siswa')
        account.groups.add(group)
        
        login(request, user)
        return JsonResponse({
            "status": True,
            "message": "Signup successful",
        }, status=200)
    else:
        return JsonResponse(form.errors, status = 400)

