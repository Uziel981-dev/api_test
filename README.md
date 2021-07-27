# API REST para consulta y guardado de "Almacen"

## Ambiente local

Solo sigue los siquientes pasos para desplegar localmente, los pasos han sido probados en un sistema linux (Ubuntu 20.04):
- pipenv -p python3.7 api_test
- source api_test/bin/activate
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py  migrate 
- python manage.py runserver

## Consumir API usando ngrok
Previa disponibilidad del API la direccion para consumir la API es:
- http://dada177aafe8.ngrok.io/almacen/


## Modelo utilizado
Se ha utilizado un unico modelo para guardar todos los campos solicitados, usando la base de datos dada por default, para consultar el diagrama de la base de datos ver el archivo; 
Crear archivo .env (en el mismo directorio donde se encuentra docker-compose.yml) con las siguientes variables de ambiente (cambie los valores de acuerdo a su ambiente): myapp_models.png de este repositorio

