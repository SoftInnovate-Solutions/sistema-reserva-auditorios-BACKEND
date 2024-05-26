from database.db import get_connection
from .entities.administrador import Administrador
from utils.transformacion import Transformacion

class AdministradorModel():

    @classmethod
    def iniciar_sesion(self, nombre, contrasenia):
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
                               FROM administrador
                               WHERE cod_usuario = %s;
                        ''',(result[0],))
                    result = cursor.fetchone()
                    if result is not None:
                        connection.close()
                        return Administrador(cod_tipo_final=result[0]).to_JSONVALIDO()
            connection.close()
            return {}
        except Exception as ex:
            raise Exception(ex)
