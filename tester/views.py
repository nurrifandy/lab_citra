from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

# Landing pertama ketika membuka halaman tester
response ={'lab_name' : 'citra'}
def index(request):
    return render(request, 'index.html')

# function untuk menambahkan tester baru
def add_tester(request):
    testers = Tester.objects.all()
    tmp = testers.count()+1
    if request.method == 'POST':
        kode = 'TST' + str(tmp)
        nama = request.POST.get('nama_tester')
        model = Tester(kode = kode, nama = nama)
        model.save()
        return HttpResponseRedirect(reverse('tester:all_tester'))
    else:
        return HttpResponseRedirect(reverse('tester:all_tester'))

# function untuk mengedit object tester
def edit_tester(request, id):
    person = Tester.objects.get(kode = id)
    if request.method == 'POST':
        person.nama = request.POST.get('nama_tester')
        person.save()
    return HttpResponseRedirect(reverse('tester:all_tester'))

# function untuk menghapus tester
def delete_tester(request, id=None):
    obj_tester = Tester.objects.get(id=1)
    obj_tester.delete()
    return render(render, 'index.html')

# function untuk menampilkan semua tester
def all_tester(request):
    testers = Tester.objects.all()
    flag_null = True
    if testers.count() != 0:
        flag_null = False
    response["testers"] = testers
    response["flag_null"] = flag_null
    return render(request, 'lp_tester.html', response)