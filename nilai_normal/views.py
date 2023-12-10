from django.shortcuts import render
from .models import *


# Create your views here.
response ={'lab_name' : 'citra'}
def index(request):
    return render(request, 'index.html')

def tambah_nilai_normal(request):
    if request.method == 'POST':
        nilai_normal = request.POST.get('nilai_normal')
        nama_pemeriksaan = request.POST.get('nama_pemeriksaan')
        kategori = request.POST.get('kategori')
        jenis_kelamin = request.POST.get('jenis_kelamin')
        model = NilaiNormal(nilai_normal=nilai_normal, nama_pemeriksaan=nama_pemeriksaan, kategori=kategori, jenis_kelamin=jenis_kelamin)
        model.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def daftar_nilai_normal(request):
    data_nilai_normal = NilaiNormal.objects.all()
    response = {"datas" : data_nilai_normal}
    return render(request, 'index.html',response)