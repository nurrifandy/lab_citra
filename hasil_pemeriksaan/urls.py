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
from django.urls import path
from .views import *

app_name= 'hasil_pemeriksaan'
urlpatterns = [
    path('', all_hasil_pemeriksaan, name='all_hasil_pemeriksaan'),
    path('add/', add_hasil_pemeriksaan, name='add_hasil_pemeriksaan'),
    path('edit/<str:id>', edit_hasil_pemeriksaan, name='edit_hasil_pemeriksaan'),
    path('delete/<str:id>', delete_hasil_pemeriksaan, name='delete_hasil_pemeriksaan'),
    path('view/<str:id>', view_hasil_pemeriksaan, name='view_hasil_pemeriksaan'),
]
