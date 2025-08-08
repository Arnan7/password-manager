"""
users_app/views.py - Vistas de autenticación actualizadas.
"""
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User # <- Se ha añadido esta línea
from .serializers import UserRegistrationSerializer, AuthTokenEmailSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    """
    Vista para el registro de nuevos usuarios.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class LoginView(ObtainAuthToken):
    """
    Vista para el inicio de sesión con email y contraseña.
    """
    serializer_class = AuthTokenEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email
        })

class LogoutView(APIView):
    """
    Vista para cerrar la sesión de un usuario.
    Elimina el token de autenticación del usuario actual.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # El token se obtiene automáticamente del objeto request
        # si la autenticación fue exitosa.
        try:
            # Elimina el token asociado al usuario autenticado.
            request.user.auth_token.delete()
            return Response({"detail": "Cierre de sesión exitoso."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)