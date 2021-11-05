# Import supporting
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from userauth.models import CustomUser
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .models import Saran
from django.http.response import HttpResponseRedirect
from .forms import SaranForm


def home(request):
    return render(request, 'main/home.html')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            CustomUser = authenticate(username=username, password=password)
            if CustomUser is not None:
                login(request, CustomUser)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

@login_required(login_url='/login')
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

@login_required(login_url='/login')
def add_saran(request):
    context = {}
    form = SaranForm(request.POST or None)
    if (request.method == 'POST' and form.is_valid()):
        form.save() 
        return HttpResponseRedirect('/')
    context['form'] = form
    return render(request, 'main/home.html', context)

@login_required(login_url='/login')
def json(request):
    modelSaran = Saran.objects.all()
    data = serializers.serialize('json', modelSaran)
    return HttpResponse(data, content_type="application/json")