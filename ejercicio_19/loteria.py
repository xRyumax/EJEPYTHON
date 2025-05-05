import random

class Boleto:
    def __init__(self, numero):
        self.numero = numero
        self.premio = 0
    
    def verificar_premio(self, numero_ganador):
        return False
    
    def __str__(self):
        return f"Boleto {self.numero:04d}"

class BoletoNormal(Boleto):
    def verificar_premio(self, numero_ganador):
        if self.numero == numero_ganador:
            self.premio = 1000  # Premio mayor
            return True
        elif abs(self.numero - numero_ganador) <= 2:
            self.premio = 100  # Premio menor por aproximación
            return True
        return False

class BoletoDorado(Boleto):
    def verificar_premio(self, numero_ganador):
        if self.numero == numero_ganador:
            self.premio = 5000  # Premio mayor especial
            return True
        elif abs(self.numero - numero_ganador) <= 5:
            self.premio = 500  # Premio menor especial
            return True
        return False

class Loteria:
    def __init__(self):
        self.boletos = []
        self.numero_ganador = None
    
    def generar_boletos(self, cantidad):
        numeros_disponibles = list(range(1, 1001))  # Números del 1 al 1000
        random.shuffle(numeros_disponibles)
        
        for _ in range(cantidad):
            if not numeros_disponibles:
                break
            
            numero = numeros_disponibles.pop()
            # 10% de probabilidad de que sea un boleto dorado
            if random.random() < 0.1:
                self.boletos.append(BoletoDorado(numero))
            else:
                self.boletos.append(BoletoNormal(numero))
    
    def realizar_sorteo(self):
        if not self.boletos:
            print("No hay boletos para realizar el sorteo")
            return
        
        self.numero_ganador = random.randint(1, 1000)
        print(f"\n¡El número ganador es: {self.numero_ganador:04d}!")
        
        ganadores = []
        for boleto in self.boletos:
            if boleto.verificar_premio(self.numero_ganador):
                ganadores.append(boleto)
        
        if ganadores:
            print("\nBoletos ganadores:")
            total_premios = 0
            for boleto in ganadores:
                print(f"{boleto} - Premio: ${boleto.premio}")
                total_premios += boleto.premio
            print(f"\nTotal en premios: ${total_premios}")
        else:
            print("\nNo hubo ganadores en este sorteo")
    
    def mostrar_estadisticas(self):
        if not self.boletos:
            print("No hay boletos registrados")
            return
        
        total_boletos = len(self.boletos)
        boletos_dorados = sum(1 for b in self.boletos if isinstance(b, BoletoDorado))
        boletos_normales = total_boletos - boletos_dorados
        
        print("\n=== ESTADÍSTICAS DE LA LOTERÍA ===")
        print(f"Total de boletos: {total_boletos}")
        print(f"Boletos normales: {boletos_normales}")
        print(f"Boletos dorados: {boletos_dorados}")

def menu_loteria():
    loteria = Loteria()
    
    while True:
        print("\n=== LOTERÍA PYTHON ===")
        print("1. Generar boletos")
        print("2. Ver boletos")
        print("3. Realizar sorteo")
        print("4. Ver estadísticas")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            try:
                cantidad = int(input("Cantidad de boletos a generar: "))
                if cantidad > 0:
                    loteria.generar_boletos(cantidad)
                    print(f"Se generaron {cantidad} boletos")
                else:
                    print("La cantidad debe ser mayor a 0")
            except ValueError:
                print("Cantidad inválida")
                
        elif opcion == "2":
            if loteria.boletos:
                print("\nBoletos disponibles:")
                for boleto in loteria.boletos:
                    tipo = "Dorado" if isinstance(boleto, BoletoDorado) else "Normal"
                    print(f"{boleto} - Tipo: {tipo}")
            else:
                print("No hay boletos generados")
                
        elif opcion == "3":
            loteria.realizar_sorteo()
            
        elif opcion == "4":
            loteria.mostrar_estadisticas()
            
        elif opcion == "5":
            print("\n¡Gracias por participar!")
            break
            
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu_loteria()
