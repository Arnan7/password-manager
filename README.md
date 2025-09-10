# Password Manager API

Una API segura para gestionar contraseñas personales, construida con Django REST Framework y JWT.

## Características 🚀

- ✅ **Autenticación segura con JWT**
- ✅ **Cifrado de contraseñas**
- ✅ **Gestión de múltiples contraseñas**
- ✅ **Documentación OpenAPI/Swagger**
- ✅ **Generador de contraseñas seguras**

## Requisitos Previos 📋

- Python 3.13+
- PostgreSQL
- pip

## Dependencias Principales 📦

- Django 5.2
- Django REST Framework
- SimpleJWT
- cryptography
- psycopg2-binary
- drf-spectacular

## Instalación 🔧

1. **Clonar el repositorio**
```bash
git clone <url-del-repositorio>
cd password-manager
```

2. **Crear y activar entorno virtual**
```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Unix
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install django djangorestframework djangorestframework-simplejwt drf-spectacular cryptography psycopg2-binary
```

4. **Configurar la base de datos**
   - Crear una base de datos PostgreSQL
   - Actualizar la configuración en `src/passmanager/settings.py`

5. **Aplicar migraciones**
```bash
cd src
python manage.py migrate
```

6. **Ejecutar el servidor de desarrollo**
```bash
python manage.py runserver
```

## Uso 🛠️

### Endpoints de Autenticación

- **POST** `/api/auth/register/`: Registrar nuevo usuario
- **POST** `/api/auth/login/`: Iniciar sesión
- **POST** `/api/auth/logout/`: Cerrar sesión

### Endpoints de Contraseñas

- **GET/POST** `/api/passwords/`: Listar/Crear contraseñas
- **GET/PUT/DELETE** `/api/passwords/{id}/`: Ver/Actualizar/Eliminar contraseña
- **GET** `/api/passwords/generate/`: Generar contraseña segura

### Documentación

La documentación completa de la API está disponible en:
- Swagger UI: `/api/docs/`
- OpenAPI Schema: `/api/schema/`

## Seguridad 🔒

- Las contraseñas se almacenan cifradas usando Fernet (cryptography)
- Autenticación mediante tokens JWT
- Blacklist de tokens para logout seguro
- Validación de datos en todas las operaciones

## Estructura del Proyecto 📁

```
password-manager/
├── src/
│   ├── accounts/          # App de autenticación
│   ├── vaults/           # App de gestión de contraseñas
│   ├── passmanager/      # Configuración principal
│   └── manage.py
├── README.md
└── requirements.txt
```

## Desarrollo 💻

### Ejecutar tests
```bash
python manage.py test
```

### Generar documentación
```bash
python manage.py spectacular --file schema.yml
```

## Características de Seguridad 🛡️

- Cifrado simétrico para las contraseñas almacenadas
- Tokens JWT con rotación
- Validación de entrada en todas las operaciones
- Permisos basados en usuario para acceso a datos
- CORS configurado para seguridad
- Rate limiting para prevenir ataques

## Ejemplos de Uso 📝

### Registro de Usuario
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
    -H "Content-Type: application/json" \
    -d '{"username":"usuario","email":"usuario@ejemplo.com","password":"contraseña123"}'
```

### Inicio de Sesión
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
    -H "Content-Type: application/json" \
    -d '{"email":"usuario@ejemplo.com","password":"contraseña123"}'
```

### Crear Nueva Contraseña
```bash
curl -X POST http://localhost:8000/api/passwords/ \
    -H "Authorization: Bearer <tu-token>" \
    -H "Content-Type: application/json" \
    -d '{"title":"Mi Cuenta","username":"usuario","password":"contraseña","notes":"notas opcionales"}'
```

## Contribuir 🤝

1. Fork el proyecto
2. Crear una rama (`git checkout -b feature/AmazingFeature`)
3. Commit los cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia 📄

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para detalles
