from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


from dokter.models import *

# Create your views here.
response ={'lab_name' : 'citra'}
def add_dokter(request):
    if request.method == 'POST':
        kode_dokter = request.POST.get("kode_dokter")
        nama = request.POST.get("nama_dokter")
        komisi_dokter = request.POST.get("komisi_dokter")
        komisi_belum_dibayar = 0
        komisi_sudah_sibayar = 0
        model = Dokter(kode_dokter=kode_dokter, nama=nama,komisi_dokter=komisi_dokter, komisi_belum_dibayar = komisi_belum_dibayar, komisi_sudah_dibayar=komisi_sudah_sibayar)
        model.save()
    return HttpResponseRedirect(reverse('dokter:all_dokter'))

def delete_dokter(request, id):
    person = Dokter.objects.get(kode_dokter = id)
    person.delete()
    return HttpResponseRedirect(reverse('dokter:all_dokter'))

def all_dokter(request):
    docters = Dokter.objects.all()
    flag_null = True
    if docters.count() != 0:
        flag_null = False
    response["doctors"] = docters
    response["flag_null"] = flag_null
    return render(request, 'landing_page_dokter.html', response)

def edit_dokter(request, id):
    person = Dokter.objects.get(kode_dokter = id)
    if request.method == 'POST':
        person.kode_dokter = request.POST.get("kode_dokter")
        person.nama = request.POST.get("nama_dokter")
        person.komisi_dokter = request.POST.get("komisi_dokter")
        person.save()
    return HttpResponseRedirect(reverse('dokter:all_dokter'))

def update_komisi_dokter(request, id):
    person = Dokter.objects.get(kode_dokter = id)
    person.komisi_sudah_dibayar = person.komisi_sudah_dibayar + person.komisi_belum_dibayar
    person.komisi_belum_dibayar = 0
    person.save()
    return HttpResponseRedirect(reverse('dokter:all_dokter'))

def view_dokter(request, id):
    return render(request, 'index.html', response)
