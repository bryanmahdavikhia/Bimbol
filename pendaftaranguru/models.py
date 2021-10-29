from django.db import models

# Create your models here.
class GuruUser(models.Model):
    nama_lengkap = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    nomor_telefon = models.CharField(max_length=100, default='')
    tanggal_lahir = models.DateField(default="1961-01-01")

    JENIS_KELAMIN_CHOICES = [('p', 'pria'), ('w', 'wanita')]
    jenis_kelamin = models.CharField(choices=JENIS_KELAMIN_CHOICES, max_length=100, default='')
    alamat = models.TextField(max_length=140, default='')

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
    mata_pelajaran = models.CharField(max_length=225, choices=MATA_PELAJARAN_CHOICES)

    validasi_guru = models.FileField()
    #foto_guru = models.ImageField()
    aggree = models.BooleanField(default=False)

    def __str__(self):
        return (self.nama_lengkap)