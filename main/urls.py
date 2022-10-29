

from django import views
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from main.views import HospitalCreateView, HospitalView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('hospital/', HospitalView.as_view(), name='hospital'),
    path('cadastrohospital/', HospitalCreateView.as_view(), name='cadastrohospital'),
]
