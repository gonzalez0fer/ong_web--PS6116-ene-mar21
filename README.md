# ong_web--PS6116-ene-mar21

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
