from django.db import models

# Create your models here.
class Tester(models.Model):
    kode = models.CharField(max_length=100)
    nama = models.CharField(max_length=150)
    pemeriksaan_on_proses = models.IntegerField(default=0)
    pemeriksaan_selesai = models.IntegerField(default=0)
    total_pemeriksaan = models.IntegerField(default=0)