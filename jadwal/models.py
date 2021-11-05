import uuid
from django.db import models
from django.contrib.auth.models import User
from userauth.models import CustomUser


class Jadwal(models.Model):
    DAY_CHOICES = [('Senin','Senin'), ('Selasa','Selasa'), ('Rabu','Rabu'), ('Kamis','Kamis'), ('Jumat', 'Jumat'), ('Sabtu', 'Sabtu'), ('Minggu', 'Minggu')]
    day = models.CharField(max_length = 10, choices=DAY_CHOICES)
    start = models.TimeField()
    end = models.TimeField()
    link = models.URLField()
    KELAS_CHOICES = [('10','10'), ('11','11'), ('12','12')]
    kelas = models.CharField(max_length = 10, choices=KELAS_CHOICES)
    title = models.CharField(max_length = 50)
    desc = models.CharField(max_length = 250, blank=True)
    guru = models.ForeignKey(CustomUser, on_delete=models.CASCADE)# foreign key ke teacher

