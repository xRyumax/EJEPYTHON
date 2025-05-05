import math

class Figura:
    def area(self):
        pass
    
    def perimetro(self):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} - Área: {self.area():.2f}, Perímetro: {self.perimetro():.2f}"

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio

def mostrar_figuras():
    figuras = [
        Rectangulo(5, 3),
        Rectangulo(4, 4),
        Circulo(2),
        Circulo(3)
    ]
    
    print("=== FIGURAS GEOMÉTRICAS ===")
    for figura in figuras:
        print(figura)
    
    # Calcular totales por tipo
    rectangulos = [f for f in figuras if isinstance(f, Rectangulo)]
    circulos = [f for f in figuras if isinstance(f, Circulo)]
    
    print("\nEstadísticas:")
    print(f"Total área rectángulos: {sum(r.area() for r in rectangulos):.2f}")
    print(f"Total área círculos: {sum(c.area() for c in circulos):.2f}")
    print(f"Total perímetro rectángulos: {sum(r.perimetro() for r in rectangulos):.2f}")
    print(f"Total perímetro círculos: {sum(c.perimetro() for c in circulos):.2f}")

if __name__ == "__main__":
    mostrar_figuras()
