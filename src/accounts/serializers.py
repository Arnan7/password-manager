"""
users_app/serializers.py - Serializadores de autenticación actualizados.
"""
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializador para el registro de nuevos usuarios con email.
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Crea un nuevo usuario con la contraseña hasheada y el email.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class AuthTokenEmailSerializer(AuthTokenSerializer):
    """
    Serializador personalizado para autenticación con email en lugar de username.
    """
    email = serializers.EmailField(label="Email")
    username = None # Deshabilitamos el campo username del serializador base

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # Buscamos al usuario por correo electrónico
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
            
            # Verificamos la contraseña
            if not user.check_password(password):
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = ('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
