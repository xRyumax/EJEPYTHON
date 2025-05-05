class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def describir(self):
        return f"Soy un vehículo genérico marca {self.marca} modelo {self.modelo}"

class Auto(Vehiculo):
    def describir(self):
        return f"Soy un auto marca {self.marca} modelo {self.modelo}"

class Moto(Vehiculo):
    def describir(self):
        return f"Soy una moto marca {self.marca} modelo {self.modelo}"

class Camion(Vehiculo):
    def describir(self):
        return f"Soy un camión marca {self.marca} modelo {self.modelo}"

# Ejemplo de uso
if __name__ == "__main__":
    vehiculos = [
        Auto("Toyota", "Corolla"),
        Moto("Honda", "CBR"),
        Camion("Volvo", "FH16")
    ]
    
    print("=== Descripción de vehículos ===")
    for vehiculo in vehiculos:
        print(vehiculo.describir())
