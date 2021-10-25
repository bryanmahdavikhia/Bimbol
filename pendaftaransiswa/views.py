from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterFormSiswa
from django.contrib.auth.models import Group

# Create your views here.
def Register_siswa(request):
	if request.method == "POST":
		form = RegisterFormSiswa(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			
			# tambahkan user ke dalam group siswa
			group = Group.objects.get(name='Siswa')
			user.groups.add(group)

			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('home')
	else:
		form = RegisterFormSiswa()
	
	response =  {'registerform':form}

	return render(request, 'register_siswa.html', response)

def home(request):
	return render(request, 'home.html', {})


