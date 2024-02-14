from django.db import models

# Create your models here.
class NilaiNormal(models.Model):
    idn = models.CharField(max_length=50)
    id_uji_lab = models.CharField(max_length=50)
    nilai_normal = models.CharField(max_length=100)
    nama_pemeriksaan = models.CharField(max_length=150)
    kategori = models.CharField(max_length=150)
    jenis_kelamin = models.CharField(max_length=50)
    satuan = models.CharField(max_length=150)
    # need id bidang