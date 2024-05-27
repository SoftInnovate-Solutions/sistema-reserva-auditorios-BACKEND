class Reserva():
    def __init__(self,cod_reserva = None, cod_dia = None, cod_bloque = None, cod_ambiente = None, cod_materia = None
                ,cod_grupo = None, cod_usuario = None, fecha_res = None):
        self.cod_reserva = cod_reserva
        self.cod_dia = cod_dia
        self.cod_bloque = cod_bloque
        self.cod_ambiente = cod_ambiente
        self.cod_materia = cod_materia
        self.cod_grupo = cod_grupo
        self.cod_usuario = cod_usuario
        self.fecha_res = fecha_res

    def to_JSONALL(self):
        return {
            'cod_reserva' : self.cod_reserva,
            'ambiente' : self.cod_ambiente,
            'materia' : self.cod_materia,
            'grupo' : self.cod_grupo,
            'fecha_res' : self.fecha_res,
            'hora' : self.cod_bloque
        }
    
    def to_JSONONE(self, numero_estudiantes):
        return {
            'cod_reserva' : self.cod_reserva,
            'ambiente' : str(self.cod_ambiente).split(),
            'materia' : str(self.cod_materia).split(),
            'grupo' : str(self.cod_grupo).split(),
            'fecha_res' : self.fecha_res,
            'hora' : str(self.cod_bloque).split(),
            'instructor' : str(self.cod_usuario).split(),
            'numero_estudiantes' : numero_estudiantes
        }
    
    def to_JSONIMPARTICION(self, imparticion,cantidad_estudiantes_imp):
        return{
            'imparticion' : str(imparticion).strip(),
            'cantidad_estudiantes_imp': cantidad_estudiantes_imp,
            'cod_grupo': self.cod_grupo,
            'cod_materia': self.cod_materia
        }
    
    def to_JSONAMBIENTESDISPONIBLES(self,nombre_ambiente):
        return{
            'cod_ambiente' : self.cod_ambiente,
            'nombre_amb' : str(nombre_ambiente).strip()
        }
    
    def to_JSONCALENDARIO(self):
        fecha_formateada = self.fecha_res.strftime("%Y-%m-%d")
        return {
            'fecha': fecha_formateada
        }
    
    def to_JSONDIABLOQUE(self,nombre_blo):
        return {
            'cod_bloque': self.cod_bloque,
            'nombre_blo': nombre_blo,
            'cod_dia': self.cod_dia
        }



