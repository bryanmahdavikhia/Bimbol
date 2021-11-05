# Generated by Django 3.2.9 on 2021-11-05 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_alter_customuser_alamat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='payment',
            field=models.CharField(choices=[('CASH', 'Cash'), ('CHECK', 'Check'), ('CARD', 'Card')], default='Card', max_length=100),
        ),
    ]
