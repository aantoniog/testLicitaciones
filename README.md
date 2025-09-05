Proyecto CRUD de Licitaciones

Este proyecto es un CRUD sencillo en Django para gestionar licitaciones.
Permite crear, ver, editar y borrar licitaciones con los siguientes campos:

  Nombre
  Fecha de inicio
  Fecha de fin
  Monto
  Estado
  Proveedor

1. Instalación y ejecución

Clonar el repositorio
git clone https://github.com/aantoniog/testLicitaciones.git
cd licitaciones_project

2. Crear entorno virtual dentro de la carpeta

  python -m venv venv
  source venv/bin/activate   # Linux / Mac
  venv\Scripts\activate      # Windows

3. Instalar Django

   pip install django

4. Aplicar migraciones

   python manage.py makemigrations
   python manage.py migrate

5. Levantar el servidor

   python manage.py runserver


Arquitectura del proyecto
App principal: licitaciones
Modelo: Licitacion con los campos solicitados
Vistas: CRUD
Templates: HTML bootstrap
Base de datos: SQLite

El CRUD usa 3 plantillas muy simples:
lista.html → Muestra todas las licitaciones y botones para editar/borrar.
form.html → Formulario para crear o editar una licitación.
confirmar_borrar.html → Pantalla de confirmación antes de eliminar.

Si ocurre el error "no such table" aplicar migraciones
  python manage.py makemigrations
  python manage.py migrate




