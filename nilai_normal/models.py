from django.db import models

# Create your models here.
class NilaiNormal(models.Model):
    nilai_normal = models.CharField(max_length=100)
    nama_pemeriksaan = models.CharField(max_length=150)
    kategori = models.CharField(max_length=150)
    jenis_kelamin = models.CharField(max_length=50)
    