from database.db import get_connection
from .entities.ajuste_ambiente import Ajuste_Ambiente
from utils.generador import Generador
class Ajuste_ambienteModel():

    @classmethod
    def update_ajustes_ambiente(self,ajuste_ambiente,configuracion,periodo):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM ajuste_ambiente WHERE cod_ambiente = %s',(ajuste_ambiente.cod_ambiente,))
                affected_deleted = cursor.rowcount
                dias = tuple(Generador.generar_dias(configuracion))
                dia_bloques = Generador.generar_dia_bloques(dias,configuracion)
                ajustes = Generador.generar_ajustes(periodo[0],periodo[1],dia_bloques)
                for ajuste in ajustes:
                    cursor.execute('''
                        INSERT INTO ajuste_ambiente (cod_ambiente, cod_dia, cod_bloque, fecha_aa)
                        VALUES (%s,%s,%s,%s);
                    ''',(ajuste_ambiente.cod_ambiente, ajuste[0], ajuste[1], ajuste[2]))
                affected_insert = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_deleted + affected_insert
        
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_ajuste_ambiente_all(self):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM ajuste_ambiente;')
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

