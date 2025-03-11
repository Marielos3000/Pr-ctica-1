
class Lugar:
    def __init__(self, nombre: str, direccion: str, telefono: str):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Lugar: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"
