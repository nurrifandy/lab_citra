from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from uji_lab.models import *
from bidang.models import *

# Create your views here.
response ={'lab_name' : 'citra'}
def add_uji_lab(request):
    uji = UjiLab.objects.all()
    tmp = uji.count()+1
    if request.method == 'POST':
        uid = 'ULCT' + str(tmp)
        nama = request.POST.get("nama")
        satuan = request.POST.get("satuan")
        print(request.POST.get("id_bidang"))
        id_bidang = request.POST.get("id_bidang")
        harga = request.POST.get("harga")
        model = UjiLab(uid=uid,nama=nama, satuan=satuan, id_bidang=id_bidang, harga=harga)
        model.save()
    return HttpResponseRedirect(reverse('uji_lab:all_uji_lab'))


def delete_uji_lab(request, id):
    return render(request, 'index.html', response)

def all_uji_lab(request):
    tmp = UjiLab.objects.all()
    bidang = Bidang.objects.all()
    flag_null = True
    if tmp.count() != 0:
        flag_null = False
    response["labs"] = tmp
    response["bidangs"] = bidang
    response["flag_null"] = flag_null
    return render(request, 'lp_uji_lab.html', response)

def edit_uji_lab(request, id):
    tmp = UjiLab.objects.get(uid=id)
    if request.method == 'POST':
        tmp.nama = request.POST.get("nama")
        tmp. satuan = request.POST.get("satuan")
        tmp.id_bidang = request.POST.get("id_bidang")
        tmp.harga = request.POST.get("harga")
        tmp.save()
    return HttpResponseRedirect(reverse('uji_lab:all_uji_lab'))

def view_uji_lab(request, id):
    return render(request, 'index.html', response)
