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
                print(resultset)
                for row in resultset:
                    reservas.append(Reserva(cod_reserva=row[0],cod_ambiente=row[1],cod_materia=row[2],cod_grupo=row[3],fecha_res=row[4],cod_bloque=row[5]))
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