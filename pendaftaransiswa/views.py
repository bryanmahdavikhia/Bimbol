from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from . forms import RegisterFormSiswa
from django.contrib.auth.models import Group
import json
from django.http import JsonResponse
from django.views import View
from userauth.models import CustomUser
from django.core.validators import validate_email

class EmailValidationView(View):
	def post(self, request):
		data = json.loads(request.body)
		email = data['email']
		if not validate_email(email):
			return JsonResponse({'email_error': 'Email is invalid'}, status=400)
		if CustomUser.objects.filter(email=email).exists():
			return JsonResponse({'email_error': 'sorry email in use, choose another one'}, status=409)
		return JsonResponse({'email_valid': True})

class UsernameValidationView(View):
	def post(self, request):
		data = json.loads(request.body)
		username = data['username']
		if not str(username).isalnum():
			return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
		if CustomUser.objects.filter(username=username).exists():
			return JsonResponse({'username_error': 'sorry username in use, choose another one'}, status=409)
		return JsonResponse({'username_valid': True})



def register_siswa(request):
	context = {}
	if request.POST:
		form = RegisterFormSiswa(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(username=username, password=raw_password)

			# tambahkan user ke dalam group siswa
			group = Group.objects.get(name='Siswa')
			account.groups.add(group)

			login(request, account)
			return redirect('homesiswa')
		else:
			context['registerform'] = form
	else: #GET request
		form = RegisterFormSiswa()
		context['registerform'] = form
	# return render(request, 'register_siswa.html', context)
	# return render(request, 'index_siswa.html', context)
	return render(request, 'registration.html', context)

def home(request):
	return render(request, 'home_siswa.html', {})

