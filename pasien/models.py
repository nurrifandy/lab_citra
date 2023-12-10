from django.db import models

# Create your models here.
class Pasien(models.Model):
    uid = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    umur = models.CharField(max_length=50)
    jenis_kelamin = models.BooleanField()
    alamat = models.CharField(max_length=250)
    tanggal_mendaftar = models.DateField()