from django.db import models

# Create your models here.
class Tester(models.Model):
    kode = models.CharField(max_length=100)
    nama = models.CharField(max_length=150)