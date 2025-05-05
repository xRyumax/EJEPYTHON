class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_salario(self):
        return self.salario_base
    
    def __str__(self):
        return f"{self.nombre} - Salario: ${self.calcular_salario():.2f}"

class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(self):
        # Bonificación del 20% para empleados de tiempo completo
        return self.salario_base * 1.2

class EmpleadoMedioTiempo(Empleado):
    def calcular_salario(self):
        # Medio tiempo recibe la mitad del salario base
        return self.salario_base * 0.5

def gestionar_empleados():
    empleados = [
        EmpleadoTiempoCompleto("Juan Pérez", 3000),
        EmpleadoTiempoCompleto("María García", 3500),
        EmpleadoMedioTiempo("Carlos López", 3000),
        EmpleadoMedioTiempo("Ana Martínez", 3200)
    ]
    
    print("=== GESTIÓN DE EMPLEADOS ===")
    print("\nLista de empleados y sus salarios:")
    
    total_salarios = 0
    for empleado in empleados:
        print(empleado)
        total_salarios += empleado.calcular_salario()
    
    print(f"\nTotal nómina mensual: ${total_salarios:.2f}")
    
    # Calcular promedios por tipo
    tiempo_completo = [e for e in empleados if isinstance(e, EmpleadoTiempoCompleto)]
    medio_tiempo = [e for e in empleados if isinstance(e, EmpleadoMedioTiempo)]
    
    promedio_tc = sum(e.calcular_salario() for e in tiempo_completo) / len(tiempo_completo)
    promedio_mt = sum(e.calcular_salario() for e in medio_tiempo) / len(medio_tiempo)
    
    print(f"\nPromedio salario tiempo completo: ${promedio_tc:.2f}")
    print(f"Promedio salario medio tiempo: ${promedio_mt:.2f}")

if __name__ == "__main__":
    gestionar_empleados()
