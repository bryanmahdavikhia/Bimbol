from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    nama_lengkap = models.CharField(max_length=100, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    # phone_regex = RegexValidator(regex=r"^\+")

    JENIS_KELAMIN_CHOICES = [('p', 'pria'), ('w', 'wanita')]
    jenis_kelamin = models.CharField(max_length=30, choices=JENIS_KELAMIN_CHOICES, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    agree = models.BooleanField(default=False)

    KELAS_CHOICES = [('1', '10'), ('2', '11'), ('3', '12')]
    kelas = models.CharField(max_length=225, choices=KELAS_CHOICES, blank=True, null=True)

    MATA_PELAJARAN_CHOICES = [
    ('MTK', 'Matematika'),
    ('Fis', 'Fisika'), 
    ('Bio', 'Biologi'),
    ('Kim', 'Kimia'),
    ('B.Indo', 'B.Indonesia'), 
    ('B.Ing', 'B.Inggris'), 
    ('Eko', 'Ekonomi'), 
    ('Geo', 'Geografi'),
    ('Sosio', 'Sosiologi'),
    ('Sejarah', 'Sejarah'),
    ]
    mata_pelajaran = models.CharField(max_length=225, choices=MATA_PELAJARAN_CHOICES, blank=True, null=True)

    PAYMENT_CHOICES=[('CASH','Cash'), ('CHECK','Check'), ('CARD','Card')]
    payment = models.CharField(max_length=225, choices=PAYMENT_CHOICES, default='Card', blank=True, null=True)

    class Meta:
        ordering = ['nama_lengkap', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'kelas', 'mata_pelajaran', 'payment', 'agree']

    def __str__(self):
        return self.username
