class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        return "..."
    
    def __str__(self):
        return f"{self.__class__.__name__} - {self.nombre} ({self.edad} años)"

class Perro(Mascota):
    def hacer_sonido(self):
        return "¡Guau guau!"

class Gato(Mascota):
    def hacer_sonido(self):
        return "¡Miau!"

class Pez(Mascota):
    def hacer_sonido(self):
        return "Glup glup..."

class SistemaMascotas:
    def __init__(self):
        self.mascotas = []
    
    def agregar_mascota(self, tipo, nombre, edad):
        if tipo.lower() == "perro":
            mascota = Perro(nombre, edad)
        elif tipo.lower() == "gato":
            mascota = Gato(nombre, edad)
        elif tipo.lower() == "pez":
            mascota = Pez(nombre, edad)
        else:
            return False
        
        self.mascotas.append(mascota)
        return True
    
    def listar_mascotas(self):
        if not self.mascotas:
            print("No hay mascotas registradas")
            return
        
        for mascota in self.mascotas:
            print(f"{mascota} - Sonido: {mascota.hacer_sonido()}")
    
    def menu(self):
        while True:
            print("\n=== SISTEMA DE MASCOTAS ===")
            print("1. Agregar mascota")
            print("2. Listar mascotas")
            print("3. Hacer que todas hagan sonido")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                tipo = input("Tipo de mascota (perro/gato/pez): ")
                nombre = input("Nombre de la mascota: ")
                try:
                    edad = int(input("Edad de la mascota: "))
                    if self.agregar_mascota(tipo, nombre, edad):
                        print("Mascota agregada exitosamente")
                    else:
                        print("Tipo de mascota no válido")
                except ValueError:
                    print("Edad inválida")
            
            elif opcion == "2":
                self.listar_mascotas()
            
            elif opcion == "3":
                print("\n¡Las mascotas hacen sonidos!")
                for mascota in self.mascotas:
                    print(f"{mascota.nombre}: {mascota.hacer_sonido()}")
            
            elif opcion == "4":
                print("¡Gracias por usar el sistema!")
                break
            
            else:
                print("Opción inválida")

if __name__ == "__main__":
    sistema = SistemaMascotas()
    sistema.menu()
