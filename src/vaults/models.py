"""
passwords_app/models.py - Modelo de contraseñas actualizado.
"""
from django.db import models
from django.contrib.auth.models import User

class PasswordRecord(models.Model):
    """
    Modelo para almacenar los registros de contraseñas de un usuario.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_records')
    title = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    encrypted_password = models.BinaryField()
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        unique_together = ('user', 'title')

    def __str__(self):
        return f"{self.title} for {self.user.username}"
