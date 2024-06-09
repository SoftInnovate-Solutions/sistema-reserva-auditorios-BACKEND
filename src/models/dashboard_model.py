from database.db import get_connection

class Dashboard_Model():
    
    @classmethod
    def get_reporte_ambientes(self, fecha_ini, fecha_fin):
        try:
            connection = get_connection()
            reportes_ambientes = []
            with connection.cursor() as cursor:
                cursor.execute('''
                                SELECT a.nombre_amb, COUNT(r.cod_ambiente) AS cantidad
                                FROM reserva AS r
                                JOIN ambiente AS a ON r.cod_ambiente = a.cod_ambiente
                                WHERE r.fecha_res BETWEEN %s AND %s
                                GROUP BY a.nombre_amb
                                ORDER BY cantidad DESC;
                                ''',(fecha_ini, fecha_fin))
                resultset = cursor.fetchall()
                for row in resultset:
                    reportes_ambientes.append({
                        'nombre_amb' : row[0],
                        'cantidad' : row[1]
                    })
            connection.close()
            return reportes_ambientes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_reporte_docentes(self, fecha_ini, fecha_fin):
        try:
            connection = get_connection()
            reportes_docentes = []
            with connection.cursor() as cursor:
                cursor.execute('''
                                SELECT u.nombre_usu, COUNT(r.cod_usuario) AS cantidad
                                FROM reserva AS r
                                JOIN final AS f ON f.cod_usuario = r.cod_usuario
                                JOIN usuario AS u ON u.cod_usuario = r.cod_usuario
                                WHERE r.fecha_res BETWEEN %s AND %s
                                GROUP BY u.nombre_usu
                                ORDER BY cantidad DESC;
                                ''',(fecha_ini, fecha_fin))
                resultset = cursor.fetchall()
                for row in resultset:
                    reportes_docentes.append({
                        'nombre_usu' : row[0],
                        'cantidad' : row[1]
                    })
            connection.close()
            return reportes_docentes
        except Exception as ex:
            raise Exception(ex)