from django.db import models

# Create your models here.
class UjiLab(models.Model):
    uid = models.CharField(max_length=100)
    users = models.CharField(max_length=50)
    diagnosa_awal = models.CharField(max_length=250)
    tanggal_pemeriksaan = models.DateField()
    testers = models.CharField(max_length=50)