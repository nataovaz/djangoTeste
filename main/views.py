from pipes import Template
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from main.forms import HospitalForm

from main.models import Hospital

# Create your views here.
class HospitalView(ListView):
    model = Hospital
    queryset = Hospital.objects.all().order_by('name')

class IndexView(TemplateView):
    template_name = 'main/index.html'

class HospitalCreateView(CreateView):
    model = Hospital
    form_class = HospitalForm
    template_name = 'main/hospital_form.html'
    success_url = '/hospital/'