class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo_inicial
        self.movimientos = []
    
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            self.movimientos.append(f"Depósito: +${monto:.2f}")
            return True
        return False
    
    def retirar(self, monto):
        if monto > 0 and self.validar_retiro(monto):
            self.saldo -= monto
            self.movimientos.append(f"Retiro: -${monto:.2f}")
            return True
        return False
    
    def validar_retiro(self, monto):
        return monto <= self.saldo
    
    def consultar_saldo(self):
        return self.saldo
    
    def ver_movimientos(self):
        return self.movimientos
    
    def __str__(self):
        return f"{self.__class__.__name__} - Titular: {self.titular}, Saldo: ${self.saldo:.2f}"

class CuentaAhorro(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo_inicial=0, saldo_minimo=100):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        self.saldo_minimo = saldo_minimo
    
    def validar_retiro(self, monto):
        return super().validar_retiro(monto) and (self.saldo - monto) >= self.saldo_minimo

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo_inicial=0, sobregiro_max=1000):
        super().__init__(numero_cuenta, titular, saldo_inicial)
        self.sobregiro_max = sobregiro_max
    
    def validar_retiro(self, monto):
        return (self.saldo - monto) >= -self.sobregiro_max

class CajeroAutomatico:
    def __init__(self):
        self.cuenta_actual = None
    
    def crear_cuenta(self):
        print("\n=== CREAR NUEVA CUENTA ===")
        tipo = input("Tipo de cuenta (1: Ahorro, 2: Corriente): ")
        numero = input("Número de cuenta: ")
        titular = input("Nombre del titular: ")
        try:
            saldo = float(input("Saldo inicial: "))
            if tipo == "1":
                self.cuenta_actual = CuentaAhorro(numero, titular, saldo)
            elif tipo == "2":
                self.cuenta_actual = CuentaCorriente(numero, titular, saldo)
            else:
                print("Tipo de cuenta no válido")
                return
            print("Cuenta creada exitosamente")
        except ValueError:
            print("Monto inválido")
    
    def menu(self):
        while True:
            print("\n=== CAJERO AUTOMÁTICO ===")
            print("1. Crear cuenta")
            print("2. Consultar saldo")
            print("3. Depositar")
            print("4. Retirar")
            print("5. Ver movimientos")
            print("6. Salir")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.crear_cuenta()
                
            elif opcion == "2" and self.cuenta_actual:
                print(f"\nSaldo actual: ${self.cuenta_actual.consultar_saldo():.2f}")
                
            elif opcion == "3" and self.cuenta_actual:
                try:
                    monto = float(input("Monto a depositar: "))
                    if self.cuenta_actual.depositar(monto):
                        print("Depósito realizado con éxito")
                    else:
                        print("Monto inválido")
                except ValueError:
                    print("Monto inválido")
                    
            elif opcion == "4" and self.cuenta_actual:
                try:
                    monto = float(input("Monto a retirar: "))
                    if self.cuenta_actual.retirar(monto):
                        print("Retiro realizado con éxito")
                    else:
                        print("Fondos insuficientes o monto inválido")
                except ValueError:
                    print("Monto inválido")
                    
            elif opcion == "5" and self.cuenta_actual:
                print("\n=== MOVIMIENTOS ===")
                for mov in self.cuenta_actual.ver_movimientos():
                    print(mov)
                print(f"\nSaldo actual: ${self.cuenta_actual.consultar_saldo():.2f}")
                
            elif opcion == "6":
                print("\n¡Gracias por usar nuestro cajero!")
                break
                
            else:
                if not self.cuenta_actual:
                    print("Debe crear una cuenta primero")
                else:
                    print("Opción inválida")

if __name__ == "__main__":
    cajero = CajeroAutomatico()
    cajero.menu()
