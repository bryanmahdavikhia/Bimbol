from django.db import models

# Create your models here.

#ToDo : Create 'Note' model that contains to, from, title, and message
class Saran(models.Model):
    Message = models.TextField()
