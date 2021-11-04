from django.forms import ModelForm, TimeInput, Textarea
from .models import Jadwal

class JadwalForm(ModelForm):
    class Meta:
        model = Jadwal
        fields = ['day', 'start', 'end', 'link', 'kelas', 'desc', 'title']
        widgets = {
            'start': TimeInput(format='%H:%M'),
            'end': TimeInput(format='%H:%M'),
            'title': Textarea(attrs={'class': "form-control"})
        }