class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []
    
    def agregar_producto(self, producto):
        self.carrito.append(producto)
    
    def calcular_total(self):
        total = sum(p.precio for p in self.carrito)
        # Aplicar descuento si hay más de 3 productos
        if len(self.carrito) > 3:
            total *= 0.9  # 10% de descuento
        return total
    
    def vaciar_carrito(self):
        self.carrito.clear()

class TiendaOnline:
    def __init__(self):
        # Catálogo predefinido de productos
        self.productos = [
            Producto("Laptop", 999.99),
            Producto("Mouse", 29.99),
            Producto("Teclado", 49.99),
            Producto("Monitor", 299.99),
            Producto("Auriculares", 79.99)
        ]
        self.cliente = None
    
    def mostrar_productos(self):
        print("\nProductos disponibles:")
        for i, producto in enumerate(self.productos, 1):
            print(f"{i}. {producto}")
    
    def menu(self):
        while True:
            if not self.cliente:
                nombre = input("\nBienvenido! Por favor, ingrese su nombre: ")
                self.cliente = Cliente(nombre)
            
            print(f"\n=== TIENDA ONLINE - Cliente: {self.cliente.nombre} ===")
            print("1. Ver productos")
            print("2. Agregar producto al carrito")
            print("3. Ver carrito")
            print("4. Finalizar compra")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.mostrar_productos()
                
            elif opcion == "2":
                self.mostrar_productos()
                try:
                    idx = int(input("Seleccione el número del producto: ")) - 1
                    if 0 <= idx < len(self.productos):
                        self.cliente.agregar_producto(self.productos[idx])
                        print("Producto agregado al carrito")
                    else:
                        print("Producto no válido")
                except ValueError:
                    print("Entrada inválida")
                    
            elif opcion == "3":
                if not self.cliente.carrito:
                    print("El carrito está vacío")
                else:
                    print("\nProductos en el carrito:")
                    for producto in self.cliente.carrito:
                        print(producto)
                    total = self.cliente.calcular_total()
                    if len(self.cliente.carrito) > 3:
                        print("\n¡Descuento del 10% aplicado!")
                    print(f"Total a pagar: ${total:.2f}")
                    
            elif opcion == "4":
                if not self.cliente.carrito:
                    print("El carrito está vacío")
                else:
                    total = self.cliente.calcular_total()
                    print(f"\nTotal a pagar: ${total:.2f}")
                    confirmar = input("¿Desea confirmar la compra? (s/n): ")
                    if confirmar.lower() == 's':
                        print("¡Compra realizada con éxito!")
                        self.cliente.vaciar_carrito()
                    else:
                        print("Compra cancelada")
                        
            elif opcion == "5":
                print("¡Gracias por su visita!")
                break
                
            else:
                print("Opción inválida")

if __name__ == "__main__":
    tienda = TiendaOnline()
    tienda.menu()
