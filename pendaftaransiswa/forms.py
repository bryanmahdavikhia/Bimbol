from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.regex_helper import Choice
from . models import SiswaModel

class RegisterFormSiswa(UserCreationForm):
	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={'class':'form-control'}))

	nama_lengkap = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(
			attrs={'class':'form-control'}))

	TAHUN = range(1990, 2021, 1)
	tanggal_lahir = forms.DateField(
		widget=forms.SelectDateWidget(
			attrs={'class':'form-group col-sm-2'}, years=TAHUN))

	jenis_kelamin = forms.ChoiceField(
		label='Jenis Kelamin', 
		widget=forms.RadioSelect(), 
		choices=[('p', 'pria'), ('w', 'wanita')])

	alamat = forms.CharField(
		widget=forms.Textarea(
			attrs={'class':'form-control'}))

	agree = forms.BooleanField(
		label="Semua data yang saya masukan adalah benar")

	kelas = forms.ChoiceField(
		label='Kelas', 
		widget=forms.RadioSelect(), 
		choices=SiswaModel.KELAS_CHOICES)
	
	mata_pelajaran = forms.MultipleChoiceField(
		label='Mata Pelajaran', 
		widget=forms.CheckboxSelectMultiple(), 
		choices=SiswaModel.MATA_PELAJARAN_CHOICES)

	payment = forms.ChoiceField(
		label='Payment Details', 
		widget=forms.RadioSelect(), 
		choices=SiswaModel.PAYMENT_CHOICES)

	class Meta:
		model = SiswaModel
        # fields='__all__'
		fields = ('username', 'nama_lengkap', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'agree', 'kelas', 'mata_pelajaran', 'payment', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterFormSiswa, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

