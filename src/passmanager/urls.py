"""
urls.py - Definición de las URLs del proyecto.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluimos las URLs de ambas aplicaciones
    path('api/auth/', include('accounts.urls')),
    path('api/passwords/', include('vaults.urls')),
]
