# proyectofinal-AgustinOrozco
proyecto final para desarrollador python coderhouse 2025
# Blog Django con perfiles y mensajería

Aplicación web estilo blog desarrollada en Django. Incluye autenticación (login, logout, registro), perfiles de usuario con avatar y datos personales, CRUD de páginas con texto enriquecido (CKEditor) e imágenes, y mensajería entre usuarios.

## Funcionalidades
- Home y Acerca de mí (about/)
- Listado de páginas (pages/) con búsqueda y detalle
- Crear, editar y eliminar páginas (solo usuarios autenticados)
- Admin con todos los modelos registrados
- Registro de usuarios (username, email, password)
- Perfil con nombre, apellido, email, avatar, bio, link y cumpleaños
- Edición de perfil y cambio de contraseña
- Mensajes privados entre usuarios

## Tecnologías
- Django
- django-ckeditor
- Pillow

## Configuración rápida
1. `pip install -r requirements.txt`
2. `python manage.py migrate`
3. `python manage.py runserver`

Nota: No se incluye `db.sqlite3` ni la carpeta `media/` en el repositorio.

## link al video de demostracion, valido por 30 dias: 
https://app.filmora.io/#/object/d463etcp7c8q5b1v9dp0?source=%7B%22product_id%22:%227598%22,%22product_page%22:%22share_url%22,%22product_version%22:%2214.10.5.15330%22%7D

