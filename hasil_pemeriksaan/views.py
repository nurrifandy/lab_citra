from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import *

# Create your views here.
response = {"lab" : "citra"}
def all_hasil_pemeriksaan(request):
    return render(request, 'index.html', response)

def edit_hasil_pemeriksaan(request, id):
    pemeriksaan_id = None
    hasil_pemeriksaan = HasilPemeriksaan.objects.get(hpid=id)
    if request.method == 'POST':
        hasil_pemeriksaan.hasil = request.POST.get("hasil")
        hasil_pemeriksaan.nilai_normal = request.POST.get("nilai_normal")
        pemeriksaan_id = request.POST.get("pid")
        hasil_pemeriksaan.save()
    return HttpResponseRedirect(reverse('pemeriksaan:view_pemeriksaan', kwargs={'id':pemeriksaan_id}))

def add_hasil_pemeriksaan(request):
    return render(request, 'index.html', response)

def delete_hasil_pemeriksaan(request, id):
    return render(request, 'index.html', response)
def view_hasil_pemeriksaan(request, id):
    return render(request, 'index.html', response)