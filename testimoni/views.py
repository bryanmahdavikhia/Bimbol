from django.shortcuts import render, get_object_or_404
from .models import Testimoni
from .forms import TestimoniForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def testimoni(request):
    testimonial = Testimoni.objects.all()
    response = {'testimonial': testimonial}
    return render(request, 'testimoni_display.html', response)

# @login_required(login_url='/main/login/')
def testimoni_update(request, pk):
	context ={}
	obj = get_object_or_404(Testimoni, pk = pk)
	form = TestimoniForm(request.POST or None, instance = obj)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/testimoni")

	context["form"] = form

	return render(request, "testimoni_form.html", context)

# @login_required(login_url='/main/login/')
def testimoni_delete(request, pk):
    
    if request.is_ajax():
            testi = Testimoni.objects.get(pk=pk)
            testi.delete()
            return JsonResponse({"message":"success"})
    return JsonResponse({"message": "Maaf, penghapusan tidak berhasil"})

# @login_required(login_url='/main/login/')
def testimoni_create(request):
    if request.method == "POST":
        form = TestimoniForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/testimoni')
    
    form = TestimoniForm
    return render(request, 'testimoni_form.html', {'form':form})





