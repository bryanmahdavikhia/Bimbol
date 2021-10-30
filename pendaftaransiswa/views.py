from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from . forms import RegisterFormSiswa

def register_siswa(request):
	context = {}
	if request.POST:
		form = RegisterFormSiswa(request.POST)
		if form.is_valid():
			form.save()
			print("test")
			username = form.cleaned_data.get('username').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(username=username, password=raw_password)
			login(request, account)
			return redirect('homesiswa')
		else:
			context['registerform'] = form
	else: #GET request
		form = RegisterFormSiswa()
		context['registerform'] = form
	return render(request, 'register_siswa.html', context)

def home(request):
	return render(request, 'home.html', {})

