import math

class Figura:
    def area(self):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} - Área: {self.area():.2f}"

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * (self.radio ** 2)

def calcular_areas():
    figuras = [
        Rectangulo(5, 3),
        Triangulo(4, 6),
        Circulo(2),
        Rectangulo(2, 2),
        Triangulo(3, 3),
        Circulo(3)
    ]
    
    print("=== CÁLCULO DE ÁREAS ===")
    
    total_area = 0
    for figura in figuras:
        print(figura)
        total_area += figura.area()
    
    print(f"\nÁrea total de todas las figuras: {total_area:.2f}")
    
    # Estadísticas por tipo
    print("\nEstadísticas por tipo:")
    for tipo in [Rectangulo, Triangulo, Circulo]:
        figuras_tipo = [f for f in figuras if isinstance(f, tipo)]
        if figuras_tipo:
            area_promedio = sum(f.area() for f in figuras_tipo) / len(figuras_tipo)
            print(f"{tipo.__name__}: {len(figuras_tipo)} figuras, área promedio: {area_promedio:.2f}")

if __name__ == "__main__":
    calcular_areas()
