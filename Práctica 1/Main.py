
    # Crear lugares

from claseLugar import Lugar
from claseFoto import Foto
from clasePersona import Persona
from claseRol import Rol 

def main():
    lugar1 = Lugar("Universidad", "Zona 12", "5717-4298")
    lugar2 = Lugar("Biblioteca", "Zona 12", "3333-4444")
    lugar3 = Lugar("Jardín", "Zona 4", "8888-5555")
    lugar4 = Lugar("Cafetería", "Zona 10", "1111-7777")
    
    # Crear fotos
    foto1 = Foto("/imagenes/jose.jpg", "jpg", 1.5)
    foto2 = Foto("/imagenes/marielos.png", "jpg", 6.9)
    
    # Crear personas con roles diferentes
    persona1 = Persona("Daniel", "López", Rol.ADMIN, foto1)
    persona2 = Persona("Marielos", "Alegria", Rol.USUARIO, foto2)
    
    # Agregar lugares a las personas
    persona1.agregar_lugar_frecuente(lugar1)
    persona1.agregar_lugar_frecuente(lugar2)
    
    persona2.agregar_lugar_frecuente(lugar3)
    persona2.agregar_lugar_frecuente(lugar4)
    
    # Mostrar información
    print(persona1)
    print("""
         ✦———————✿———————✦—✿—✦———————✿———————✦
    """)
    print(persona2)

if __name__ == "__main__":
    main()
