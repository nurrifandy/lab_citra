from django.db import models

# Create your models here.
class HasilPemeriksaan(models.Model):
    hpid = models.CharField(max_length=100)
    id_pemeriksaan = models.CharField(max_length=100)
    nama_uji_lab = models.CharField(max_length=100)
    hasil = models.CharField(max_length=100)
    satuan = models.CharField(max_length=100)
    nilai_normal = models.CharField(max_length=50)
    # id_uji_lab