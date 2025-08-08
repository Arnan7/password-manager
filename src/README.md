# Gestor de Contraseñas API

Este proyecto es una API RESTful segura construida con Django y Django REST Framework para gestionar contraseñas de usuarios. Ofrece funcionalidades para el registro de usuarios, autenticación basada en tokens, y un baúl cifrado para almacenar, recuperar y gestionar contraseñas de forma segura.

## Características Principales

- **Autenticación Segura:** Sistema de registro y login con autenticación basada en tokens.
- **Cifrado de Datos:** Todas las contraseñas se almacenan cifradas utilizando criptografía simétrica (Fernet).
- **Gestión de Contraseñas (CRUD):** Operaciones completas para crear, leer, actualizar y eliminar registros de contraseñas.
- **Generador de Contraseñas:** Un endpoint para generar contraseñas seguras y personalizables en longitud.
- **API RESTful:** Una interfaz bien definida y fácil de consumir para aplicaciones cliente (frontend, móvil, etc.).

## Tecnologías Utilizadas

- **Backend:** Python, Django, Django REST Framework
- **Base de Datos:** PostgreSQL (recomendado), SQLite (para desarrollo)
- **Cifrado:** `cryptography` (Fernet)
- **Autenticación:** `djangorestframework.authtoken`

---

## Guía de Inicio Rápido

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### 1. Prerrequisitos

- Python 3.8 o superior
- `pip` (gestor de paquetes de Python)
- Git

### 2. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd password-manager
```

### 3. Configurar el Entorno Virtual

Es una buena práctica usar un entorno virtual para aislar las dependencias del proyecto.

```bash
# Crear un entorno virtual
python -m venv .venv

# Activar el entorno virtual
# En Windows:
.venv\Scripts\activate
# En macOS/Linux:
source .venv/bin/activate
```

### 4. Instalar Dependencias

Instala todas las librerías necesarias desde el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 5. Aplicar Migraciones

Aplica las migraciones de la base de datos para crear las tablas necesarias.

```bash
python src/manage.py migrate
```

### 6. Ejecutar el Servidor de Desarrollo

¡Ya está todo listo! Inicia el servidor de desarrollo.

```bash
python src/manage.py runserver
```

La API estará disponible en `http://127.0.0.1:8000`.

---

## Referencia de la API: Guía Detallada

A continuación, se presenta una guía detallada de cada endpoint de la API. Está diseñada para que un desarrollador frontend pueda entender el flujo de trabajo y consumir los servicios de manera eficiente.

**URL Base:** `http://127.0.0.1:8000/`

---

### **Flujo de Trabajo General**

1.  **Registrar un Usuario:** El primer paso para cualquier usuario nuevo.
2.  **Iniciar Sesión:** El usuario proporciona sus credenciales (email y contraseña) para obtener un **token de autenticación**.
3.  **Acceder a Recursos Protegidos:** El cliente (frontend) debe guardar este token y enviarlo en la cabecera `Authorization` de cada petición a los endpoints que requieren autenticación (como la gestión de contraseñas).
4.  **Gestionar Contraseñas:** Con un token válido, el usuario puede crear, ver, actualizar, eliminar y generar contraseñas.
5.  **Cerrar Sesión:** Cuando el usuario termina, el token se invalida para cerrar la sesión de forma segura.

---

### **Módulo de Autenticación (`/api/auth/`)**

#### **1. Registro de un Nuevo Usuario**

-   **Propósito:** Permite que un nuevo usuario cree una cuenta en el sistema.
-   **Endpoint:** `POST /api/auth/register/`
-   **Cómo funciona:** Se envía el nombre de usuario, email y contraseña. El servidor crea un nuevo registro de usuario con la contraseña hasheada (no en texto plano).

-   **Ejemplo de Petición (usando `fetch` en JavaScript):**
    ```javascript
    fetch('http://127.0.0.1:8000/api/auth/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: 'juanperez',
        email: 'juan.perez@email.com',
        password: 'PasswordSeguro123!',
      }),
    })
    .then(response => response.json())
    .then(data => console.log(data));
    ```

-   **Respuesta Exitosa (`201 Created`):**
    ```json
    {
        "username": "juanperez",
        "email": "juan.perez@email.com"
    }
    ```

#### **2. Inicio de Sesión y Obtención de Token**

-   **Propósito:** Verificar las credenciales de un usuario y proporcionarle un token de acceso.
-   **Endpoint:** `POST /api/auth/login/`
-   **Cómo funciona:** El usuario envía su email y contraseña. Si son correctos, el servidor genera (o recupera) un token único y lo devuelve. **Este token es esencial para las siguientes peticiones.**

-   **Ejemplo de Petición:**
    ```javascript
    fetch('http://127.0.0.1:8000/api/auth/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: 'juan.perez@email.com',
        password: 'PasswordSeguro123!',
      }),
    })
    .then(response => response.json())
    .then(data => {
      if (data.token) {
        // Guardar el token de forma segura (ej. en localStorage o una cookie)
        localStorage.setItem('authToken', data.token);
        console.log('Inicio de sesión exitoso:', data);
      }
    });
    ```

-   **Respuesta Exitosa (`200 OK`):**
    ```json
    {
        "token": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2",
        "user_id": 1,
        "username": "juanperez",
        "email": "juan.perez@email.com"
    }
    ```

#### **3. Cierre de Sesión**

-   **Propósito:** Invalidar el token de sesión del usuario para que ya no pueda ser utilizado.
-   **Endpoint:** `POST /api/auth/logout/`
-   **Autenticación Requerida:** Sí.
-   **Cómo funciona:** El cliente envía una petición a este endpoint incluyendo el token en la cabecera. El servidor buscará y eliminará el token asociado al usuario, haciendo que cualquier petición futura con ese token falle.

-   **Ejemplo de Petición:**
    ```javascript
    const token = localStorage.getItem('authToken');

    fetch('http://127.0.0.1:8000/api/auth/logout/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`,
      },
    })
    .then(response => {
      if (response.ok) {
        // Eliminar el token del almacenamiento local
        localStorage.removeItem('authToken');
        console.log('Sesión cerrada exitosamente.');
      }
    });
    ```

-   **Respuesta Exitosa (`200 OK`):**
    ```json
    {
        "detail": "Cierre de sesión exitoso."
    }
    ```

---

### **Módulo de Gestión de Contraseñas (`/api/passwords/`)**

Estos endpoints permiten a un usuario autenticado gestionar su baúl de contraseñas. **Todos requieren un token de autenticación válido.**

**Cabecera de Autorización Requerida:**
`Authorization: Token <tu_token_aqui>`

#### **1. Listar Todas las Contraseñas y Crear una Nueva**

-   **Endpoint:** `/api/passwords/`

-   **Caso de Uso: Listar Contraseñas (`GET`)**
    -   **Propósito:** Obtener todos los registros de contraseñas guardados por el usuario.
    -   **Ejemplo de Petición:**
        ```javascript
        const token = localStorage.getItem('authToken');
        fetch('http://127.0.0.1:8000/api/passwords/', {
          headers: {
            'Authorization': `Token ${token}`,
          }
        })
        .then(response => response.json())
        .then(passwords => console.log('Mis contraseñas:', passwords));
        ```
    -   **Respuesta Exitosa (`200 OK`):** Un array de objetos, donde cada objeto es un registro de contraseña. La contraseña se devuelve descifrada.
        ```json
        [
            {
                "id": 1,
                "label": "Gmail",
                "username": "juan.perez",
                "password": "mi_contraseña_de_gmail",
                "created_at": "2023-10-27T10:00:00Z",
                "updated_at": "2023-10-27T10:00:00Z"
            },
            {
                "id": 2,
                "label": "GitHub",
                "username": "juanperez-dev",
                "password": "mi_super_contraseña_de_github",
                "created_at": "2023-10-28T12:30:00Z",
                "updated_at": "2023-10-28T12:30:00Z"
            }
        ]
        ```

-   **Caso de Uso: Crear una Nueva Contraseña (`POST`)**
    -   **Propósito:** Guardar un nuevo registro de contraseña en el baúl. La contraseña enviada se cifra en el servidor antes de guardarse.
    -   **Ejemplo de Petición:**
        ```javascript
        const token = localStorage.getItem('authToken');
        fetch('http://127.0.0.1:8000/api/passwords/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
          },
          body: JSON.stringify({
            label: 'Twitter',
            username: 'juanperez_tweets',
            password: 'MiClaveDeTwitter123',
          }),
        })
        .then(response => response.json())
        .then(newPassword => console.log('Nueva contraseña guardada:', newPassword));
        ```
    -   **Respuesta Exitosa (`201 Created`):** El objeto del nuevo registro creado, con la contraseña descifrada para confirmación.
        ```json
        {
            "id": 3,
            "label": "Twitter",
            "username": "juanperez_tweets",
            "password": "MiClaveDeTwitter123",
            "created_at": "2023-10-29T14:00:00Z",
            "updated_at": "2023-10-29T14:00:00Z"
        }
        ```

#### **2. Gestionar un Registro de Contraseña Específico**

-   **Endpoint:** `/api/passwords/<id>/` (ej. `/api/passwords/3/`)

-   **Caso de Uso: Ver Detalles (`GET`)**
    -   **Propósito:** Obtener la información de un solo registro de contraseña.

-   **Caso de Uso: Actualizar (`PUT` / `PATCH`)**
    -   **Propósito:** Modificar los datos de un registro existente (ej. cambiar la contraseña o el nombre de usuario).
    -   `PUT`: Reemplaza el objeto completo. Debes enviar todos los campos.
    -   `PATCH`: Actualiza solo los campos que envíes.

-   **Caso de Uso: Eliminar (`DELETE`)**
    -   **Propósito:** Borrar permanentemente un registro de contraseña.

-   **Ejemplo de Petición (Actualizar con `PATCH`):**
    ```javascript
    const token = localStorage.getItem('authToken');
    const passwordId = 3;
    fetch(`http://127.0.0.1:8000/api/passwords/${passwordId}/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`,
      },
      body: JSON.stringify({
        password: 'MiNuevaClaveDeTwitterMasSegura456',
      }),
    })
    .then(response => response.json())
    .then(updatedPassword => console.log('Contraseña actualizada:', updatedPassword));
    ```

-   **Ejemplo de Petición (Eliminar):**
    ```javascript
    const token = localStorage.getItem('authToken');
    const passwordIdToDelete = 3;
    fetch(`http://127.0.0.1:8000/api/passwords/${passwordIdToDelete}/`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Token ${token}`,
      },
    })
    .then(response => {
      if (response.status === 204) {
        console.log('Registro eliminado exitosamente.');
      }
    });
    ```

#### **3. Generar una Contraseña Segura**

-   **Propósito:** Obtener una contraseña segura generada aleatoriamente por el servidor.
-   **Endpoint:** `GET /api/passwords/generate/`
-   **Autenticación Requerida:** Sí.
-   **Cómo funciona:** Es una herramienta de utilidad para que el usuario pueda generar contraseñas fuertes directamente desde la aplicación cliente sin necesidad de lógica adicional en el frontend.

-   **Ejemplo de Petición (con longitud personalizada):**
    ```javascript
    const token = localStorage.getItem('authToken');
    const passwordLength = 20;
    fetch(`http://127.0.0.1:8000/api/passwords/generate/?length=${passwordLength}`, {
      headers: {
        'Authorization': `Token ${token}`,
      }
    })
    .then(response => response.json())
    .then(data => console.log('Contraseña generada:', data.password));
    ```

-   **Respuesta Exitosa (`200 OK`):**
    ```json
    {
        "password": "aBc1@XyZ!pQrS#tUv&wYz"
    }
    ```
