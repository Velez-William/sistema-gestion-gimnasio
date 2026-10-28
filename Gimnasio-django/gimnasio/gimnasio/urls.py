"""
URL configuration for gimnasio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # ======================
    # INICIO
    # ======================
    path('', views.inicio, name='inicio'),

    # ======================
    # MIEMBROS
    # ======================
    path('miembros/nuevo/', views.nuevoMiembro, name='nuevo_miembro'),
    path('miembros/<int:id>/', views.detalleMiembro, name='detalle_miembro'),
    path('miembros/editar/<int:id>/', views.editarMiembro, name='editar_miembro'),
    path('miembros/eliminar/<int:id>/', views.eliminarMiembro, name='eliminar_miembro'),

    # ======================
    # CLASES
    # ======================
    path('clases/nueva/', views.nuevaClase, name='nueva_clase'),
    path('clases/<int:id>/', views.detalleClase, name='detalle_clase'),
    path('clases/editar/<int:id>/', views.editarClase, name='editar_clase'),
    path('clases/eliminar/<int:id>/', views.eliminarClase, name='eliminar_clase'),
]








# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)