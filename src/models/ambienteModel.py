from database.db import get_connection
from .entities.ambiente import Ambiente
from utils.transformacion import Transformacion
from utils.generador import Generador

from .entities.imparticion import Imparticion

class AmbienteModel():
    @classmethod
    def get_ambientes_all(self):
        try:
            connection = get_connection()
            ambientes = []
            with connection.cursor() as cursor:
                cursor.execute('SELECT a.cod_ambiente, a.nombre_amb, e.nombre_ea,a.albergacion_min_amb, a.capacidad_amb, a.albergacion_max_amb From ambiente a JOIN estado_ambiente e ON a.cod_estado_ambiente = e.cod_estado_ambiente;')
                resultset = cursor.fetchall()
                for row in resultset:
                    ambientes.append(Ambiente(cod_ambiente=row[0],nombre_amb=row[1],cod_estado_ambiente=row[2],albergacion_min_amb=row[3],capacidad_amb=row[4],albergacion_max_amb=row[5]).to_JSONALL())
            connection.close()
            return ambientes
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_imparticion_all(cls):
        try:
            connection = get_connection()
            imparticion = []
            with connection.cursor() as cursor:
                cursor.execute('''
                    SELECT 
                        u.NOMBRE_USU AS nombreUsuario, m.NOMBRE_MAT AS materia, 
                        g.NOMBRE_GRU AS grupo, i.CANTIDAD_ESTUDIANTES_IMP AS cantidad_estudiantes
                    FROM imparticion i
                    JOIN usuario u ON i.COD_USUARIO = u.COD_USUARIO
                    JOIN materia m ON i.COD_MATERIA = m.COD_MATERIA
                    JOIN grupo g ON i.COD_GRUPO = g.COD_GRUPO;
                ''')
                resultset = cursor.fetchall()
                for row in resultset:
                    imparticion.append(Imparticion(row[0], row[1], row[2], row[3]).to_JSONALL())
            connection.close()
            return imparticion
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_ambientes_filter(self,filtro):
        pFiltro = Transformacion.convertirTuplaFiltraddor(filtro)
        sql = Generador.generadorSql(pFiltro)
        try:
            connection = get_connection()
            ambientes = []
            with connection.cursor() as cursor:
                cursor.execute(sql)
                resultset = cursor.fetchall()
                for row in resultset:
                    ambientes.append(Ambiente(cod_ambiente=row[0], nombre_amb=row[1],cod_estado_ambiente=row[2],capacidad_amb=row[3]).to_JSONALL())
            connection.close()
            return ambientes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_ambiente_one(self,id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('SELECT cod_ambiente, nombre_amb, capacidad_amb, ubicacion_amb, descripcion_amb, cod_facultad, cod_estado_ambiente, cod_piso, cod_tipo_ambiente, cod_edificacion FROM ambiente WHERE cod_ambiente = %s',(id,))
                row = cursor.fetchone()
                ambiente = None
                if row != None:
                    ambiente = Ambiente(cod_ambiente=row[0],nombre_amb=row[1],capacidad_amb=row[2],ubicacion_amb=row[3],descripcion_amb=row[4],cod_facultad=row[5],cod_estado_ambiente=row[6],cod_piso=row[7],cod_tipo_ambiente=row[8],cod_edificacion=row[9])
                    ambiente = ambiente.to_JSONONE()
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
                    INSERT INTO 
                    ambiente (nombre_amb,capacidad_amb,ubicacion_amb,descripcion_amb,albergacion_max_amb,albergacion_min_amb,cod_estado_ambiente,cod_piso,
                    cod_edificacion,cod_facultad,cod_tipo_ambiente) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
                    ambiente.nombre_amb, ambiente.capacidad_amb, ambiente.ubicacion_amb, ambiente.descripcion_amb, ambiente.albergacion_max_amb, ambiente.albergacion_min_amb,
                    int(ambiente.cod_estado_ambiente), int(ambiente.cod_piso), int(ambiente.cod_edificacion), int(ambiente.cod_facultad),
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
                cursor.execute('DELETE FROM ambiente WHERE cod_ambiente = %s',(ambiente.cod_ambiente,))
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
                cod_piso = %s, cod_edificacion = %s, cod_facultad = %s, cod_tipo_ambiente = %s WHERE cod_ambiente = %s
                ''', (ambiente.nombre_amb,ambiente.capacidad_amb,ambiente.ubicacion_amb,ambiente.descripcion_amb,int(ambiente.cod_estado_ambiente),
                int(ambiente.cod_piso),int(ambiente.cod_edificacion),int(ambiente.cod_facultad),int(ambiente.cod_tipo_ambiente),int(ambiente.cod_ambiente)
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_one_setting(self,id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('SELECT cod_ambiente, albergacion_max_amb, albergacion_min_amb, capacidad_amb FROM ambiente WHERE cod_ambiente = %s',(id,))
                row = cursor.fetchone()
                ambiente = None
                if row != None:
                    ambiente = Ambiente(cod_ambiente=row[0],albergacion_max_amb=row[1],albergacion_min_amb=row[2],capacidad_amb=row[3])
                    ambiente = ambiente.to_JSONSETTING()
                connection.close()
                return ambiente
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_setting_ambiente(self,ambiente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                               UPDATE ambiente 
                               SET albergacion_max_amb = %s, albergacion_min_amb = %s 
                               WHERE cod_ambiente = %s
                ''', (int(ambiente.albergacion_max_amb), int(ambiente.albergacion_min_amb), int(ambiente.cod_ambiente)
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)



