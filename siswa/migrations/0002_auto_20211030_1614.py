# Generated by Django 3.2.8 on 2021-10-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siswa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['nama_lengkap', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'kelas', 'mata_pelajaran', 'payment', 'agree']},
        ),
        migrations.AddField(
            model_name='customuser',
            name='agree',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='alamat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='jenis_kelamin',
            field=models.CharField(blank=True, choices=[('p', 'pria'), ('w', 'wanita')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='kelas',
            field=models.CharField(blank=True, choices=[('1', '10'), ('2', '11'), ('3', '12')], max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='mata_pelajaran',
            field=models.CharField(blank=True, choices=[('MTK', 'Matematika'), ('Fis', 'Fisika'), ('Bio', 'Biologi'), ('Kim', 'Kimia'), ('B.Indo', 'B.Indonesia'), ('B.Ing', 'B.Inggris'), ('Eko', 'Ekonomi'), ('Geo', 'Geografi'), ('Sosio', 'Sosiologi'), ('Sejarah', 'Sejarah')], max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nama_lengkap',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='payment',
            field=models.CharField(blank=True, choices=[('CASH', 'Cash'), ('CHECK', 'Check'), ('CARD', 'Card')], default='Card', max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tanggal_lahir',
            field=models.DateField(blank=True, null=True),
        ),
    ]