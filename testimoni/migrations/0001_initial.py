# Generated by Django 3.2.9 on 2021-12-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimoni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('kelas', models.CharField(choices=[('10 IPA', '10 IPA'), ('10 IPS', '10 IPS'), ('11 IPA', '11 IPA'), ('11 IPS', '11 IPS'), ('12 IPA', '12 IPA'), ('12 IPS', '12 IPS')], max_length=100)),
                ('testimoni', models.TextField()),
            ],
        ),
    ]
