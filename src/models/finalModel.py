from database.db import get_connection
from .entities.final import Final
from utils.transformacion import Transformacion


class FinalModel():

    @classmethod
    def iniciar_sesion(self, nombre, contrasenia, codigo_sis):
        try:
            connection = get_connection()
            cifrado = Transformacion.transformarSHA512(contrasenia)
            with connection.cursor() as cursor:
                cursor.execute('''
                               SELECT cod_usuario
                               FROM usuario
                               WHERE nombre_usu = %s AND contrasenia_usu = %s;
                        ''',(nombre,cifrado))
                result = cursor.fetchone()
                if result is not None:
                    cursor.execute('''
                               SELECT cod_usuario
                               FROM final
                               WHERE cod_usuario = %s AND codigo_sis_fin = %s;
                        ''',(result[0],codigo_sis))
                    result = cursor.fetchone()
                    if result is not None:
                        connection.close()
                        return Final(cod_tipo_final=result[0], nombre_usu= nombre, codigo_sis_fin= codigo_sis).to_JSONVALIDO()
            connection.close()
            return {}
        except Exception as ex:
            raise Exception(ex)



