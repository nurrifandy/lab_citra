from django.shortcuts import render
from .models import *

# Landing pertama ketika membuka halaman tester
def index(request):
    return render(request, 'index.html')

# function untuk menambahkan tester baru
def add_tester(request):
    if request.method == 'POST':
        kode = request.POST.get('kode')
        nama = request.POST.get('nama')
        model = Tester(kode = kode, nama = nama)
        model.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

# function untuk mengedit object tester
def edit_tester(request, id):
    obj_tester = Tester.objects.get(id=1)
    if request.method == 'POST':
        obj_tester.kode = request.POST.get('kode')
        obj_tester.nama = request.POST.get('nama')
        obj_tester.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
    return render(request, 'index.html')

# function untuk menghapus tester
def delete_tester(request, id=None):
    obj_tester = Tester.objects.get(id=1)
    obj_tester.delete()
    return render(render, 'index.html')

# function untuk menampilkan semua tester
def all_tester(request):
    all_obj = Tester.objects.all()
    return render(render, 'index.html')