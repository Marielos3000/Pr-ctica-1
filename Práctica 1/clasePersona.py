
class Persona:
    def __init__(self, nombre: str, apellido: str, rol: "Rol", foto: str):
        self.nombre = nombre
        self.apellido = apellido
        self.roles = [rol]  # Lista de roles, inicializada con el primer rol
        self.lugares_frecuentes = []  # Lista de lugares frecuentes
        self.foto = foto  # Se asume que es un string con la ruta o nombre de la imagen

    def agregar_lugar_frecuente(self, lugar: "Lugar"):
        self.lugares_frecuentes.append(lugar)

    def set_rol(self, rol: "Rol"):
        if rol not in self.roles:
            self.roles.append(rol)
    
    def __str__(self):
        lugares_str = "\n".join(str(lugar) for lugar in self.lugares_frecuentes)
        roles_str = ", ".join([rol.name for rol in self.roles])  # Se asume que `Rol` tiene un atributo `name`
        return (f"Persona: {self.nombre} {self.apellido}, Roles: {roles_str}\n"
                f"Foto: {self.foto}\n"
                f"Lugares Frecuentes:\n{lugares_str}")
