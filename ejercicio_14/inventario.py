class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def aplicar_descuento(self):
        return self.precio
    
    def verificar_stock(self):
        return self.stock > 5
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"

class Ropa(Producto):
    def __init__(self, nombre, precio, stock, talla):
        super().__init__(nombre, precio, stock)
        self.talla = talla
    
    def aplicar_descuento(self):
        # 20% de descuento si hay más de 10 unidades
        if self.stock > 10:
            return self.precio * 0.8
        return self.precio

class Alimento(Producto):
    def __init__(self, nombre, precio, stock, fecha_vencimiento):
        super().__init__(nombre, precio, stock)
        self.fecha_vencimiento = fecha_vencimiento
    
    def aplicar_descuento(self):
        # 15% de descuento si hay más de 15 unidades
        if self.stock > 15:
            return self.precio * 0.85
        return self.precio

class Tecnologia(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre, precio, stock)
        self.garantia = garantia
    
    def aplicar_descuento(self):
        # 10% de descuento si hay más de 5 unidades
        if self.stock > 5:
            return self.precio * 0.9
        return self.precio

class Tienda:
    def __init__(self):
        self.productos = [
            Ropa("Camiseta", 25.99, 12, "M"),
            Ropa("Pantalón", 45.99, 8, "L"),
            Alimento("Arroz", 5.99, 20, "2024-12-31"),
            Alimento("Leche", 2.99, 15, "2023-06-01"),
            Tecnologia("Auriculares", 99.99, 6, "1 año"),
            Tecnologia("Mouse", 29.99, 4, "6 meses")
        ]
    
    def verificar_inventario(self):
        print("=== INVENTARIO DE LA TIENDA ===")
        
        productos_bajos = []
        while True:
            productos_bajos = [p for p in self.productos if not p.verificar_stock()]
            if not productos_bajos:
                break
            
            print("\nProductos con stock bajo:")
            for producto in productos_bajos:
                print(f"¡Alerta! {producto}")
            
            respuesta = input("\n¿Desea reabastecer todos los productos bajos? (s/n): ")
            if respuesta.lower() == 's':
                for producto in productos_bajos:
                    producto.stock += 10
                print("Productos reabastecidos")
            else:
                break
        
        # Mostrar inventario completo
        print("\nInventario completo:")
        for producto in self.productos:
            precio_con_descuento = producto.aplicar_descuento()
            if precio_con_descuento < producto.precio:
                print(f"{producto} - ¡Descuento! Precio final: ${precio_con_descuento:.2f}")
            else:
                print(producto)
        
        # Estadísticas
        total_productos = sum(p.stock for p in self.productos)
        valor_total = sum(p.precio * p.stock for p in self.productos)
        
        print(f"\nTotal de productos: {total_productos}")
        print(f"Valor total del inventario: ${valor_total:.2f}")

if __name__ == "__main__":
    tienda = Tienda()
    tienda.verificar_inventario()
