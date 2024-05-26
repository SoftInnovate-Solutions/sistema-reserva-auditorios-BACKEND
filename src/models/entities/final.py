from .usuario import Usuario

class Final(Usuario):
    def __init__(self, cod_usuario = None, nombre_usu = None, contrasenia_usu = None,codigo_sis_fin = None,cod_tipo_final = None):
        super().__init__(cod_usuario, nombre_usu, contrasenia_usu)
        self.codigo_sis_fin = codigo_sis_fin
        self.cod_tipo_final = cod_tipo_final

    def to_JSON(self):
        return{
            "cod_usuario" : self.cod_usuario,
            "nombre_usu" : str(self.nombre_usu).strip(),
            "contrasenia_usu" : str(self.contrasenia_usu).strip(),
            "codigo_sis_fin" : str(self.codigo_sis_fin).strip(),
            "cod_tipo_final" : self.cod_tipo_final
        }

    def to_JSONVALIDO(self):
        return{
            "cod_usuario" : self.cod_usuario,
            "nombre_usu" : str(self.cod_usuario).split(),
            "codigo_sis_fin" : str(self.codigo_sis_fin).strip()
        }
