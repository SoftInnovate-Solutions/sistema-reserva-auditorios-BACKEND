class Periodo_Reserva():
    def __init__(self,cod_periodo_reserva = None, fecha_inicio_general_per = None, 
                 fecha_fin_docente_per = None, fecha_inicio_docente_per = None, 
                 fecha_fin_general_per = None, fecha_inicio_auxiliar_per = None, fecha_fin_auxiliar_per = None,
                 notificacion_per = None, estado_visualizacion_per = None):
        self.cod_periodo_reserva = cod_periodo_reserva
        self.fecha_inicio_general_per = fecha_inicio_general_per
        self.fecha_fin_general_per = fecha_fin_general_per
        self.fecha_inicio_docente_per = fecha_inicio_docente_per
        self.fecha_fin_docente_per = fecha_fin_docente_per
        self.fecha_inicio_auxiliar_per = fecha_inicio_auxiliar_per
        self.fecha_fin_auxiliar_per = fecha_fin_auxiliar_per
        self.notificacion_per = notificacion_per
        self.estado_visualizacion_per = estado_visualizacion_per
    
    def to_JSON(self):
        return{
            'cod_periodo_reserva' : self.cod_periodo_reserva,
            'fecha_inicio_general_per': str(self.fecha_inicio_general_per),
            'fecha_fin_general_per': str(self.fecha_fin_general_per),
            'fecha_inicio_docente_per': str(self.fecha_inicio_docente_per),
            'fecha_fin_docente_per': str(self.fecha_fin_docente_per),
            'fecha_inicio_auxiliar_per': str(self.fecha_inicio_auxiliar_per),
            'fecha_fin_auxiliar_per': str(self.fecha_fin_auxiliar_per),
            'notificacion_per' : str(self.notificacion_per),
            'estado_visualizacion_per' : str(self.estado_visualizacion_per)
        }
    
    def to_JSONGENERAL(self):
        return{
            'cod_periodo_reserva' : self.cod_periodo_reserva,
            'fecha_inicio_general_per': str(self.fecha_inicio_general_per),
            'fecha_fin_general_per': str(self.fecha_fin_general_per)
        }

    
