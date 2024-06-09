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
                                WHERE cod_grupo = %s AND cod_materia = %s AND cod_materia = %s;
                                ''',(row[7],row[8],row[9]))
                    cantidad = cursor.fetchone()

            connection.close()
            if row is not None:
                return Reserva(cod_reserva=row[0],cod_ambiente=row[1],cod_materia=row[2],cod_grupo=row[3],fecha_res=row[4],cod_bloque=row[5],cod_usuario=row[6]).to_JSONONE(cantidad[0])
            return {}
            
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_imparticiones(self,id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                SELECT CONCAT(TRIM(m.nombre_mat),' - ',TRIM(g.nombre_gru)) AS imparticion, i.cantidad_estudiantes_imp, g.cod_grupo, m.cod_materia, i.cod_imparticion
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
                    imparticiones.append(Reserva(cod_grupo=row[2], cod_materia=row[3]).to_JSONIMPARTICION(row[0],row[1],row[4]))
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
                WHERE %s BETWEEN a.albergacion_min_amb AND a.albergacion_max_amb AND a.cod_estado_ambiente = 1
                EXCEPT
                SELECT r.cod_ambiente, r.cod_dia, r.cod_bloque, r.fecha_res, amb.nombre_amb 
                FROM reserva AS r
                JOIN ambiente AS amb ON amb.cod_ambiente = r.cod_ambiente;
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

    @classmethod    
    def get_calendario(self,id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                SELECT cod_dia, cod_bloque,  CONCAT(nombre_blo,': ', hora_inicio_blo,' - ',hora_fin_blo) AS nombre
                                FROM (
                                SELECT aa.cod_ambiente, aa.cod_dia, aa.cod_bloque, aa.fecha_aa, b.nombre_blo, b.hora_inicio_blo,b.hora_fin_blo
                                FROM ajuste_ambiente AS aa
                                JOIN bloque AS b ON b.cod_bloque = aa.cod_bloque
                                WHERE aa.cod_ambiente = %s AND aa.fecha_aa = %s
                                EXCEPT
                                SELECT r.cod_ambiente, r.cod_dia, r.cod_bloque, r.fecha_res,blo.nombre_blo, bb.hora_inicio_blo,bb.hora_fin_blo
                                FROM reserva AS r
                                JOIN bloque AS blo ON blo.cod_bloque = r.cod_bloque
                                ) AS subconsulta_externa
                                ORDER BY nombre_blo;
                                ''',(id,))
                rows = cursor.fetchall()
            connection.close()
            if rows is not None:
                fechas = []
                for row in rows:
                    fechas.append(Reserva(fecha_res=row[3]).to_JSONCALENDARIO())
                return fechas
            return {}
            
        except Exception as ex:
            raise Exception(ex)    

    @classmethod    
    def get_bloque(self,cod_ambiente, fecha_aa):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                SELECT cod_dia, cod_bloque,  CONCAT(nombre_blo,': ', hora_inicio_blo,' - ',hora_fin_blo) AS nombre
                FROM (
                SELECT aa.cod_ambiente, aa.cod_dia, aa.cod_bloque, aa.fecha_aa, b.nombre_blo, b.hora_inicio_blo,b.hora_fin_blo
                FROM ajuste_ambiente AS aa
                JOIN bloque AS b ON b.cod_bloque = aa.cod_bloque
                WHERE aa.cod_ambiente = %s AND aa.fecha_aa = %s
                EXCEPT
                SELECT r.cod_ambiente, r.cod_dia, r.cod_bloque, r.fecha_res,'', '00:00','00:00'
                FROM reserva AS r
                ) AS subconsulta_externa
                ORDER BY nombre_blo;
                                ''',(cod_ambiente, fecha_aa))
                rows = cursor.fetchall()
            connection.close()
            if rows is not None:
                conjuntos = []
                for row in rows:
                    conjuntos.append(Reserva(cod_dia=row[0],cod_bloque=row[1]).to_JSONDIABLOQUE(nombre_blo=row[2]))
                return conjuntos
            return {}
            
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_reserva(self,cod_usuario, cod_grupo, cod_materia, cod_ambiente, cod_dia, cod_bloque, fecha_res, cantidad_estudiantes_res, cantidad_estudiantes_res_total):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                            INSERT INTO 
                            reserva ( cod_usuario, cod_grupo, cod_materia, cod_ambiente, cod_dia, cod_bloque, fecha_res , cantidad_estudiantes_res, cantidad_estudiantes_total_res)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
                                ''', (
                                    cod_usuario, cod_grupo, cod_materia, cod_ambiente, cod_dia, cod_bloque, fecha_res, cantidad_estudiantes_res, cantidad_estudiantes_res_total
                            ))
                affected_row = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_row
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod    
    def get_history_all(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                SELECT r.cod_reserva, a.nombre_amb, CONCAT(b.hora_inicio_blo,' - ',b.hora_fin_blo), r.fecha_res
                FROM reserva AS r
                JOIN bloque AS b ON r.cod_bloque = b.cod_bloque
                JOIN ambiente AS a ON r.cod_ambiente = a.cod_ambiente
                ORDER BY fecha_res DESC, b.hora_inicio_blo ASC;
                                ''')
                rows = cursor.fetchall()
            connection.close()
            if rows is not None:
                conjuntos = []
                for row in rows:
                    conjuntos.append(Reserva(cod_reserva=row[0],cod_ambiente=row[1],cod_bloque=row[2],fecha_res=row[3]).to_JSONHISTORIALALL())
                return conjuntos
            return {}
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod    
    def get_history_one(self,cod_reserva):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                        SELECT f.codigo_sis_fin, u.nombre_usu, a.nombre_amb, e.nombre_edi, fa.nombre_fac, r.fecha_res, 
                        CONCAT(b.hora_inicio_blo,' - ',b.hora_fin_blo) AS horario
                        FROM reserva AS r
                        JOIN usuario AS u ON r.cod_usuario = u.cod_usuario
                        JOIN final AS f ON u.cod_usuario = f.cod_usuario
                        JOIN ambiente AS a ON r.cod_ambiente = a.cod_ambiente
                        JOIN edificacion AS e ON a.cod_edificacion = e.cod_edificacion
                        JOIN facultad AS fa ON a.cod_facultad = fa.cod_facultad
                        JOIN bloque AS b ON r.cod_bloque = b.cod_bloque
                        WHERE cod_reserva = %s;
                                ''',(cod_reserva,))
                row = cursor.fetchone()
            connection.close()
            return Reserva(fecha_res=row[5],cod_bloque=row[6]).to_JSONHISTORYONE(row[0],row[1],row[2],row[3],row[4])
            
        except Exception as ex:
            raise Exception(ex)