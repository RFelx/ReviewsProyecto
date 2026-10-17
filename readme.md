Recordar que es necesario tener Docker instalado

Pasos de instalacion

1 - Crear entorno virtual:
Esto se puede hacer con "python -m venv .venv"

2 - Activar entorno virtual:
Dentro de la carpeta del entorno puedes usar "Scripts\activate"

3 - Instalar dependencias:
Para esto puedes usar el comando "pip install -r requirements.txt"

4 - completar informacion en settings:
Alguna informacion fue removida dentro de settings, especificamente informacion de las credenciales de la base de datos y la secret key

5 - Levantar base de datos en Docker:
aprovecha el comando "docker compose up -d", recordar que algunos datos faltan en la informacion de usuario, contrasena y nombre de la base de datos del docker-compose.yml, asi que se deben rellenar esos datos.

6 - Realizar migraciones
Esto se puede realizar con los comandos "python manage.py makemigrations" y luego con "python manage.py migrate"

A este punto ya todo deberia estar listo y se deberia poder correr el server sin problemas.

"python manage.py runserver"