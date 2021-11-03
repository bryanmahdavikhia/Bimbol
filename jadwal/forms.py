from django.forms import ModelForm, TimeInput
from .models import Jadwal

class JadwalForm(ModelForm):
    class Meta:
        model = Jadwal
        fields = ['day', 'start', 'end', 'link', 'kelas', 'desc']
        widgets = {
            'start': TimeInput(format='%H:%M'),
            'end': TimeInput(format='%H:%M'),
        }