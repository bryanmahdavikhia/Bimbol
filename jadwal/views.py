from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Jadwal, CustomUser
from .forms import JadwalForm
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required


# def index(request):
#     jadwal = Jadwal.objects.all()  # TODO Implement this
#     response = {'jadwal': jadwal}
#     return render(request, 'jadwal.html', response)

def jadwal_json(request):
    data = serializers.serialize('json', Jadwal.objects.all())
    return HttpResponse(data, content_type="application/json")

def is_guru(user):
    return user.groups.filter(name='Guru').exists()

@login_required(login_url='/pendaftaranguru/')
def jadwal(request, pk = None):
    if not is_guru(request.user):
        HttpResponseRedirect('/')
    
    failed = False
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
                failed = True
        
        form = JadwalForm()
        obj = None

    return render(request, 'jadwal.html', {'form':form, 'failed':failed, 'jadwal': jadwal, 'obj':obj, 'edit':edit})
