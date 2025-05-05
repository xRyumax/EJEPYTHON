class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.alimentado = False
    
    def emitir_sonido(self):
        return "..."
    
    def alimentar(self):
        if not self.alimentado:
            self.alimentado = True
            return f"{self.nombre} ha sido alimentado"
        return f"{self.nombre} ya fue alimentado hoy"
    
    def __str__(self):
        estado = "Alimentado" if self.alimentado else "Hambriento"
        return f"{self.__class__.__name__} - {self.nombre} ({self.edad} años) - {estado}"

class Leon(Animal):
    def emitir_sonido(self):
        return "¡ROAR!"

class Tigre(Animal):
    def emitir_sonido(self):
        return "¡GRRR!"

class Elefante(Animal):
    def emitir_sonido(self):
        return "¡PAWOO!"

class Zoologico:
    def __init__(self):
        self.animales = [
            Leon("Simba", 5),
            Leon("Mufasa", 8),
            Tigre("Rajah", 4),
            Tigre("Shere Khan", 6),
            Elefante("Dumbo", 3),
            Elefante("Tantor", 7)
        ]
    
    def menu(self):
        while True:
            print("\n=== ZOOLÓGICO INTERACTIVO ===")
            print("1. Ver todos los animales")
            print("2. Escuchar sonidos")
            print("3. Alimentar animal")
            print("4. Ver animales por tipo")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print("\nAnimales en el zoológico:")
                for i, animal in enumerate(self.animales, 1):
                    print(f"{i}. {animal}")
                    
            elif opcion == "2":
                print("\nLos animales hacen sonidos:")
                for animal in self.animales:
                    print(f"{animal.nombre}: {animal.emitir_sonido()}")
                    
            elif opcion == "3":
                print("\nAnimales disponibles para alimentar:")
                for i, animal in enumerate(self.animales, 1):
                    print(f"{i}. {animal}")
                    
                try:
                    idx = int(input("Seleccione el número del animal: ")) - 1
                    if 0 <= idx < len(self.animales):
                        print(self.animales[idx].alimentar())
                    else:
                        print("Animal no válido")
                except ValueError:
                    print("Entrada inválida")
                    
            elif opcion == "4":
                tipos = {Leon: "Leones", Tigre: "Tigres", Elefante: "Elefantes"}
                for tipo, nombre in tipos.items():
                    animales_tipo = [a for a in self.animales if isinstance(a, tipo)]
                    print(f"\n{nombre}:")
                    for animal in animales_tipo:
                        print(f"- {animal}")
                        
            elif opcion == "5":
                print("¡Gracias por visitar el zoológico!")
                break
                
            else:
                print("Opción inválida")

if __name__ == "__main__":
    zoo = Zoologico()
    zoo.menu()
