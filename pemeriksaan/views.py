from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from datetime import date
import random
import string

from pasien.models import *
from hasil_pemeriksaan.models import *
from uji_lab.models import *
from bidang.models import *
from nilai_normal.models import *
from .models import *


def uid_generator():
    random_string = ''.join(random.choices(string.ascii_uppercase, k=5))
    count = Pemeriksaan.objects.all().count()
    tmp = "CK" + str(count) + random_string
    return tmp

def uid_generator_hasil(count):
    random_string = ''.join(random.choices(string.ascii_uppercase, k=4))
    tmp = "HP" + str(count) + random_string
    return tmp

# Create your views here.
response ={'lab_name' : 'citra'}
def add_pemeriksaan(request):
    daftar_lab = []
    if request.method == 'POST':
        pid = uid_generator()
        id_pasien = request.POST.get("uid")
        id_bidang = request.POST.get("id_bidang")
        id_dokter = request.POST.get("id_dokter")
        id_tester = request.POST.get("id_tester")
        tanggal_pemeriksaan = date.today()
        daftar_lab = request.POST.getlist("uji_lab")
        count = 0
        total = 0
        for x in daftar_lab:
            obj = UjiLab.objects.get(uid=x)
            hpid = uid_generator_hasil(count)
            id_pemeriksaan = pid
            nama_uji_lab = obj.nama
            hasil = ""
            satuan = obj.satuan
            nilai_normal = ""
            model = HasilPemeriksaan(hpid=hpid, id_pemeriksaan=id_pemeriksaan,nama_uji_lab=nama_uji_lab,hasil=hasil,satuan=satuan,nilai_normal=nilai_normal)
            model.save()
            count = count + 1
            total = total + int(obj.harga)
        total_biaya = total
        status = "On Proses"
        diagnosa_awal = request.POST.get("diagnosa")
        submit = Pemeriksaan(pid=pid, id_pasien=id_pasien, id_bidang=id_bidang,id_dokter=id_dokter, id_tester=id_tester, tanggal_pemeriksaan=tanggal_pemeriksaan,total_biaya=total_biaya, diagnosa_awal=diagnosa_awal, status=status)
        submit.save()        
    return HttpResponseRedirect(reverse('pasien:all_pasien'))

def delete_pemeriksaan(request, id):
    return render(request, 'index.html', response)

def all_pemeriksaan(request):
    pemeriksaan = Pemeriksaan.objects.filter(status="On Proses")
    flag_null = True
    if pemeriksaan.count() != 0:
        flag_null = False
    response['flag_null'] = flag_null
    response["datas"] = pemeriksaan
    return render(request, 'lp_pemeriksaan_aktif.html', response)

def edit_pemeriksaan(request, id):
    return render(request, 'index.html', response)

def view_pemeriksaan(request, id):
    tmp = Pemeriksaan.objects.get(pid=id)
    person = Pasien.objects.get(uid=tmp.id_pasien)
    data = HasilPemeriksaan.objects.filter(id_pemeriksaan=id)
    nama_bidang = Bidang.objects.get(uid=tmp.id_bidang).nama
    response["datas"] = data
    response["person"] = person
    response["pemeriksaan"] = tmp
    response["nama_bidang"] = nama_bidang
    return render(request, 'lp_pemeriksaan.html', response)
