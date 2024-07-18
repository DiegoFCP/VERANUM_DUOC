# Proyecto DUOUC
## _Poryecto en python y django Hotel_

[![N|Solid](https://cdn-icons-png.flaticon.com/128/919/919852.png)]()

[![N|Solid](https://cdn-icons-png.flaticon.com/128/9307/9307630.png)]()

## versiones
- python 3.12.3
- entorno virtual seleccionado 'virtualenv'



## Instalacion y ejecucion
Descargar repositorio en un directorio de trabajo
```sh
git clone https://github.com/DiegoFCP/VERANUM_DUOC.git
```

entrar al directorio
```sh
cd VERANUM_DUOC
```
crear un entorno virtual
```sh
virtualenv env
```
iniciar el entorno virtual
```sh
./env/scripts/activate
```
se debe instalar los paquetes requeridos
```sh
pip install -r requirements.txt
```
abrir el edictor de codigo y ejecutar el motor de base de datos, en nuestro caso utilizamos mariadb o se puede usar cualquier otro motor de base de datos relacionales

-abrir el editor de codigo (visual studio code)
```sh
code .
```

ajustar los parametros de la conexion a la base de datos, abriendo el archivo, en el directorio
```sh
proyecto1/setings.py
```
configurar la base de datos, en este caso se utilizo 'inventoryweb', verificar el puerto correcto 3306,
verificar usuario y password
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'inventoryweb',
        'USER': 'tu-usuario',
        'PASSWORD': 'tu-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

se deben crear las migraciones y ejecutarlas
```sh
python ./manage.py makemigrations
python ./manage.py migrate
```

se deben ejecutar los seeders, para ver los registros
```sh
python ./manage.py seed_habitaciones
python ./manage.py seed_hoteles
python ./manage.py seed_serv_extras
```

se debe crear un usuario superuser, llenar con los datos de usuario, email, passord que ud requiera
```sh
python ./manage.py createsuperuser
```

correr el servidor
```sh
python ./manage.py runserver
```
para entrar al admin
```sh
http://127.0.0.1:8000/admin
```

```sh
se debe asignar en el admin habitaciones a los hoteles 
 ${habitaciones a los hoteles } .
```
