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
            'ambiente' : self.cod_ambiente,
            'materia' : self.cod_materia,
            'grupo' : self.cod_grupo,
            'fecha_res' : self.fecha_res,
            'hora' : self.cod_bloque,
            'instructor' : self.cod_usuario,
            'numero_estudiantes' : numero_estudiantes
        }

