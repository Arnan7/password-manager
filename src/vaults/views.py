"""
passwords_app/views.py - Vistas para la gestión de contraseñas.
"""
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Ya no necesitas importar Fernet, string, secrets ni settings aquí.
from .models import PasswordRecord
from .serializers import PasswordRecordSerializer
from .utils import encrypt_data, decrypt_data, generate_secure_password # ¡Importación corregida!


# --- Vistas de la API ---
class PasswordRecordListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar los registros de contraseñas del usuario autenticado
    y crear nuevos registros.
    """
    serializer_class = PasswordRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retorna solo los registros de contraseñas del usuario autenticado.
        """
        return PasswordRecord.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Asigna el usuario autenticado al crear un nuevo registro.
        """
        serializer.save(user=self.request.user)

class PasswordRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para ver, actualizar y eliminar un registro de contraseña específico.
    """
    serializer_class = PasswordRecordSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """
        Asegura que el usuario solo pueda acceder a sus propios registros.
        """
        return PasswordRecord.objects.filter(user=self.request.user)

class GeneratePasswordView(views.APIView):
    """
    Vista para generar una contraseña segura.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            length = int(request.query_params.get('length', 16))
            if length < 8:
                return Response({"error": "La longitud debe ser al menos 8."}, status=status.HTTP_400_BAD_REQUEST)
        except (ValueError, TypeError):
            length = 16

        secure_password = generate_secure_password(length)
        return Response({"password": secure_password})
