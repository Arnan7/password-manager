"""
passwords_app/urls.py - URLs de la aplicación de contraseñas.
"""
from django.urls import path
from .views import (
    PasswordRecordListCreateView, 
    PasswordRecordDetailView,
    GeneratePasswordView
)

urlpatterns = [
    path('', PasswordRecordListCreateView.as_view(), name='password-list-create'),
    path('<int:pk>/', PasswordRecordDetailView.as_view(), name='password-detail'),
    path('generate/', GeneratePasswordView.as_view(), name='generate-password'),
]
