from django import forms
from .models import Saran

# Buat kelas untuk NoteForm menggunakan model Note
# Pastikan semua fields telah digunakan
class SaranForm(forms.ModelForm):
    class Meta:
        model = Saran
        fields = ['Message']