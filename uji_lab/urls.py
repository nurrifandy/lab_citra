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

app_name= 'uji_lab'
urlpatterns = [
    path('', all_uji_lab, name='all_uji_lab'),
    path('add/<str:id>', add_uji_lab, name='add_uji_lab'),
    path('edit/<str:id>', edit_uji_lab, name='edit_uji_lab'),
    path('delete/<str:id>', delete_uji_lab, name='delete_uji_lab'),
    path('view/<str:id>', view_uji_lab, name='view_uji_lab'),
]
