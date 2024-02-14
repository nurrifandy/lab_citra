from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *

from uji_lab.models import *

# Create your views here.
response ={'lab_name' : 'citra'}
def index(request):
    return render(request, 'index.html')

def add_nilai_normal(request):
    nilai_normal = NilaiNormal.objects.all()
    tmp = nilai_normal.count()+1
    if request.method == 'POST':
        idn = "NNL" + str(tmp)
        nilai_normal = request.POST.get('nilai_normal')
        data = UjiLab.objects.get(uid = request.POST.get('id_pemeriksaan'))
        nama_pemeriksaan = data.nama
        kategori = request.POST.get('kategori')
        jenis_kelamin = request.POST.get('jenis_kelamin')
        satuan = request.POST.get('satuan')
        model = NilaiNormal(idn=idn,nilai_normal=nilai_normal,id_uji_lab=data.uid,nama_pemeriksaan=nama_pemeriksaan, kategori=kategori, jenis_kelamin=jenis_kelamin, satuan=satuan)
        model.save()
    return HttpResponseRedirect(reverse('nilai_normal:all_nilai_normal'))

def all_nilai_normal(request):
    data = NilaiNormal.objects.all()
    data2 = UjiLab.objects.all()
    flag_null = True
    if data.count() != 0:
        flag_null = False
    response["datas"] = data
    response["labs"] = data2
    response["flag_null"] = flag_null
    return render(request, 'lp_nilai_normal.html',response)

def edit_nilai_normal(request, id):
    obj = NilaiNormal.objects.get(idn=id)
    if request.method == 'POST':
        obj.nilai_normal = request.POST.get('nilai_normal')
        data = UjiLab.objects.get(uid = request.POST.get('id_pemeriksaan'))
        obj.nama_pemeriksaan = data.nama
        obj.id_uji_lab = data.uid
        obj.kategori = request.POST.get('kategori')
        obj.jenis_kelamin = request.POST.get('jenis_kelamin')
        obj.satuan = request.POST.get('satuan')
        obj.save()
    return HttpResponseRedirect(reverse('nilai_normal:all_nilai_normal'))

# function untuk menghapus tester
def delete_nilai_normal(request, id=None):
    obj_tester = Tester.objects.get(id=1)
    obj_tester.delete()
    return render(render, 'index.html')