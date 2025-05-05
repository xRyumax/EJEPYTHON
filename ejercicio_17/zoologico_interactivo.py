class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.energia = 100
        self.hambre = 50
    
    def alimentar(self):
        self.hambre = max(0, self.hambre - 30)
        self.energia = min(100, self.energia + 20)
        return f"{self.nombre} ha sido alimentado"
    
    def estado(self):
        return f"Energía: {self.energia}%, Hambre: {self.hambre}%"
    
    def __str__(self):
        return f"{self.__class__.__name__} - {self.nombre} ({self.edad} años)"

class Felino(Animal):
    def __init__(self, nombre, edad, especie):
        super().__init__(nombre, edad)
        self.especie = especie
    
    def alimentar(self):
        mensaje = super().alimentar()
        return f"{mensaje} con carne fresca"

class Ave(Animal):
    def __init__(self, nombre, edad, puede_volar):
        super().__init__(nombre, edad)
        self.puede_volar = puede_volar
    
    def alimentar(self):
        mensaje = super().alimentar()
        return f"{mensaje} con semillas y frutas"

class ZoologicoInteractivo:
    def __init__(self):
        self.animales = [
            Felino("Leo", 5, "León"),
            Felino("Tigger", 3, "Tigre"),
            Ave("Rio", 2, True),
            Ave("Penny", 1, False),
            Felino("Jaguar", 4, "Jaguar"),
            Ave("Blu", 2, True)
        ]
    
    def mostrar_animal(self, animal):
        print(f"\n{animal}")
        print(f"Especie: {animal.especie if isinstance(animal, Felino) else 'Ave'}")
        if isinstance(animal, Ave):
            print(f"Puede volar: {'Sí' if animal.puede_volar else 'No'}")
        print(animal.estado())
    
    def menu(self):
        while True:
            print("\n=== ZOOLÓGICO INTERACTIVO ===")
            print("1. Ver todos los animales")
            print("2. Alimentar animal")
            print("3. Ver felinos")
            print("4. Ver aves")
            print("5. Ver estados")
            print("6. Salir")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                print("\nAnimales en el zoológico:")
                for i, animal in enumerate(self.animales, 1):
                    print(f"{i}. {animal}")
                    
            elif opcion == "2":
                print("\nAnimales disponibles para alimentar:")
                for i, animal in enumerate(self.animales, 1):
                    print(f"{i}. {animal} - Hambre: {animal.hambre}%")
                
                try:
                    idx = int(input("\nSeleccione el número del animal: ")) - 1
                    if 0 <= idx < len(self.animales):
                        print(self.animales[idx].alimentar())
                    else:
                        print("Número de animal no válido")
                except ValueError:
                    print("Entrada inválida")
                    
            elif opcion == "3":
                felinos = [a for a in self.animales if isinstance(a, Felino)]
                print("\nFelinos en el zoológico:")
                for felino in felinos:
                    self.mostrar_animal(felino)
                    
            elif opcion == "4":
                aves = [a for a in self.animales if isinstance(a, Ave)]
                print("\nAves en el zoológico:")
                for ave in aves:
                    self.mostrar_animal(ave)
                    
            elif opcion == "5":
                print("\nEstado de todos los animales:")
                for animal in self.animales:
                    print(f"\n{animal}")
                    print(animal.estado())
                    
            elif opcion == "6":
                print("\n¡Gracias por visitar el zoológico!")
                break
                
            else:
                print("Opción inválida")

if __name__ == "__main__":
    zoo = ZoologicoInteractivo()
    zoo.menu()
