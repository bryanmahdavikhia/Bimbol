from django.contrib.auth.forms import UserCreationForm
from userauth.models import CustomUser
from django import forms

class RegisterFormGuru(UserCreationForm):
	nama_lengkap = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(
			attrs={'class':'form-control'}))

	email = forms.EmailField(
		widget=forms.EmailInput(
			attrs={'class':'form-control'}))
	
	nomor_telefon = forms.CharField(
		max_length=100, 
		widget=forms.TextInput(
			attrs={'class':'form-control'}))

	TAHUN = range(1961, 2002, 1)
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
		choices=CustomUser.KELAS_CHOICES)
	
	mata_pelajaran = forms.ChoiceField(
		label='Mata Pelajaran', 
		widget=forms.RadioSelect(), 
		choices=CustomUser.MATA_PELAJARAN_CHOICES)
	
	validasi_guru = forms.FileField(
		widget=forms.FileInput(
			attrs={'class':'form-control'}))

	class Meta:
		model = CustomUser
		fields = ('username', 'nama_lengkap', 'nomor_telefon', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'agree', 'kelas', 'mata_pelajaran', 'email', 'password1', 'password2')

	
	def __init__(self, *args, **kwargs):
		super(RegisterFormGuru, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
	
	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = CustomUser.objects.get(email= email)
		except Exception as e:
			return email
		raise forms.ValidationError("Email {email} is already in use.")

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = CustomUser.objects.get(username=username)
		except Exception as e:
			return username
		raise forms.ValidationError("Username {username} is already in use.")

