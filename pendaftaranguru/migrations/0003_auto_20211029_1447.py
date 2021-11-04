# Generated by Django 3.2.8 on 2021-10-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaranguru', '0002_auto_20211029_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userguru',
            name='jenis_kelamin',
            field=models.CharField(choices=[('pria', 'pria'), ('wanita', 'wanita')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userguru',
            name='kelas',
            field=models.CharField(choices=[('10', '10'), ('11', '11'), ('12', '12')], default='10', max_length=225),
        ),
        migrations.AlterField(
            model_name='userguru',
            name='mata_pelajaran',
            field=models.CharField(choices=[('Matematika', 'Matematika'), ('Fisika', 'Fisika'), ('Biologi', 'Biologi'), ('Kimia', 'Kimia'), ('B.Indonesia', 'B.Indonesia'), ('B.Inggris', 'B.Inggris'), ('Ekonomi', 'Ekonomi'), ('Geografi', 'Geografi'), ('Sosiologi', 'Sosiologi'), ('Sejarah', 'Sejarah')], max_length=225),
        ),
    ]
