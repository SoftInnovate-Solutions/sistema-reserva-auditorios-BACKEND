from database.db import get_connection
from .entities.final import Final
from utils.transformacion import Transformacion


class FinalModel():

    @classmethod
    def iniciar_sesion(self, contrasenia, codigo_sis):
        try:
            connection = get_connection()
            cifrado = Transformacion.transformarSHA512(contrasenia)
            with connection.cursor() as cursor:
                cursor.execute('''
                               SELECT cod_usuario, nombre_usu
                               FROM usuario
                               WHERE contrasenia_usu = %s;
                        ''',(cifrado,))
                result1 = cursor.fetchone()
                if result1 is not None:
                    cursor.execute('''
                            SELECT f.cod_usuario, tf.nombre_tf
                            FROM final AS f
                            JOIN tipo_final AS tf ON tf.cod_tipo_final = f.cod_tipo_final
                            WHERE f.cod_usuario = %s AND f.codigo_sis_fin = %s;
                        ''',(result1[0],codigo_sis))
                    result2 = cursor.fetchone()
                    if result2 is not None:
                        connection.close()
                        return Final(cod_usuario = result2[0],cod_tipo_final = str(result2[1]).strip(), nombre_usu = result1[1], codigo_sis_fin = codigo_sis).to_JSONVALIDO()
            connection.close()
            return {}
        except Exception as ex:
            raise Exception(ex)



