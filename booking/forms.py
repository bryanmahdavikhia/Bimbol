from django import forms
from .models import Booking
from django.contrib.auth.models import Group
from userauth.models import CustomUser
class BookForm(forms.ModelForm):
<<<<<<< HEAD
    groupGuru = Group.objects.get(name='Guru')
    # gurunya = groupGuru.user_set.all()
    # guru = forms.ModelChoiceField(queryset=gurunya)
=======
>>>>>>> 17ed6aebf6caa6fb8355739b5ca8d6565a7bca8f

    TAHUN = range(2021, 2024, 1)
    selesai = forms.DateField(widget=forms.SelectDateWidget(
			attrs={'class':'form-group col-sm-2'}, years=TAHUN))

    class Meta():
        model = Booking
        fields = ['guru','selesai']