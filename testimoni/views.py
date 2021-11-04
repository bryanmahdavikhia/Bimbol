from django.forms import models
from django.shortcuts import render
from .models import Testimoni
from .forms import TestimoniForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_testimoni(request):
    if request.method == "POST":
        form = TestimoniForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/testimoni/display')
    
    form = TestimoniForm
    return render(request, 'testimoni_form.html', {'form':form})

def testimoni(request):
    testimonial = Testimoni.objects.all()
    response = {'testimonial': testimonial}
    return render(request, 'testimoni_display.html', response)