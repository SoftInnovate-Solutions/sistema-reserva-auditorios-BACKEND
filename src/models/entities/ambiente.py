class Ambiente():
    def __init__(self,cod_ambiente = None,nombre_amb = None,capacidad_amb = None,ubicacion_amb = None,descripcion_amb = None, albergacion_max_amb = None, albergacion_min_amb = None, cod_facultad = None,cod_estado_ambiente = None,cod_piso = None,cod_tipo_ambiente = None,cod_edificacion = None):
        self.cod_ambiente = cod_ambiente
        self.nombre_amb = nombre_amb
        self.capacidad_amb = capacidad_amb
        self.ubicacion_amb = ubicacion_amb
        self.descripcion_amb = descripcion_amb
        self.albergacion_max_amb = albergacion_max_amb
        self.albergacion_min_amb = albergacion_min_amb
        self.cod_facultad = cod_facultad
        self.cod_estado_ambiente = cod_estado_ambiente
        self.cod_piso = cod_piso
        self.cod_tipo_ambiente = cod_tipo_ambiente
        self.cod_edificacion = cod_edificacion
        
    def to_JSONONE(self):
        return{
            'cod_ambiente' : self.cod_ambiente,
            'nombre_amb' : str(self.nombre_amb).strip(),
            'capacidad_amb' : self.capacidad_amb,
            'ubicacion_amb' : str(self.ubicacion_amb).strip(),
            'descripcion_amb' : str(self.descripcion_amb).strip(),
            'cod_facultad' : self.cod_facultad,
            'cod_estado_ambiente' : self.cod_estado_ambiente,
            'cod_piso' : self.cod_piso,
            'cod_tipo_ambiente' : self.cod_tipo_ambiente,
            'cod_edificacion' : self.cod_edificacion
        }

    def to_JSONALL(self):
        return{
            'cod_ambiente' : self.cod_ambiente,
            'nombre_amb' : str(self.nombre_amb).strip(),
            'estado_ambiente' : str(self.cod_estado_ambiente).strip(),
            'capacidad_amb' : self.capacidad_amb
        }
    
    def to_JSONSETTING(self):
        return{
            'cod_ambiente' : self.cod_ambiente,
            'albergacion_max_amb' : self.albergacion_max_amb,
            'albergacion_min_amb' : self.albergacion_min_amb,
            'capacidad_amb' : self.capacidad_amb
        }
    