from django.db import models
from userauth.models import CustomUser
# Create your models here.

class Booking(models.Model):
    # guru = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    siswa = models.ForeignKey(CustomUser, on_delete=models.CASCADE)