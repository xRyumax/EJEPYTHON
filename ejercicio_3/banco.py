class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial
    
    def consultar_saldo(self):
        return self.saldo
    
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return True
        return False
    
    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            return True
        return False
    
    def tipo_cuenta(self):
        return "Cuenta Bancaria Genérica"

class CuentaAhorro(CuentaBancaria):
    def tipo_cuenta(self):
        return "Cuenta de Ahorro"
    
    def retirar(self, monto):
        if self.saldo - monto >= 100:  # Mantener saldo mínimo
            return super().retirar(monto)
        return False

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, saldo_inicial=0, sobregiro_max=500):
        super().__init__(numero_cuenta, saldo_inicial)
        self.sobregiro_max = sobregiro_max
    
    def tipo_cuenta(self):
        return "Cuenta Corriente"
    
    def retirar(self, monto):
        if monto > 0 and (self.saldo - monto) >= -self.sobregiro_max:
            self.saldo -= monto
            return True
        return False

def menu_principal():
    cuenta = None
    while True:
        print("\n=== SISTEMA BANCARIO ===")
        print("1. Crear cuenta")
        print("2. Consultar saldo")
        print("3. Depositar")
        print("4. Retirar")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1" and cuenta is None:
            tipo = input("Tipo de cuenta (1: Ahorro, 2: Corriente): ")
            num_cuenta = input("Número de cuenta: ")
            saldo_inicial = float(input("Saldo inicial: "))
            
            if tipo == "1":
                cuenta = CuentaAhorro(num_cuenta, saldo_inicial)
            else:
                cuenta = CuentaCorriente(num_cuenta, saldo_inicial)
            print(f"Cuenta creada: {cuenta.tipo_cuenta()}")
            
        elif opcion == "2" and cuenta:
            print(f"Saldo actual: ${cuenta.consultar_saldo():.2f}")
            
        elif opcion == "3" and cuenta:
            monto = float(input("Monto a depositar: "))
            if cuenta.depositar(monto):
                print("Depósito exitoso")
            else:
                print("Error en el depósito")
                
        elif opcion == "4" and cuenta:
            monto = float(input("Monto a retirar: "))
            if cuenta.retirar(monto):
                print("Retiro exitoso")
            else:
                print("Fondos insuficientes o monto inválido")
                
        elif opcion == "5":
            print("¡Gracias por usar nuestro sistema!")
            break
            
        else:
            print("Opción inválida o debe crear una cuenta primero")

if __name__ == "__main__":
    menu_principal()
