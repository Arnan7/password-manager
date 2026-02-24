# syntax=docker/dockerfile:1
FROM python:3.12-slim

# evitar prompts de locales
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# primero las dependencias para aprovechar cache
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# copiar el resto del código al directorio de trabajo
# ubicamos los ficheros directamente en /app para que el paquete
# `passmanager` esté en el path de Python sin necesidad de PYTHONPATH
COPY src/ .
COPY README.md ./

# variables por defecto (se sobreescriben con docker-compose)
ENV DJANGO_SETTINGS_MODULE=passmanager.settings \
    DJANGO_DEBUG=False

# comando de arranque
CMD ["gunicorn", "passmanager.wsgi:application", "--bind", "0.0.0.0:8000"]