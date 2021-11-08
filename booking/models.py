from django.db import models
from django.contrib.auth.models import Group
from userauth.models import CustomUser
from django.utils import timezone
# Create your models here.

class Booking(models.Model):
<<<<<<< HEAD
    groupGuru = Group.objects.get(name='Guru')
    groupSiswa = Group.objects.get(name='Siswa')
    gurunya = groupGuru.user_set.all()
    siswanya = groupSiswa.user_set.all()
=======
>>>>>>> 17ed6aebf6caa6fb8355739b5ca8d6565a7bca8f
    guru = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    selesai = models.DateField(blank=True, null=True)