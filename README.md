# Titulo

### Descripcion:
El proyecto consiste en una aplicacion wep para poder realizar reservar de ambientes esto permitira que los usuario puedan realizarlos de una manera mas rapida.
### Herramientas a instalar:
* Postgres 16
* Python 3.12.0
* Visual Studio Code
### Preparacion de entorno de trabajo
1. Verificar que el archivo ```.env``` tenga los mismos datos que su postgres instalado en caso de que varien los datos usted podra cambiar la informacion del archivo ```.env``` a la que tiene definido su postgres, no obstante no cambie el valor de ```SECRET_KEY```, ```PGSQL_HOST```, ```PGSQL_DATABASE``` por ningun motivo.
2. Instalar el entorno vistual en la carpeta backend, el comando para ello es ```python -m venv venv```, todo esto en la terminal de ``visual studio code``.
3. Habilitar el entorno de trabajo, el comando para ello es ```venv\Scripts\activate```, todo esto en la terminal de ``visual studio code``.
4. Instalar el archivo ```requirements.txt``` esto con el objetivo de tener todas las librerias necesarias, el comando para ello es ```pip install -r requirements.txt```, todo esto en la terminal de ``visual studio code``.
5. Cree la base de datos en ```sistemareservadb``` de postgres 16, para ello el comando se encuentra en ```src\database\1_creator_database.sql```.
6. Cree las tablas y relaciones de la base datos en ```sistemareservadb```, para ello el comando se encuentra en ```src\database\2_creator_tables.sql```.
7. Inserte los datos precargados en ```sistemareservadb```, para ello el comando se encuentra en ```src\database\3_insert_dates.sql```.
8. Finalmente levante el servidor con el comando ```python src\app.py```, todo esto en la terminal de ``visual studio code``.

### Endpoints definidos
Estas no son mas que las rutas para consumir cierto recurso de la api rest.
* ruta: ``http://127.0.0.1:5000/piso/all``, nos proporciona la informacion de todos los pisos registrados en la base de datos.

* ruta: ``http://127.0.0.1:5000/edificacion/all``, nos proporciona la informacion de todos las edificaciones registrados en la base de datos.

* ruta: ``http://127.0.0.1:5000/facultad/all``, nos proporciona la informacion de todas las facultades registradas en la base de datos.

* ruta: ``http://127.0.0.1:5000/estado_ambiente/all``, nos proporciona la informacion de todos los estados de ambientes registrados en la base de datos.

* ruta: ``http://127.0.0.1:5000/tipo_ambiente/all``, nos proporciona la informacion de todos los tipos de ambientes registrados en la base de datos.

* ruta: ``http://127.0.0.1:5000/ambiente/all``, nos proporciona la informacion de todos los ambientes registrados en la base de datos.
* ruta: ``http://127.0.0.1:5000/ambiente/one/id``, nos proporciona la informacion de un ambiente registrado en la base de datos.
* ruta: ``http://127.0.0.1:5000/ambiente/add``, agrega un nuevo ambiente a la base de datos.
* ruta: ``http://127.0.0.1:5000/ambiente/delete/id``, elimina un ambiente de la base de datos.
* ruta: ``http://127.0.0.1:5000/ambiente/update/id``, actualiza un ambiente de la base de datos.
* ruta: ``http://127.0.0.1:5000/ambiente/filter/"filtro"``, nos proporciona la informacion de todos los ambientes registrados en la base de datos pero con la diferencia de realizar filtrados, para ello se recomienda usar este formato de string ``"1,2,9,-1"`` donde ``-1`` indica que no se esta filtrando por ese parametro, el primer parametro es ``Tipo de ambiente``, el segundo es ``Facultad``, el tercero es ``Edificio`` y el ultimo es ``Estado``.
* ruta: ``http://127.0.0.1:5000/ambiente/one_setting/id_ambiente``, obtienes solo la albergacion maxima y la minima.
* ruta: ``http://127.0.0.1:5000/ambiente/update_setting/id_ambiente``, actualizas solo la albergacion maxima y la minima.

* ruta: ``http://127.0.0.1:5000/ajuste_ambiente/addUpdate``, nos permite insertar todos los registrios de disponibilidad de un ambiente en especifico para ello se tiene que mandar un json del siguiente formato:
{
  ``"cod_ambiente": 2``,
  ``"configuracion": [
    [1,0,1,0,0,0,1],
    [0,0,0,1,0,0,0],
    [1,0,1,0,0,0,1],
    [0,0,0,1,0,0,0],
    [1,0,1,0,0,0,1],
    [0,0,0,1,0,0,0],
    [1,0,1,0,0,0,1],
    [0,0,0,1,0,0,0],
    [1,0,1,0,0,0,1],
    [0,0,0,1,1,0,0]
  ]``,
  ``fecha_inicio_general_per": "2024-05-01``,
  ``fecha_fin_general_per": "2024-07-10``
}
Cabe recalcar que la matriz solo tiene que ser de ``10 x 7`` y sus valores tienen que ser ``1`` para habilitar el bloque y ``0`` para no abilitar el bloque.
* ruta: ``http://127.0.0.1:5000/ajuste_ambiente/deleteAll``, eliminara todos los registros de nuestra tabla ajuste_ambiente.
* ruta: ``http://127.0.0.1:5000/ajuste_ambiente/get_ajuste_ambiente/id_ambiente``, obtienes la configuracion del ajuste del ambiente.

* ruta: ``http://127.0.0.1:5000/final/iniciar_sesion``, permite iniciar sesion al usuario final, cabe recalcar que se tiene que enviar el nombre de usuario, la contrasenia, el codigo sis y el codigo de tipo final todo esto en un json.

* ruta: ``http://127.0.0.1:5000/administrador/iniciar_sesion``, permite iniciar sesion al usuario administrador, cabe recalcar que se tiene que enviar el nombre de usuario, la contrasenia y el alias todo esto en un json.

* ruta: ``http://127.0.0.1:5000/periodo_reserva/periodo_general``, permite obtener el codigo del periodo y las fechas generales como inicio y fin en caso contrario de que no exista un periodo devuelve una json vacio
* ruta: ``http://127.0.0.1:5000/periodo_reserva/add``, permite agregar los datos del periodo de las reservas
{
  "fecha_inicio_general_per": "2024-05-12",
  "fecha_fin_general_per": "2024-06-12",
  "fecha_inicio_docente_per": "2024-05-15",
  "fecha_fin_docente_per": "2024-06-15",
  "fecha_inicio_auxiliar_per": "2024-05-18",
  "fecha_fin_auxiliar_per": "2024-06-18",
  "notificacion_per": "2024-05-12 08:30:00"
}
* ruta: ``http://127.0.0.1:5000/periodo_reserva/delete/1``, permite eliminar el periodo unico mediante su cod_periodo
* ruta: ``http://127.0.0.1:5000/periodo_reserva/periodo_docente``, se obtiene un parametro para indicar si el docente podra realizar una reserva y tambien se obtiene las fechas de tal periodo
* ruta: ``http://127.0.0.1:5000/periodo_reserva/periodo_auxiliar``, se obtiene un parametro para indicar si el auxiliar realizar una reserva y tambien se obtiene las fechas de tal periodo

* ruta: ``http://127.0.0.1:5000/reserva/all/id_usuario``, se obtiene todas las reservas del usuario
* ruta: ``http://127.0.0.1:5000/reserva/delete/id_reserva``, elimina la reserva seleccionada
* ruta: ``http://127.0.0.1:5000/reserva/one/id_reserva``, obtienes la reserva seleccionada
Paso 1
* ruta: ``http://127.0.0.1:5000/reserva/imparticiones/id_usuario``, obtienes todas las imparticiones del usuario final ya sea docente o auxiliar obtienes cod_materia y cod_grupo
Paso 2
* ruta: ``http://127.0.0.1:5000/reserva/ambientes_disponibles/cantidad``, obtenemos el cod_ambiente y el nombre del ambiente
Paso 3
* ruta: ``http://127.0.0.1:5000/reserva/get_calendario/id_ambiente``, obtenemos las fechas para el calendario
Paso 4
* ruta: ``http://127.0.0.1:5000/reserva/get_calendario``, con un json que contenga el cod_ambiente y la fecha extraida se obtiene los cod_dia, los cod_bloque y sus correspondientes nombres
Paso 5
* ruta: ``http://127.0.0.1:5000/reserva/add_reserva``, con un json que contenga el siguiente formato se registrara una nueva reserva
{
  "cod_usuario": 2,
  "cod_grupo": 1,
  "cod_materia": 2,
  "cod_ambiente": 10,
  "cod_dia": 1,
  "cod_bloque": 3,
  "fecha_res": "2024-07-01"
}
* ruta: ``http://127.0.0.1:5000/reserva/get_history_all``, obtienes todas las reservas realizadas
* ruta: ``http://127.0.0.1:5000/reserva/get_history_one/<id>``, obtienes la informacion de la reserva realizada

* ruta: ``http://127.0.0.1:5000/dashboard/reporte_ambientes``, obtienes todos los reportes de los ambientes
{
  "fecha_inicio" : YYYY-MM-DD,
  "fecha_fin" : YYYY-MM-DD
}
* ruta: ``http://127.0.0.1:5000/dashboard/reporte_docentes``, obtienes todos los reportes de los docentes
{
  "fecha_inicio" : YYYY-MM-DD,
  "fecha_fin" : YYYY-MM-DD
}

