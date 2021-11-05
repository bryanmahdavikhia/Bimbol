from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True, default="")
    username = models.CharField(max_length=30, unique=True, default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    nama_lengkap = models.CharField(max_length=100, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    # phone_regex = RegexValidator(regex=r"^\+")

    JENIS_KELAMIN_CHOICES = [('p', 'pria'), ('w', 'wanita')]
    jenis_kelamin = models.CharField(max_length=30, choices=JENIS_KELAMIN_CHOICES, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    agree = models.BooleanField(default=False)

    KELAS_CHOICES = [('1', '10'), ('2', '11'), ('3', '12')]
    kelas = models.CharField(max_length=225, choices=KELAS_CHOICES)

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
    mata_pelajaran = models.CharField(max_length=225)
    # , choices=MATA_PELAJARAN_CHOICES, blank=True, null=True)

    PAYMENT_CHOICES=[('CASH','Cash'), ('CHECK','Check'), ('CARD','Card')]
    payment = models.CharField(max_length=225, choices=PAYMENT_CHOICES, default='Card')

    validasi_guru = models.FileField()
    nomor_telefon = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ['nama_lengkap', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'kelas', 'mata_pelajaran', 'payment', 'validasi_guru', 'nomor_telefon', 'agree']

    def __str__(self):
        return self.username




# # from typing_extensions import Required
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # from django.core.validators import RegexValidator

# class CustomUser(AbstractUser):
#     nama_lengkap = models.CharField(max_length=100, blank=True, null=True)
#     tanggal_lahir = models.DateField(blank=True, null=True)
#     # phone_regex = RegexValidator(regex=r"^\+")

#     JENIS_KELAMIN_CHOICES = [('pria', 'pria'), ('wanita', 'wanita')]
#     jenis_kelamin = models.CharField(max_length=30, choices=JENIS_KELAMIN_CHOICES, blank=True, null=True)
#     alamat = models.TextField(blank=True, null=True)
#     agree = models.BooleanField(default=False)

#     KELAS_CHOICES = [('10', '10'), ('11', '11'), ('12', '12')]
#     kelas = models.CharField(max_length=225, choices=KELAS_CHOICES)

#     MATA_PELAJARAN_CHOICES = [
#     ('Matematika', 'Matematika'),
#     ('Fisika', 'Fisika'), 
#     ('Biologi', 'Biologi'),
#     ('Kimia', 'Kimia'),
#     ('B.Indonesia', 'B.Indonesia'), 
#     ('B.Inggris', 'B.Inggris'), 
#     ('Ekonomi', 'Ekonomi'), 
#     ('Geografi', 'Geografi'),
#     ('Sosiologi', 'Sosiologi'),
#     ('Sejarah', 'Sejarah'),
#     ]
#     mata_pelajaran = models.CharField(max_length=225)
#     # , choices=MATA_PELAJARAN_CHOICES, blank=True, null=True)

#     PAYMENT_CHOICES=[('CASH','Cash'), ('CHECK','Check'), ('CARD','Card')]
#     payment = models.CharField(max_length=225, choices=PAYMENT_CHOICES, default='Card')

#     validasi_guru = models.FileField()
#     nomor_telefon = models.CharField(max_length=100, default='')

#     class Meta:
#         ordering = ['nama_lengkap', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'kelas', 'mata_pelajaran', 'payment', 'validasi_guru', 'nomor_telefon', 'agree']

#     def __str__(self):
#         return self.username



