from django.db import models

# Create your models here.
class GuruUser(models.Model):
    nama_lengkap = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    nomor_telefon = models.CharField(max_length=100, default='')
    tanggal_lahir = models.DateField(default="1961-01-01")

    JENIS_KELAMIN_CHOICES = [('pria', 'pria'), ('wanita', 'wanita')]
    jenis_kelamin = models.CharField(choices=JENIS_KELAMIN_CHOICES, max_length=100, default='')
    alamat = models.TextField(max_length=140, default='')

    KELAS_CHOICES = [('10', '10'), ('11', '11'), ('12', '12')]
    kelas = models.CharField(max_length=225, choices=KELAS_CHOICES, default='10')

    MATA_PELAJARAN_CHOICES = [
    ('Matematika', 'Matematika'),
    ('Fisika', 'Fisika'), 
    ('Biologi', 'Biologi'),
    ('Kimia', 'Kimia'),
    ('B.Indonesia', 'B.Indonesia'), 
    ('B.Inggris', 'B.Inggris'), 
    ('Ekonomi', 'Ekonomi'), 
    ('Geografi', 'Geografi'),
    ('Sosiologi', 'Sosiologi'),
    ('Sejarah', 'Sejarah'),
    ]
    mata_pelajaran = models.CharField(max_length=225, choices=MATA_PELAJARAN_CHOICES)

    validasi_guru = models.FileField()
    #foto_guru = models.ImageField()
    aggree = models.BooleanField(default=False)

    def __str__(self):
        return (self.nama_lengkap)