from django.shortcuts import render
from obras.models import Obra, Perfil, Mensaje
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
def index(request):
    return render(request, "obras/index.html")

def home(request):
    return render(request, "obras/home.html")

def about(request):
    return render(request, "obras/about.html")

class ObraList(ListView):
    model = Obra
    context_object_name = "obras"

class ObraUserList(LoginRequiredMixin, ObraList):
    def get_queryset(self):
        return Obra.objects.filter(autor=self.request.user.id).all()
  

class ObraDetalle(DetailView):
    model = Obra
    context_object_name = "obra"

class ObraActualizar(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Obra
    success_url = reverse_lazy("obra-list")
    fields = '__all__'
    
    def test_func(self):
        user_id = self.request.user.id
        obra_id = self.kwargs.get("pk")
        return Obra.objects.filter(autor=user_id, id=obra_id).exists()

class ObraEliminar(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Obra
    context_object_name = "obra"
    success_url = reverse_lazy("obra-list")

    def test_func(self):
        user_id = self.request.user.id
        obra_id = self.kwargs.get("pk")
        return Obra.objects.filter(autor=user_id, id=obra_id).exists()

class ObraCrear(LoginRequiredMixin, CreateView):
    model = Obra
    success_url = reverse_lazy("obra-list")
    fields = '__all__'

class Login(LoginView):
    next_page = reverse_lazy("obra-list")
    
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("login")

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class PerfilCrear(CreateView):
    model = Perfil
    success_url = reverse_lazy("obra-list")
    fields = ['avatar']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PerfilActualizar(UserPassesTestMixin, UpdateView):
    model = Perfil
    success_url = reverse_lazy("obra-list")
    fields = ['avatar']

    def test_func(self):
        return Perfil.objects.filter(user=self.request.user).exists()

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy("mensaje-crear")
    fields = '__all__'

class MensajeEliminar(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        return Mensaje.objects.filter(destinatario=self.request.user).exists()

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensaje"

    def get_queryset(self):
        import pdb; pdb.set_trace
        return Mensaje.objects.filter(destinatario=self.request.user).all()

class MensajeDetalle(DetailView):
    model = Mensaje
    context_object_name = "mensaje"