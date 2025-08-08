"""
passwords_app/serializers.py - Serializador de contraseñas actualizado.
"""
from rest_framework import serializers
from .models import PasswordRecord
from .utils import encrypt_data, decrypt_data

class PasswordRecordSerializer(serializers.ModelSerializer):
    """
    Serializador para los registros de contraseñas.
    Maneja el cifrado y descifrado de la contraseña.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = PasswordRecord
        # Se elimina el campo 'url' de los campos serializados
        fields = ('id', 'label', 'username', 'password', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def create(self, validated_data):
        """
        Cifra la contraseña antes de guardar el registro en la base de datos.
        """
        password_text = validated_data.pop('password')
        encrypted_password = encrypt_data(password_text)
        password_record = PasswordRecord.objects.create(
            encrypted_password=encrypted_password,
            **validated_data
        )
        return password_record

    def update(self, instance, validated_data):
        """
        Cifra la nueva contraseña antes de actualizar el registro.
        """
        if 'password' in validated_data:
            password_text = validated_data.pop('password')
            instance.encrypted_password = encrypt_data(password_text)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance

    def to_representation(self, instance):
        """
        Descifra la contraseña al leer los datos para enviarlos al frontend.
        """
        representation = super().to_representation(instance)
        try:
            representation['password'] = decrypt_data(instance.encrypted_password)
        except Exception:
            representation['password'] = None
        return representation
