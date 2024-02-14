from django.db import models

# Create your models here.
class Bidang(models.Model):
    uid = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
