from database.db import get_connection
from .entities.periodo_reserva import Periodo_Reserva

class PeriodoModel():


    @classmethod
    def get_periodos_all(self):
        try:
            connection = get_connection()
            periodos = []
            with connection.cursor() as cursor:
                cursor.execute('SELECT cod_periodo,fecha_inicio_per,fecha_fin_per FROM periodo;')
                resultset = cursor.fetchall()
                for row in resultset:
                    periodos.append(Periodo_Reserva(row[0],row[1],row[2]).to_JSON())
            connection.close()
            return periodos
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_periodo_one(self,id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('SELECT cod_periodo,fecha_inicio_per,fecha_fin_per FROM periodo WHERE cod_periodo = %s;',(id,))
                row = cursor.fetchone()
                periodo = None
                if row != None:
                    periodo = Periodo_Reserva(row[0],row[1],row[2])
                    periodo = periodo.to_JSON()
                connection.close()
                return periodo
        except Exception as ex:
            raise Exception(ex)






    @classmethod
    def add_periodo(self,periodo):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                    INSERT INTO periodo_reserva 
                    (
                    fecha_inicio_general_per, fecha_fin_general_per, fecha_inicio_docente_per, fecha_fin_docente_per,
                    fecha_inicio_auxiliar_per, fecha_fin_auxiliar_per, notificacion_per, estado_visualizacion_per
                    ) 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                ''',(periodo.fecha_inicio_general_per, periodo.fecha_fin_general_per, periodo.fecha_inicio_docente_per, 
                     periodo.fecha_fin_docente_per, periodo.fecha_inicio_auxiliar_per, periodo.fecha_fin_auxiliar_per, 
                     periodo.notificacion_per, periodo.estado_visualizacion_per)) 
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_periodo(self,periodo):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                    UPDATE periodo_reserva 
                    SET fecha_inicio_general_per = %s, fecha_fin_general_per = %s, fecha_inicio_docente_per = %s, 
                        fecha_fin_docente_per = %s, fecha_inicio_auxiliar_per = %s, fecha_fin_auxiliar_per = %s,
                        notificacion_per = %s
                    WHERE cod_periodo_reserva = %s;
                ''',(periodo.fecha_inicio_general_per, periodo.fecha_fin_general_per, periodo.fecha_inicio_docente_per, 
                     periodo.fecha_fin_docente_per, periodo.fecha_inicio_auxiliar_per, periodo.fecha_fin_auxiliar_per, 
                     periodo.notificacion_per, periodo.cod_periodo_reserva))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_periodo_general(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                    SELECT cod_periodo_reserva, fecha_inicio_general_per, fecha_fin_general_per
                    FROM periodo_reserva
                    WHERE estado_visualizacion_per = TRUE
                    LIMIT 1;
                ''')
                result = cursor.fetchone()
            if result is not None:
                return Periodo_Reserva(cod_periodo_reserva = result[0],fecha_inicio_general_per = result[1],fecha_fin_general_per = result[2]).to_JSONGENERAL()
            connection.close()
            return {}
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_periodo_docente(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                    SELECT COUNT(cod_periodo_reserva)
                    FROM periodo_reserva
                    WHERE estado_visualizacion_per = TRUE AND CURRENT_DATE BETWEEN fecha_inicio_docente_per AND fecha_fin_docente_per
                    LIMIT 1;
                ''')
                result = cursor.fetchone()
            if result is not None:
                return {'existe' : result[0], 'rol' : 1}
            connection.close()
            return {'existe' : 0}
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_periodo_auxiliar(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                    SELECT COUNT(cod_periodo_reserva)
                    FROM periodo_reserva
                    WHERE estado_visualizacion_per = TRUE AND CURRENT_DATE BETWEEN fecha_inicio_auxiliar_per AND fecha_fin_auxiliar_per
                    LIMIT 1;
                ''')
                result = cursor.fetchone()
            if result is not None:
                return {'existe' : result[0], 'rol' : 2}
            connection.close()
            return {'existe' : 0}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_periodo(self,periodo_reserva):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM periodo_reserva WHERE cod_periodo_reserva = %s',(periodo_reserva.cod_periodo_reserva))
                affected_rows_periodo = cursor.rowcount
                cursor.execute('DELETE FROM ajuste_ambiente;')
                affected_rows_detalle_periodo = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows_periodo + affected_rows_detalle_periodo
        except Exception as ex:
            raise Exception(ex)

