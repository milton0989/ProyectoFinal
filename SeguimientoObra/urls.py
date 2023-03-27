"""SeguimientoObra URL Configuration

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
from django.urls import path

from obras.views import index, ObraList, ObraDetalle, ObraActualizar, ObraEliminar, ObraCrear, Login

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('obra/list', ObraList.as_view(), name="obra-list"),
    path('obra/<pk>/detalle', ObraDetalle.as_view(), name="obra-detalle"),
    path('obra/<pk>/actualizar', ObraActualizar.as_view(), name="obra-actualizar"),
    path('obra/<pk>/eliminar', ObraEliminar.as_view(), name="obra-eliminar"),
    path('obra/crear', ObraCrear.as_view(), name="obra-crear"),
    path('login/', Login.as_view(), name="login"),
]
