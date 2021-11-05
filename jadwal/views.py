from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Jadwal, CustomUser
from .forms import JadwalForm
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string


def jadwal_json(request):
    data = serializers.serialize('json', Jadwal.objects.all())
    return HttpResponse(data, content_type="application/json")

def is_guru(user):
    return user.groups.filter(name='Guru').exists()

@login_required(login_url='/pendaftaranguru/')
def jadwal(request, pk = None):
    if not is_guru(request.user):
        HttpResponseRedirect('/')
    
    edit = False
    jadwal = Jadwal.objects.all().filter(guru=request.user)
    
    # Update Jadwal
    if pk != None:
        edit = True
        obj = jadwal.filter(id=pk).first()

        if not obj:
            return HttpResponseRedirect('/jadwal')

        form = JadwalForm(instance=obj)
        if request.method == 'POST' and request.user.is_authenticated:
            form = JadwalForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/jadwal')
            else:
                pass

    # Create Jadwal
    else:
        if request.method == 'POST' and request.user.is_authenticated:
            form = JadwalForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.guru = request.user
                form.save()
                return HttpResponseRedirect('/jadwal')
            else:
                obj = None
        else:
            form = JadwalForm()
            obj = None

    return render(request, 'jadwal.html', {'form':form, 'jadwal': jadwal, 'obj':obj, 'edit':edit})

def filter_jadwal(request):
    kelas=request.GET.getlist('kelas[]')
    jadwal=Jadwal.objects.all().filter(guru=request.user)
    if len(kelas)>0:
	    jadwal=jadwal.filter(kelas__in=kelas).distinct()

    t=render_to_string('jadwal_card.html',{'jadwal':jadwal})
    return JsonResponse({'data':t})
