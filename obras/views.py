from django.shortcuts import render
from obras.models import Obra
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

# Create your views here.

class ObraList(ListView):
    model = Obra
    context_object_name = "obras"

class ObraDetalle(DetailView):
    model = Obra
    context_object_name = "obra"

class ObraActualizar(UpdateView):
    model = Obra
    success_url = reverse_lazy("obra-list")
    fields = '__all__'

class ObraEliminar(DeleteView):
    model = Obra
    context_object_name = "obra"
    success_url = reverse_lazy("obra-list")

class ObraCrear(CreateView):
    model = Obra
    success_url = reverse_lazy("obra-list")
    fields = '__all__'

