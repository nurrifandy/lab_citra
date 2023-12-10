from django.shortcuts import render


from pasien.models import *

# Create your views here.
response ={'lab_name' : 'citra'}
def add_pemeriksaan(request, id):
    person = Pasien.objects.get(uid=id)

    response['person'] = person
    return render(request, 'tambah_ujilab.html', response)

def delete_pemeriksaan(request, id):
    return render(request, 'index.html', response)

def all_pemeriksaan(request, id):
    return render(request, 'index.html', response)

def edit_pemeriksaan(request, id):
    return render(request, 'index.html', response)

def view_pemeriksaan(request, id):
    return render(request, 'index.html', response)
