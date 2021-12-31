from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from . forms import RegisterFormGuru
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from .forms import RegisterFormGuru
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register_guru(request):
	context={}
	if request.is_ajax():
		form = RegisterFormGuru(request.POST)
		print(form.errors.as_data())
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(username=username, password=raw_password)
			# tambahkan user ke dalam group Guru
			group = Group.objects.get(name='Guru')
			account.groups.add(group)

			login(request, account)
			return JsonResponse({
				'msg':'success'
			})
		else:
			context['registerform'] = form
		
		
	else:
		form = RegisterFormGuru()
		context['registerform'] = form
	return render(request, 'register_guru.html', context)

def home(request):
	return render(request, 'home.html', {})

@csrf_exempt
def regFlutter(request):
  data = json.loads(request.body)
  dataUser={
    'username':  data['username'],
    'password1': data['password1'],
    'password2': data['password2'],
	'email' : data['email'],
	'nama_lengkap': data['nama_lengkap'],
	'tanggal_lahir': '01-01-2001',
	'kelas' : '10',
	'mata_pelajaran' : 'Matematika',
	'alamat' : 'baung',
	'jenis_kelamin' : 'wanita',
	'agree' : True,
	'nomor_telefon' : data['nomor_telefon']

  }

  form = RegisterFormGuru(dataUser or None)

  if data['password1']==data['password2']:
    user = form.save()

    return JsonResponse({
      'status': 'success'
    })
  else:
    return JsonResponse({
      'status': 'failed'
    })



