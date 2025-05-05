class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def valor_total(self):
        if self.cantidad > 10:
            # Aplicar 10% de descuento si hay más de 10 unidades
            return self.precio * self.cantidad * 0.9
        return self.precio * self.cantidad

class ProductoPerecedero(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento):
        super().__init__(nombre, precio, cantidad)
        self.fecha_vencimiento = fecha_vencimiento

class ProductoNoPerecedero(Producto):
    def __init__(self, nombre, precio, cantidad, tipo):
        super().__init__(nombre, precio, cantidad)
        self.tipo = tipo

# Ejemplo de uso
if __name__ == "__main__":
    # Crear lista de productos
    inventario = [
        ProductoPerecedero("Leche", 2.5, 15, "2025-06-01"),
        ProductoPerecedero("Yogurt", 1.0, 20, "2025-05-15"),
        ProductoNoPerecedero("Arroz", 3.0, 50, "Granos"),
        ProductoNoPerecedero("Sal", 1.0, 8, "Condimentos")
    ]
    
    # Calcular valor total del inventario
    total = sum(producto.valor_total() for producto in inventario)
    
    print("=== Inventario de Productos ===")
    for producto in inventario:
        print(f"{producto.nombre}: {producto.cantidad} unidades - Valor: ${producto.valor_total():.2f}")
    print(f"\nValor total del inventario: ${total:.2f}")
