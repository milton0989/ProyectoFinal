from django.shortcuts import render
from obras.models import Obra
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, "obras/index.html")

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

class Login(LoginView):
    next_page = reverse_lazy("obra-list")
    
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("obra-list")

class Logout(LogoutView):
    template_name = 'registration/logout.html'
