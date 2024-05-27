from database.db import get_connection
from .entities.reserva import Reserva

class ReservaModel():
    @classmethod
    def get_reservas(self,id):
        try:
            connection = get_connection()
            reservas = []
            with connection.cursor() as cursor:
                cursor.execute('''
                                SELECT r.cod_reserva, a.nombre_amb, m.nombre_mat, g.nombre_gru, r.fecha_res, CONCAT(b.hora_inicio_blo,' - ',b.hora_fin_blo) as horario
                                FROM reserva AS r
                                JOIN ambiente AS a ON r.cod_ambiente = a.cod_ambiente
                                JOIN materia AS m ON r.cod_materia = m.cod_materia
                                JOIN grupo AS g ON r.cod_grupo = g.cod_grupo
                                JOIN bloque AS b ON r.cod_bloque = b.cod_bloque
                                WHERE r.cod_usuario = %s;
                                ''',(id,))
                resultset = cursor.fetchall()
                for row in resultset:
                    reservas.append(Reserva(cod_reserva=row[0],cod_ambiente=row[1],cod_materia=row[2],cod_grupo=row[3],fecha_res=row[4],cod_bloque=row[5]).to_JSONALL())
            connection.close()
            return reservas
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_reserva(self,reserva):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM reserva WHERE cod_reserva = %s',(reserva.cod_reserva,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_reserva(self,id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                SELECT r.cod_reserva, a.nombre_amb, m.nombre_mat, g.nombre_gru, r.fecha_res, CONCAT(b.hora_inicio_blo,' - ',b.hora_fin_blo) as horario, u.nombre_usu, r.cod_grupo, r.cod_materia, r.cod_usuario
                                FROM reserva AS r
                                JOIN ambiente AS a ON r.cod_ambiente = a.cod_ambiente
                                JOIN materia AS m ON r.cod_materia = m.cod_materia
                                JOIN grupo AS g ON r.cod_grupo = g.cod_grupo
                                JOIN bloque AS b ON r.cod_bloque = b.cod_bloque
                                JOIN usuario AS u ON r.cod_usuario = u.cod_usuario
                                WHERE r.cod_reserva = %s;
                                ''',(id,))
                row = cursor.fetchone()

                if row is not None:

                    cursor.execute('''
                                SELECT cantidad_estudiantes_imp
                                FROM imparticion
                                WHERE cod_usuario = %s AND cod_materia = %s AND cod_grupo = %s;
                                ''',(row[7],row[8],row[9]))
                    cantidad = cursor.fetchone()

            connection.close()
            if row is not None:
                return Reserva(cod_reserva=row[0],cod_ambiente=row[1],cod_materia=row[2],cod_grupo=row[3],fecha_res=row[4],cod_bloque=row[5],cod_usuario=row[6]).to_JSONONE(cantidad)
            return {}
            
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_imparticiones(self,id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                SELECT CONCAT(TRIM(m.nombre_mat),' - ',TRIM(g.nombre_gru)) AS imparticion, cantidad_estudiantes_imp, g.cod_grupo, m.cod_materia
                FROM imparticion AS i
                JOIN materia AS m ON i.cod_materia = m.cod_materia
                JOIN grupo AS g ON i.cod_grupo = g.cod_grupo
                WHERE cod_usuario = %s;
                                ''',(id,))
                rows = cursor.fetchall()
            connection.close()
            if rows is not None:
                imparticiones = []
                for row in rows:
                    imparticiones.append(Reserva(cod_grupo=row[2], cod_materia=row[3]).to_JSONIMPARTICION(row[0],row[1]))
                return imparticiones
            return {}
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod    
    def get_ambientes_disponibles(self,cantidad):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                SELECT DISTINCT ON (aa.cod_ambiente) 
                aa.cod_ambiente,aa.cod_dia,aa.cod_bloque,aa.fecha_aa,a.nombre_amb
                FROM ajuste_ambiente AS aa
                JOIN ambiente AS a ON a.cod_ambiente = aa.cod_ambiente
                WHERE 
                %s BETWEEN  a.capacidad_amb - a.capacidad_amb::DOUBLE PRECISION * (a.albergacion_min_amb::DOUBLE PRECISION / 100) 
                AND a.capacidad_amb::DOUBLE PRECISION * (a.albergacion_max_amb::DOUBLE PRECISION / 100)
                EXCEPT
                SELECT cod_ambiente, cod_dia, cod_bloque, fecha_res, '' 
                FROM reserva;
                                ''',(cantidad,))
                rows = cursor.fetchall()
            connection.close()
            if rows is not None:
                ambientes = []
                for row in rows:
                    ambientes.append(Reserva(cod_ambiente=row[0]).to_JSONAMBIENTESDISPONIBLES(row[4]))
                return ambientes
            return {}
            
        except Exception as ex:
            raise Exception(ex)

    
