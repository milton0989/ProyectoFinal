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

from obras.views import (index, home, about,
                         ObraList, ObraDetalle, ObraActualizar, ObraEliminar, ObraCrear,
                        Login, SignUp, Logout, ObraUserList, PerfilCrear, PerfilActualizar,
                        MensajeCrear, MensajeList, MensajeEliminar, MensajeDetalle,
                        )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('about/', about, name="about"),
    path('admin/', admin.site.urls),
    path('obra/list', ObraList.as_view(), name="obra-list"),
    path('obra/<pk>/detalle', ObraDetalle.as_view(), name="obra-detalle"),
    path('obra/<pk>/actualizar', ObraActualizar.as_view(), name="obra-actualizar"),
    path('obra/<pk>/eliminar', ObraEliminar.as_view(), name="obra-eliminar"),
    path('obra/crear', ObraCrear.as_view(), name="obra-crear"),
    path('login/', Login.as_view(), name="login"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('logout/', Logout.as_view(), name="logout"),
    path('obra/list/user', ObraUserList.as_view(), name="obra-user"),
    path('perfil/crear', PerfilCrear.as_view(), name="perfil-crear"),
    path('perfil/<pk>/actualizar', PerfilActualizar.as_view(), name="perfil-actualizar"),
    path('mensaje/crear', MensajeCrear.as_view(), name="mensaje-crear"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),
    path('mensaje/<pk>/detalle', MensajeDetalle.as_view(), name="mensaje-detalle"),
    path('mensaje/<pk>/eliminar', MensajeEliminar.as_view(), name="mensaje-eliminar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)