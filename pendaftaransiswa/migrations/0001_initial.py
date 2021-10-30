# Generated by Django 3.2.8 on 2021-10-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiswaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('nama_lengkap', models.CharField(max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('jenis_kelamin', models.CharField(choices=[('p', 'pria'), ('w', 'wanita')], max_length=30)),
                ('alamat', models.TextField()),
                ('agree', models.BooleanField(default=False)),
                ('kelas', models.CharField(choices=[('1', '10'), ('2', '11'), ('3', '12')], default='10', max_length=225)),
                ('mata_pelajaran', models.CharField(choices=[('MTK', 'Matematika'), ('Fis', 'Fisika'), ('Bio', 'Biologi'), ('Kim', 'Kimia'), ('B.Indo', 'B.Indonesia'), ('B.Ing', 'B.Inggris'), ('Eko', 'Ekonomi'), ('Geo', 'Geografi'), ('Sosio', 'Sosiologi'), ('Sejarah', 'Sejarah')], default=None, max_length=225)),
                ('payment', models.CharField(choices=[('CASH', 'Cash'), ('CHECK', 'Check'), ('CARD', 'Card')], default='Card', max_length=225)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
