# ong_web--PS6116-ene-mar21
Sistema para la ONG +Verde +Humana el cual tiene como función princiapl llevar un mejor control del ingreso y egreso del agua y los productos que manejan, (comida, productos de mantenimiento, maquinarias), en los disitntos puntos de distribución que estos manejan. 

## Sistema +Verde +Humano
Este proyecto fue generado en Django v3.1.5

## Clonar el repositorio e instalar los requerimientos
git clone https://github.com/gonzalez0fer/ong_web--PS6116-ene-mar21.git

pip install -r requirements.txt

## Crear una base de datos en SQL
sudo -i -u postgres

psql

create database ong_db

Colocar en el archivo .env el usuario y contraseña de postgres

## Realizar las migraciones de python
python manage.py makemigrations

python manage.py migrate 

## Crear un usuario administrador en el sistema
python manage.py create superuser

## Correr en el servidor 
python manage.py runserver

## Funcionalidades
1. Gestión de inventarios de:
- Agua
- Productos de mantenimiento 
- Alimentos
- Equipos

2. Gestión de mantenimientos
3. Control de acceso

## Dependencias
- asgiref==3.3.1
- certifi==2020.12.5
- Django==3.1.5
- django-environ==0.4.5
- django-extra-views==0.13.0
- django-model-utils==4.1.1
- django-widget-tweaks==1.4.8
- psycopg2-binary==2.8.6
- pytz==2020.5
- request==2.25.1
- six==1.15.0
- sqlparse==0.4.1

## Integrantes
Fernando González
Juan Diego Porras
Javier Vivas
Victoria Torres
Pablo González
Maria F. Machado
Pedro Maldonado
