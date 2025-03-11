
class Foto:
    def __init__(self, ubicacion_archivo: str, tipo_archivo: str, tamano: float):
        self.ubicacion_archivo = ubicacion_archivo
        self.tipo_archivo = tipo_archivo
        self.tamano = tamano

    def __str__(self):
        return f"Foto - Ubicación: {self.ubicacion_archivo}, Tipo: {self.tipo_archivo}, Tamaño: {self.tamano}MB"