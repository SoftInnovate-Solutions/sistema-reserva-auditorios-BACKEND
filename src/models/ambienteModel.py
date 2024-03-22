from database.db import get_connection
from .entities.ambiente import Ambiente

class AmbienteModel():
    @classmethod
    def get_ambientes(self):
        try:
            connection = get_connection()
            ambientes = []
            with connection.cursor() as cursor:
                cursor.execute('SELECT cod_ambiente,nombre_amb,descripcion_amb FROM ambiente;')
                resultset = cursor.fetchall()
                for row in resultset:
                    ambientes.append(Ambiente(row[0],row[1],row[2]).to_JSON())
            connection.close()
            return ambientes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_ambiente(self,id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM ambiente WHERE cod_ambiente = %s',(id,))
                row = cursor.fetchone()
                ambiente = None
                if row != None:
                    ambiente = Ambiente(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    ambiente = ambiente.to_JSON()
                connection.close()
                return ambiente
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_ambiente(self,ambiente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO ambiente (nombre_amb,capacidad_amb,ubicacion_amb,descripcion_amb,cod_estado_ambiente,cod_piso,
                    cod_edificio,cod_facultad,cod_tipo_ambiente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
                    ambiente.nombre_amb,int(ambiente.capacidad_amb),ambiente.ubicacion_amb,ambiente.descripcion_amb,
                    int(ambiente.cod_estado_ambiente),int(ambiente.cod_piso),int(ambiente.cod_edificio),int(ambiente.cod_facultad),
                    int(ambiente.cod_tipo_ambiente)
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_ambiente(self,ambiente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM ambiente WHERE cod_ambiente = %s',(ambiente.cod_ambiente))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_ambiente(self,ambiente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''UPDATE ambiente SET 
                nombre_amb = %s, capacidad_amb = %s, ubicacion_amb = %s, descripcion_amb = %s, cod_estado_ambiente = %s, 
                cod_piso = %s, cod_edificio = %s, cod_facultad = %s, cod_tipo_ambiente = %s WHERE cod_ambiente = %s
                ''', (ambiente.nombre_amb,int(ambiente.capacidad_amb),ambiente.ubicacion_amb,ambiente.descripcion_amb,int(ambiente.cod_estado_ambiente),
                int(ambiente.cod_piso),int(ambiente.cod_edificio),int(ambiente.cod_facultad),int(ambiente.cod_tipo_ambiente),int(ambiente.cod_ambiente)
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
