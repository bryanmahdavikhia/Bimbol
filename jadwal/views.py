from django.shortcuts import render

# Create your views here.
from .models import Jadwal
from .forms import JadwalForm
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.core import serializers

def index(request):
    jadwal = Jadwal.objects.all()  # TODO Implement this
    response = {'jadwal': jadwal}
    return render(request, 'jadwal.html', response)

def jadwal_json(request):
    data = serializers.serialize('json', Jadwal.objects.all())
    return HttpResponse(data, content_type="application/json")

# def add_note(request):
#     failed = False
#     if request.method == 'POST':
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/lab-4')
#         else:
#             failed = True
    
#     form = NoteForm()
#     return render(request, 'lab4_form.html', {'form':form, 'failed':failed})

# def note_list(request):
#     notes = Note.objects.all()  # TODO Implement this
#     response = {'notes': notes}
#     return render(request, 'lab4_note_list.html', response)