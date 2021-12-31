from django.shortcuts import render, get_object_or_404
from .models import Testimoni
from .forms import TestimoniForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from .serializers import TestimoniSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def testimoni(request):
    testimonial = Testimoni.objects.all()
    response = {'testimonial': testimonial}
    return render(request, 'testimoni_display.html', response)

# @login_required(login_url='/login')
def testimoni_update(request, pk):
	context ={}
	obj = get_object_or_404(Testimoni, pk = pk)
	form = TestimoniForm(request.POST or None, instance = obj)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/testimoni")

	context["form"] = form

	return render(request, "testimoni_form.html", context)

# @login_required(login_url='/login')
def testimoni_delete(request, pk):
    
    if request.is_ajax():
            testi = Testimoni.objects.get(pk=pk)
            testi.delete()
            return JsonResponse({"message":"success"})
    return JsonResponse({"message": "Maaf, penghapusan tidak berhasil"})

# @login_required(login_url='/login')
def testimoni_create(request):
    if request.method == "POST":
        form = TestimoniForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/testimoni')
    
    form = TestimoniForm
    return render(request, 'testimoni_form.html', {'form':form})

# @login_required(login_url='/login')
@api_view(['GET'])
def testimoni_json(request):
    data = serializers.serialize('json', Testimoni.objects.all())
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def add_testi_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        nama = data["nama"]

        kelas = data["kelas"]

        testimoni = data["testimoni"]

        testi_form = Testimoni(nama=nama, kelas=kelas, testimoni=testimoni)
        testi_form.save()
        return JsonResponse({"status": "success"}, status = 200)
    else:
        return JsonResponse({"status": "error"}, status = 401)

@api_view(['GET'])
class Testimoni(viewsets.ModelViewSet):
    queryset = Testimoni.objects.all()
    serializer_class = TestimoniSerializer





