# Módulo: Autenticación Personalizada — book-course-django-customauth

Este README se centra exclusivamente en la implementación de un módulo de usuario personalizado (login) dentro del repositorio [`book-course-django-customauth`](https://github.com/libredesarrollo/book-course-django-customauth), basada en lo expuesto en el módulo “Módulo de usuario y autenticación en Django” del curso de Desarrollolibre:contentReference[oaicite:1]{index=1}.


https://www.desarrollolibre.net/blog/python/curso-django

https://www.desarrollolibre.net/libros/primeros-pasos-django

---

## 1. Descripción del módulo

Se desarrolla desde cero un sistema de autenticación personalizado usando Django, que supera las opciones genéricas incluye vistas, formularios, rutas y lógica de autenticación adaptada a requisitos específicos de la aplicación.

---

## 2. Instalación y configuración

1. **Instalar dependencias**: Asegúrate de incluir en `INSTALLED_APPS`:
   ```python
   INSTALLED_APPS = [
       ...,
       'django.contrib.auth',
       'django.contrib.sessions',
       ...
   ]
