class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "..."
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre}"

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

class Pato(Animal):
    def hacer_sonido(self):
        return "¡Cuac cuac!"

def simular_granja():
    animales = [
        Perro("Firulais"),
        Gato("Garfield"),
        Pato("Donald"),
        Perro("Rex"),
        Gato("Tom"),
        Pato("Lucas")
    ]
    
    print("=== SIMULADOR DE ANIMALES ===")
    
    # Mostrar todos los animales y sus sonidos
    print("\nAnimales en la granja:")
    for animal in animales:
        print(f"{animal} dice: {animal.hacer_sonido()}")
    
    # Estadísticas por tipo
    tipos = {Perro: "Perros", Gato: "Gatos", Pato: "Patos"}
    print("\nEstadísticas:")
    for tipo, nombre in tipos.items():
        cantidad = sum(1 for a in animales if isinstance(a, tipo))
        print(f"Total de {nombre}: {cantidad}")
    
    # Coro de animales
    print("\n¡Coro de animales!")
    for tipo, nombre in tipos.items():
        print(f"\n{nombre}:")
        animales_tipo = [a for a in animales if isinstance(a, tipo)]
        for animal in animales_tipo:
            print(f"{animal.nombre}: {animal.hacer_sonido()}")

if __name__ == "__main__":
    simular_granja()
