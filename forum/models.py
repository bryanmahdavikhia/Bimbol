from django.db import models

# Create your models here.
class Forum(models.Model):
    Title = models.CharField(max_length=50)
