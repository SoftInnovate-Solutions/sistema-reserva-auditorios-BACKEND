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
                               SELECT cod_usuario, nombre_usu
                               FROM usuario
                               WHERE nombre_usu = %s AND contrasenia_usu = %s;
                        ''',(nombre,cifrado))
                result1 = cursor.fetchone()
                if result1 is not None:
                    cursor.execute('''
                               SELECT cod_usuario
                               FROM administrador
                               WHERE cod_usuario = %s;
                        ''',(result1[0],))
                    result2 = cursor.fetchone()
                    if result2 is not None:
                        connection.close()
                        return Administrador(cod_usuario=result2[0], nombre_usu=result1[1]).to_JSONVALIDO()
            connection.close()
            return {}
        except Exception as ex:
            raise Exception(ex)
