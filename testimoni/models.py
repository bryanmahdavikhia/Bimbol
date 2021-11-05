from django.db import models

# Create your models here.
class Testimoni(models.Model):

    nama = models.CharField(max_length=100)

    PILIHAN_KELAS = [
        ('10 IPA', '10 IPA'), 
        ('10 IPS', '10 IPS'), 
        ('11 IPA', '11 IPA'), 
        ('11 IPS', '11 IPS'),
        ('12 IPA', '12 IPA'),
        ('12 IPS', '12 IPS')
        ]
    kelas = models.CharField(max_length=100, choices=PILIHAN_KELAS)

    testimoni = models.TextField()


