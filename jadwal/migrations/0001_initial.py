# Generated by Django 3.2.9 on 2021-11-04 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'), ('Kamis', 'Kamis'), ('Jumat', 'Jumat'), ('Sabtu', 'Sabtu'), ('Minggu', 'Minggu')], max_length=10)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('link', models.URLField()),
                ('kelas', models.CharField(choices=[('10', '10'), ('11', '11'), ('12', '12')], max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]
