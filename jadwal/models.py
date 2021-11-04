import uuid
from django.db import models

class Jadwal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    DAY_CHOICES = [('Senin','Senin'), ('Selasa','Selasa'), ('Rabu','Rabu'), ('Kamis','Kamis'), ('Jumat', 'Jumat'), ('Sabtu', 'Sabtu'), ('Minggu', 'Minggu')]
    day = models.CharField(max_length = 10, choices=DAY_CHOICES)
    start = models.TimeField()
    end = models.TimeField()
    link = models.URLField()
    KELAS_CHOICES = [('10','10'), ('11','11'), ('12','12')]
    kelas = models.CharField(max_length = 10, choices=KELAS_CHOICES)
    title = models.CharField(max_length = 50, unique=True)
    desc = models.CharField(max_length = 250, blank=True)
    # foreign key ke teacher
