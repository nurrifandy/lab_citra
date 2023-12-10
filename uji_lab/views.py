from django.shortcuts import render


from pasien.models import *

# Create your views here.
response ={'lab_name' : 'citra'}
def add_uji_lab(request, id):
    person = Pasien.objects.get(uid=id)

    response['person'] = person
    return render(request, 'tambah_ujilab.html', response)

def delete_uji_lab(request, id):
    return render(request, 'index.html', response)

def all_uji_lab(request, id):
    return render(request, 'index.html', response)

def edit_uji_lab(request, id):
    return render(request, 'index.html', response)

def view_uji_lab(request, id):
    return render(request, 'index.html', response)
