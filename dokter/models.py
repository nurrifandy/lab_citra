from django.db import models

# Create your models here.
class Dokter(models.Model):
    kode_dokter = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    komisi_belum_dibayar = models.IntegerField(default=0)
    komisi_sudah_dibayar = models.IntegerField(default=0)