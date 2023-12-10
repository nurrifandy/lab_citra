"""citra_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

import main.urls
import pasien.urls
import nilai_normal.urls
import uji_lab.urls
import dokter.urls
import tester.urls
import pemeriksaan.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='pasien/', permanent=True)),
    path('home/', include(main.urls)),
    path('pasien/', include(pasien.urls)),
    path('nilai_normal/', include(nilai_normal.urls)),
    path('ujilab/', include(uji_lab.urls)),
    path('pemeriksaan/', include(pemeriksaan.urls)),
    path('dokter/', include(dokter.urls)),
    path('tester/', include(tester.urls)),
    
]
