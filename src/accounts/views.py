"""
users_app/views.py - Vistas de autenticación actualizadas con JWT.
"""
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, CustomTokenObtainPairSerializer, LogoutSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


@extend_schema(
    tags=['Autenticación'],
    summary='Registrar nuevo usuario',
    description='Crea una nueva cuenta de usuario en el sistema de gestión de contraseñas.'
)
class RegisterView(generics.CreateAPIView):
    """
    Vista para el registro de nuevos usuarios.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

@extend_schema(
    tags=['Autenticación'],
    summary='Iniciar sesión',
    description='Autentica un usuario y retorna tokens JWT (access y refresh) para acceder a la API.'
)
class LoginView(TokenObtainPairView):
    """
    Vista para el inicio de sesión con email y contraseña usando JWT.
    """
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]

@extend_schema(
    tags=['Autenticación'],
    summary='Cerrar sesión',
    description='Invalida el refresh token del usuario agregándolo a la blacklist, cerrando efectivamente la sesión.'
)
class LogoutView(generics.GenericAPIView):
    """
    Vista para cerrar la sesión de un usuario.
    Invalida el refresh token agregándolo a la blacklist.
    """
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            refresh_token = serializer.validated_data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Cierre de sesión exitoso."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
