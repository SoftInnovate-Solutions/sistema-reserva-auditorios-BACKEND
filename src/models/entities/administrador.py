from .usuario import Usuario
class Administrador(Usuario):
    def __init__(self, cod_usuario=None, nombre_usu=None, contrasenia_usu=None,alias_adm=None):
        super().__init__(cod_usuario, nombre_usu, contrasenia_usu)
        self.alias_adm = alias_adm

    def to_JSON(self):
        return{
            "cod_usuario" : self.cod_usuario,
            "nombre_usu" : str(self.nombre_usu).strip(),
            "contrasenia_usu" : str(self.contrasenia_usu).strip(),
            "alias_adm" : str(self.alias_adm).strip()
        }

    def to_JSONVALIDO(self):
        return{
            "cod_usuario" : self.cod_usuario,
            "nombre_usu" : str(self.nombre_usu).strip()
        }
