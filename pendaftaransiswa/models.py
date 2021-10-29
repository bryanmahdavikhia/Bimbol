from django.db import models

# Create your models here.

class SiswaUser(models.Model):
    nama_lengkap = models.CharField(max_length=100),
    email = models.EmailField('User Email'),
    tanggal_lahir = models.DateField(),

    JENIS_KELAMIN_CHOICES = [('p', 'pria'), ('w', 'wanita')]
    jenis_kelamin = models.CharField(choices=JENIS_KELAMIN_CHOICES),
    alamat = models.TextField(),
    agree = models.BooleanField(default=False)

    KELAS_CHOICES = [('1', '10'), ('2', '11'), ('3', '12')]
    kelas = models.CharField(max_length=225, choices=KELAS_CHOICES, default='10')

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
    mata_pelajaran = models.CharField(max_length=225, choices=MATA_PELAJARAN_CHOICES, default=None)

    PAYMENT_CHOICES=[('CASH','Cash'), ('CHECK','Check'), ('CARD','Card')]
    payment = models.CharField(max_length=225, choices=PAYMENT_CHOICES, default='Card')


    def __str__(self):
        return (self.nama_lengkap),