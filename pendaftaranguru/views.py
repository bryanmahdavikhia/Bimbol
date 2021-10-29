from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterFormGuru
from django.contrib.auth.models import Group

# Create your views here.
def Register_guru(request):
	if request.method == "POST":
		form = RegisterFormGuru(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get['username']
			password = form.cleaned_data.get['password1']
			user = authenticate(request,username=username, password=password)
			
			# tambahkan user ke dalam group Guru
			group = Group.objects.get(name='Guru')
			user.groups.add(group)

			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('home')
	else:
		form = RegisterFormGuru()
	
	response =  {'registerform':form}

	return render(request, 'register_guru.html', response)

def home(request):
	return render(request, 'home.html', {})


