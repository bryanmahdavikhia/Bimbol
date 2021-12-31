from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Jadwal, CustomUser
from .forms import JadwalForm
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JadwalSerializer
from rest_framework import status


def is_guru(user):
    return user.groups.filter(name='Guru').exists()

@api_view(['GET'])
def get_jadwals(request,username):
    try:
        user = CustomUser.objects.get(username=username)
        if is_guru(user):
            jadwals = Jadwal.objects.all().filter(guru=user)
            serializer = JadwalSerializer(jadwals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_jadwal(request, pk):
    jadwal = Jadwal.objects.get(id=pk)
    serializer = JadwalSerializer(jadwal, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_jadwal(request):
    try:
        data = request.data
        jadwal = Jadwal.objects.create(
            title = data["title"],
            kelas = data["kelas"],
            day = data["day"],
            start = data["start"],
            end = data["end"],
            link = data["link"],
            desc = data["desc"],
            guru = CustomUser.objects.get(username=data["guru"])
        )
        serializer = JadwalSerializer(jadwal, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_jadwal(request, pk):
    try:
        data = request.data
        jadwal = Jadwal(
            id = pk,
            title = data["title"],
            kelas = data["kelas"],
            day = data["day"],
            start = data["start"],
            end = data["end"],
            link = data["link"],
            desc = data["desc"],
            guru = CustomUser.objects.get(username=data["guru"])
        )
        jadwal.save()
        serializer = JadwalSerializer(jadwal, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# def jadwal_json(request):
#     obj = Jadwal.objects.all()
#     data = serializers.serialize('json', list(obj), fields=('title','kelas', 'link', 'day'))
#     return HttpResponse(data, content_type="application/json")
    
# def add_jadwal(request):
#     if not is_guru(request.user):
#         return JsonResponse({"status": "error"}, status=401)

#     if request.method == 'POST':
#         data = json.loads(request.body)
#         form = JadwalForm()
        
#         form.day = data["day"]
#         form.start = data["start"]
#         form.end = data["end"]
#         form.link = data["link"]
#         form.kelas = data["kelas"]
#         form.title = data["title"]
#         form.desc = data["desc"]
#         form.guru = request.user

#         form.save()

#         return JsonResponse({"status": "success"}, status=200)
#     else:
#         return JsonResponse({"status": "error"}, status=401)

# def update_jadwal(request):
#     if not is_guru(request.user):
#         return JsonResponse({"status": "error"}, status=401)

#     if request.method == 'POST':
#         data = json.loads(request.body)
#         jadwal = Jadwal.objects.all().filter(guru=request.user)
#         obj = jadwal.filter(id=data['id']).first()

#         if not obj:
#             return JsonResponse({"status": "error"}, status=401)

#         form = JadwalForm(instance=obj)
        
#         form.day = data["day"]
#         form.start = data["start"]
#         form.end = data["end"]
#         form.link = data["link"]
#         form.kelas = data["kelas"]
#         form.title = data["title"]
#         form.desc = data["desc"]
#         form.guru = request.user

#         form.save()

#         return JsonResponse({"status": "success"}, status=200)
#     else:
#         return JsonResponse({"status": "error"}, status=401)

@login_required(login_url='/pendaftaranguru/')
def jadwal(request, pk = None):
    if not is_guru(request.user):
        return render(request, 'jadwal.html', {'is_guru':False})
    
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

    return render(request, 'jadwal.html', {'is_guru':True, 'form':form, 'jadwal': jadwal, 'obj':obj, 'edit':edit})

def filter_jadwal(request):
    kelas=request.GET.getlist('kelas[]')
    jadwal=Jadwal.objects.all().filter(guru=request.user)
    if len(kelas)>0:
        jadwal=jadwal.filter(kelas__in=kelas).distinct()
        
    t=render_to_string('jadwal_card.html',{'jadwal':jadwal})
    return JsonResponse({'data':t})

