class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    
    def calcular_bono(self):
        return 0
    
    def salario_total(self):
        return self.salario_base + self.calcular_bono()
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre}"

class Gerente(Empleado):
    def __init__(self, nombre, salario_base, departamento):
        super().__init__(nombre, salario_base)
        self.departamento = departamento
    
    def calcular_bono(self):
        # Bono del 30% del salario base
        return self.salario_base * 0.30

class Asistente(Empleado):
    def __init__(self, nombre, salario_base, horas_extra=0):
        super().__init__(nombre, salario_base)
        self.horas_extra = horas_extra
    
    def calcular_bono(self):
        # Bono por horas extra ($10 por hora)
        return self.horas_extra * 10

class ControlEmpleados:
    def __init__(self):
        self.empleados = []
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def mostrar_nomina(self):
        print("\n=== NÓMINA DE EMPLEADOS ===")
        total_nomina = 0
        
        # Mostrar por tipo de empleado
        for tipo in [Gerente, Asistente]:
            empleados_tipo = [e for e in self.empleados if isinstance(e, tipo)]
            if empleados_tipo:
                print(f"\n{tipo.__name__}s:")
                for emp in empleados_tipo:
                    bono = emp.calcular_bono()
                    total = emp.salario_total()
                    print(f"{emp.nombre}:")
                    print(f"  Salario base: ${emp.salario_base:.2f}")
                    print(f"  Bono: ${bono:.2f}")
                    print(f"  Total: ${total:.2f}")
                    total_nomina += total
        
        print(f"\nTotal nómina: ${total_nomina:.2f}")
    
    def aplicar_aumento(self, porcentaje):
        for empleado in self.empleados:
            empleado.salario_base *= (1 + porcentaje/100)
        print(f"\nAumento del {porcentaje}% aplicado a todos los empleados")

def demo_sistema():
    control = ControlEmpleados()
    
    # Agregar algunos empleados de ejemplo
    control.agregar_empleado(Gerente("Ana García", 5000, "Ventas"))
    control.agregar_empleado(Gerente("Juan Pérez", 5500, "IT"))
    control.agregar_empleado(Asistente("María López", 2000, 10))
    control.agregar_empleado(Asistente("Carlos Ruiz", 2200, 5))
    
    while True:
        print("\n=== CONTROL DE EMPLEADOS ===")
        print("1. Ver nómina")
        print("2. Aplicar aumento general")
        print("3. Agregar empleado")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            control.mostrar_nomina()
            
        elif opcion == "2":
            try:
                porcentaje = float(input("Porcentaje de aumento: "))
                control.aplicar_aumento(porcentaje)
            except ValueError:
                print("Porcentaje inválido")
                
        elif opcion == "3":
            tipo = input("Tipo (1: Gerente, 2: Asistente): ")
            nombre = input("Nombre: ")
            try:
                salario = float(input("Salario base: "))
                if tipo == "1":
                    depto = input("Departamento: ")
                    control.agregar_empleado(Gerente(nombre, salario, depto))
                elif tipo == "2":
                    horas = int(input("Horas extra: "))
                    control.agregar_empleado(Asistente(nombre, salario, horas))
                else:
                    print("Tipo no válido")
                    continue
                print("Empleado agregado exitosamente")
            except ValueError:
                print("Datos inválidos")
                
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
            
        else:
            print("Opción inválida")

if __name__ == "__main__":
    demo_sistema()
