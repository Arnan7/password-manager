"""
vaults/utils.py - Funciones de utilidad para cifrado y generación de contraseñas.
"""
from django.conf import settings
from cryptography.fernet import Fernet
import string
import secrets

# Inicializa la suite de cifrado con la clave de la configuración.
cipher_suite = Fernet(settings.ENCRYPTION_KEY)

def encrypt_data(data: str) -> bytes:
    """Cifra los datos usando la clave de cifrado del servidor."""
    return cipher_suite.encrypt(data.encode('utf-8'))

def decrypt_data(encrypted_data: bytes) -> str:
    """Descifra los datos cifrados con la clave del servidor."""
    try:
        return cipher_suite.decrypt(encrypted_data).decode('utf-8')
    except Exception as e:
        # Manejo de errores en caso de que la clave sea incorrecta o el dato esté corrupto.
        print(f"Error al descifrar: {e}")
        return ""

def generate_secure_password(length: int = 16) -> str:
    """Genera una contraseña segura y aleatoria."""
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(characters) for _ in range(length))
    return secure_password
