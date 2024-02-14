from django.db import models

# Create your models here.
class UjiLab(models.Model):
    uid = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    satuan = models.CharField(max_length=250)
    id_bidang = models.CharField(max_length=100)
    harga = models.IntegerField(default=0)