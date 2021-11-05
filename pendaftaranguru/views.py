from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from . forms import RegisterFormGuru
from django.contrib.auth.models import Group

# Create your views here.
def register_guru(request):
	context={}
	if request.is_ajax():
		form = RegisterFormGuru(request.POST)
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


