from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *
from datetime import date
from django.utils.dateparse import parse_date
import random
import string
from uji_lab.models import *
from pemeriksaan.models import *
from dokter.models import *
from tester.models import *
from bidang.models import *
from json import dumps
from django.core import serializers
import json

'''

'''

# Register Pasien Views.
response ={'lab_name' : 'citra'}

def calculate_age(birthdate):
    tmp = parse_date(birthdate)
    today = date.today()
    age = today.year - tmp.year - ((today.month, today.day) < (tmp.month, tmp.day))
    return age

def uid_generator():
    random_string = ''.join(random.choices(string.ascii_uppercase, k=5))
    count = Pasien.objects.all().count()
    tmp = "LC" + str(count) + random_string
    return tmp

def add_pasien(request):
    # get register form
    if request.method == 'POST':
        uid = uid_generator()
        nama = request.POST.get("nama")
        tanggal_lahir = request.POST.get("tanggal_lahir")
        umur = calculate_age(tanggal_lahir)
        jenis_kelamin = None
        if request.POST.get("jenis_kelamin") == "true":
            jenis_kelamin = True
        else:
            jenis_kelamin = False
        alamat = request.POST.get("alamat")
        tanggal_mendaftar = date.today()
        diagnosa_awal = "None"
        model = Pasien(uid=uid, nama=nama, tanggal_lahir = tanggal_lahir, umur=umur, jenis_kelamin=jenis_kelamin, alamat=alamat, tanggal_mendaftar=tanggal_mendaftar, diagnosa_awal=diagnosa_awal)
        model.save()
    return HttpResponseRedirect(reverse('pasien:all_pasien'))


# List pasien views
def all_pasien(request):
    data_pasien = Pasien.objects.all()
    flag_null = True
    if data_pasien.count() != 0:
        flag_null = False
    response['flag_null'] = flag_null
    response['data_pasien'] = data_pasien
    return render(request, 'lp_pasien.html', response)

# Edit pasien views
def edit_pasien(request, id):
    person = Pasien.objects.get(uid=id)
    edit_success =True
    return render(request, 'main.html', response)


# Arsipkan pasien views
def delete_pasien(request, id):
    person = Pasien.objects.get(uid=1)
    delete_success = True
    return render(request, 'main.html', response)


# View profile views
def view_pasien(request, id):
    person = Pasien.objects.get(uid=id)
    pemeriksaan = Pemeriksaan.objects.filter(id_pasien=id)
    bidang = Bidang.objects.all()
    dokter = Dokter.objects.all()
    tester = Tester.objects.all()
    
    for tmp in bidang:
        uji_lab = UjiLab.objects.filter(id_bidang = tmp.uid)
        # create json
        tmpJson = serializers.serialize("json",uji_lab)
        tmpObj = json.loads(tmpJson)
        response[tmp.uid] = dumps(tmpObj)
    response['person'] = person
    flag_null = True
    if pemeriksaan.count() != 0:
        flag_null = False
    # make json
    tmpJson2 = serializers.serialize("json",bidang)
    tmpObj2 = json.loads(tmpJson2)
    
    response["count"] = dumps(tmpObj2)
    response['flag_null'] = flag_null
    response['datas'] = pemeriksaan
    response['bidang'] = bidang
    response['dokter'] = dokter
    response['tester'] = tester
    return render(request, 'lp_profile.html', response)
