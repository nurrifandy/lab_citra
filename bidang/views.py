from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

response ={'lab_name' : 'citra'}

# function untuk menambahkan bidang baru
def add_bidang(request):
    bidangs = Bidang.objects.all()
    tmp = bidangs.count()+1
    if request.method == 'POST':
        uid = 'BDG' + str(tmp)
        nama = request.POST.get('nama_bidang')
        model = Bidang(uid = uid, nama = nama)
        model.save()
    return HttpResponseRedirect(reverse('bidang:all_bidang'))
    

# function untuk mengedit object bidang
def edit_bidang(request, id):
    tmp = Bidang.objects.get(uid = id)
    if request.method == 'POST':
        tmp.nama = request.POST.get('nama_bidang')
        tmp.save()
    return HttpResponseRedirect(reverse('bidang:all_bidang'))

# function untuk menghapus bidang
def delete_bidang(request, id=None):
    obj_bidang = Bidang.objects.get(uid=id)
    obj_bidang.delete()
    return render(render, 'index.html')

# function untuk menampilkan semua bidang
def all_bidang(request):
    bidangs = Bidang.objects.all()
    flag_null = True
    if bidangs.count() != 0:
        flag_null = False
    response["bidangs"] = bidangs
    response["flag_null"] = flag_null
    return render(request, 'lp_bidang.html', response)