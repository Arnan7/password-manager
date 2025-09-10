# Documentación Swagger - Password Manager API

## Configuración Completada

Este proyecto ahora incluye documentación automática de la API usando **drf-spectacular** (Swagger/OpenAPI 3.0).

## Instalación

```bash
pip install drf-spectacular
```

## Migración de Base de Datos

```bash
python manage.py makemigrations
python manage.py migrate
```

## Generar Esquema de la API

```bash
# Generar esquema YAML
python manage.py spectacular --color --file schema.yml

# Generar esquema JSON
python manage.py spectacular --color --file schema.json --format openapi-json
```

## Acceso a la Documentación

Una vez que el servidor esté ejecutándose, puedes acceder a la documentación en:

### 1. Swagger UI (Interfaz Interactiva)
```
http://localhost:8000/api/docs/
```

### 2. ReDoc (Documentación Alternativa)
```
http://localhost:8000/api/redoc/
```

### 3. Esquema OpenAPI (JSON)
```
http://localhost:8000/api/schema/
```

## Características de la Documentación

### ✅ Endpoints Documentados

#### **Autenticación** (`/api/auth/`)
- `POST /register/` - Registrar nuevo usuario
- `POST /login/` - Iniciar sesión (JWT)
- `POST /logout/` - Cerrar sesión
- `POST /token/refresh/` - Renovar access token
- `POST /token/verify/` - Verificar token

#### **Gestión de Contraseñas** (`/api/passwords/`)
- `GET /` - Listar contraseñas del usuario
- `POST /` - Crear nueva contraseña
- `GET /{id}/` - Obtener contraseña específica
- `PUT /{id}/` - Actualizar contraseña
- `PATCH /{id}/` - Actualización parcial
- `DELETE /{id}/` - Eliminar contraseña
- `GET /generate/` - Generar contraseña segura

### ✅ Características Incluidas

1. **Ejemplos de Request/Response**: Cada endpoint incluye ejemplos reales
2. **Códigos de Estado HTTP**: Documentación completa de respuestas
3. **Parámetros**: Descripción detallada de parámetros de query y path
4. **Autenticación JWT**: Configurada para pruebas interactivas
5. **Tags Organizados**: Endpoints agrupados por funcionalidad
6. **Validación de Esquemas**: Validación automática de datos

### ✅ Interfaz de Usuario

- **Swagger UI**: Interfaz moderna y fácil de usar
- **ReDoc**: Documentación limpia y profesional
- **Pruebas Interactivas**: Puedes probar la API directamente desde la documentación
- **Autenticación Integrada**: Botón "Authorize" para JWT tokens

## Uso de la Documentación

### 1. Probar la API

1. Ve a `http://localhost:8000/api/docs/`
2. Haz clic en "Authorize" (🔒)
3. Ingresa tu JWT token: `Bearer <tu_access_token>`
4. Prueba los endpoints directamente

### 2. Obtener Token JWT

1. Usa el endpoint `/api/auth/login/` con:
   ```json
   {
     "email": "tu_email@ejemplo.com",
     "password": "tu_contraseña"
   }
   ```
2. Copia el `access` token de la respuesta
3. Úsalo en el botón "Authorize"

### 3. Ejemplos de Uso

#### Registrar Usuario
```bash
curl -X POST "http://localhost:8000/api/auth/register/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "usuario_test",
    "email": "test@ejemplo.com",
    "password": "contraseña123"
  }'
```

#### Iniciar Sesión
```bash
curl -X POST "http://localhost:8000/api/auth/login/" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@ejemplo.com",
    "password": "contraseña123"
  }'
```

#### Crear Contraseña (con autenticación)
```bash
curl -X POST "http://localhost:8000/api/passwords/" \
  -H "Authorization: Bearer <tu_access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Mi cuenta de Gmail",
    "username": "mi_email@gmail.com",
    "password": "mi_contraseña_encriptada",
    "notes": "Cuenta principal"
  }'
```

## Configuración Avanzada

### Personalización del Esquema

La configuración de drf-spectacular se encuentra en `settings.py`:

```python
SPECTACULAR_SETTINGS = {
    'TITLE': 'Password Manager API',
    'DESCRIPTION': 'API para gestión segura de contraseñas con autenticación JWT',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SCHEMA_PATH_PREFIX': '/api/',
    'AUTHENTICATION_WHITELIST': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'SERVERS': [
        {
            'url': 'http://localhost:8000',
            'description': 'Servidor de desarrollo'
        },
    ],
    'TAGS': [
        {'name': 'Autenticación', 'description': 'Endpoints de autenticación y gestión de usuarios'},
        {'name': 'Contraseñas', 'description': 'Gestión de contraseñas y bóvedas'},
    ],
}
```

### Generar Documentación Estática

```bash
# Generar esquema YAML
python manage.py spectacular --color --file schema.yml

# Generar esquema JSON
python manage.py spectacular --color --file schema.json --format openapi-json
```

## Ventajas de esta Implementación

1. **Documentación Automática**: Se actualiza automáticamente con los cambios en el código
2. **Interfaz Interactiva**: Permite probar la API sin herramientas externas
3. **Estándar OpenAPI 3.0**: Compatible con herramientas de terceros
4. **Integración JWT**: Autenticación configurada para pruebas
5. **Ejemplos Reales**: Cada endpoint incluye ejemplos prácticos
6. **Organización Clara**: Endpoints agrupados por funcionalidad

## Próximos Pasos

1. **Ejecutar el servidor**: `python manage.py runserver`
2. **Visitar la documentación**: `http://localhost:8000/api/docs/`
3. **Probar los endpoints**: Usar la interfaz interactiva
4. **Compartir con el equipo**: La documentación está lista para uso

¡La documentación Swagger está completamente configurada y lista para usar! 🚀



{
  "title": "Netlfix",
  "username": "netflixaccf@gmail.com",
  "password": "fullxd515",
  "notes": ""
}
