from django.db import models

# Create your models here.
class Pemeriksaan(models.Model):
    pid = models.CharField(max_length=100)
    id_pasien = models.CharField(max_length=100)
    id_bidang = models.CharField(max_length=100)
    id_dokter = models.CharField(max_length=100)
    id_tester = models.CharField(max_length=100)
    tanggal_pemeriksaan = models.DateField()
    total_biaya = models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    diagnosa_awal = models.CharField(max_length=250)