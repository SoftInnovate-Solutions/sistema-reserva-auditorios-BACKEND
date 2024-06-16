# imparticion.py

class Imparticion:
    def __init__(self, nombre_usu, materia, grupo, cant_estudiantes):
        self.nombre_usu = nombre_usu
        self.materia = materia
        self.grupo = grupo
        self.cant_estudiantes = cant_estudiantes

    def to_JSONALL(self):
        return {
            'nombreUsuario': str(self.nombre_usu).strip(),
            'materia': str(self.materia).strip(),
            'grupo': str(self.grupo).strip(),
            'cantidad_estudiantes': self.cant_estudiantes
        }
