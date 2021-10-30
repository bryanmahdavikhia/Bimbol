from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class SiswaManager(BaseUserManager):
     def create_user(self, email, username, nama_lengkap, tanggal_lahir, jenis_kelamin, alamat, agree, kelas, mata_pelajaran, payment, password=None):

        if not email:
            raise ValueError('You must provide an email address')
        if not username:
            raise ValueError('You must have username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            nama_lengkap=nama_lengkap,
            tanggal_lahir=tanggal_lahir,
            jenis_kelamin=jenis_kelamin,
            alamat=alamat,
            agree=agree,
            kelas=kelas,
            mata_pelajaran=mata_pelajaran,
            payment=payment,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        
     def create_superuser(self, email,  username, nama_lengkap, tanggal_lahir, jenis_kelamin, alamat, agree, kelas, mata_pelajaran, payment, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            nama_lengkap=nama_lengkap,
            tanggal_lahir=tanggal_lahir,
            jenis_kelamin=jenis_kelamin,
            alamat=alamat,
            agree=agree,
            kelas=kelas,
            mata_pelajaran=mata_pelajaran,
            payment=payment,
            is_superuser = True,
        )

        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user

        
#         def has_module_perms(self, app_label):
#             return self.is_superuser
        
# def has_perm(self, perm, obj=None):
#         return self.is_superuser

       
        

class SiswaModel(AbstractBaseUser):
    email 				= models.EmailField(unique=True, verbose_name='email', max_length=60)
    username 				= models.CharField(max_length=30, unique=True)
    date_joined			= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)
	# first_name 				= models.CharField(max_length=30)
    nama_lengkap = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()

    JENIS_KELAMIN_CHOICES = [('p', 'pria'), ('w', 'wanita')]
    jenis_kelamin = models.CharField(max_length=30, choices=JENIS_KELAMIN_CHOICES)
    alamat = models.TextField()
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
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nama_lengkap', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'agree', 'kelas', 'mata_pelajaran', 'payment']
    
    objects = SiswaManager()
    
    
    def __str__(self):
         return self.email
         
    def has_perm(self, perm, obj=None):
         self.is_admin

    def has_module_perms(self, app_label):
         return True


# class SiswaModel(models.Model):
#     nama_lengkap = models.CharField(max_length=100),
#     email = models.EmailField('User Email'),
#     tanggal_lahir = models.DateField(),

#     JENIS_KELAMIN_CHOICES = [('p', 'pria'), ('w', 'wanita')]
#     jenis_kelamin = models.CharField(choices=JENIS_KELAMIN_CHOICES),
#     alamat = models.TextField(),
#     agree = models.BooleanField(default=False)

#     KELAS_CHOICES = [('1', '10'), ('2', '11'), ('3', '12')]
#     kelas = models.CharField(max_length=225, choices=KELAS_CHOICES, default='10')

#     MATA_PELAJARAN_CHOICES = [
#     ('MTK', 'Matematika'),
#     ('Fis', 'Fisika'), 
#     ('Bio', 'Biologi'),
#     ('Kim', 'Kimia'),
#     ('B.Indo', 'B.Indonesia'), 
#     ('B.Ing', 'B.Inggris'), 
#     ('Eko', 'Ekonomi'), 
#     ('Geo', 'Geografi'),
#     ('Sosio', 'Sosiologi'),
#     ('Sejarah', 'Sejarah'),
#     ]
#     mata_pelajaran = models.CharField(max_length=225, choices=MATA_PELAJARAN_CHOICES, default=None)

#     PAYMENT_CHOICES=[('CASH','Cash'), ('CHECK','Check'), ('CARD','Card')]
#     payment = models.CharField(max_length=225, choices=PAYMENT_CHOICES, default='Card')


#     def __str__(self):
#         return (self.nama_lengkap),