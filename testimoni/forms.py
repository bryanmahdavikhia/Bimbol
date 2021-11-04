from django import forms
from django.forms import fields
from .models import Testimoni

class TestimoniForm (forms.ModelForm):

    nama = forms.CharField(
        label='Nama Lengkap', 
        widget=forms.TextInput(attrs={'placeholder': 'Isi dengan nama lengkap', 'class':'form-control'})
    )

    kelas = forms.ChoiceField(
        label='Kelas', 
		choices=Testimoni.PILIHAN_KELAS,
        widget=forms.Select(attrs={ 'class':'form-control'})
    )

    testimoni = forms.CharField(
        label='Testimoni', 
        widget=forms.Textarea(attrs={'placeholder': 'Ceritakan pengalaman anda disini', 'class':'form-control'})
    )

    class Meta:
        model = Testimoni
        fields = '__all__'