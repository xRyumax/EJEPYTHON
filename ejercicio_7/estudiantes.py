class Estudiante:
    def __init__(self, nombre, notas=None):
        self.nombre = nombre
        self.notas = notas if notas is not None else []
    
    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            return True
        return False
    
    def calcular_promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def esta_aprobado(self):
        return self.calcular_promedio() >= 6.0
    
    def __str__(self):
        estado = "APROBADO" if self.esta_aprobado() else "REPROBADO"
        return f"{self.nombre} - Promedio: {self.calcular_promedio():.2f} - {estado}"

class EstudianteBecado(Estudiante):
    def esta_aprobado(self):
        # Los estudiantes becados necesitan un promedio más alto para aprobar
        return self.calcular_promedio() >= 8.0

def gestionar_estudiantes():
    estudiantes = []
    
    while True:
        print("\n=== SISTEMA DE ESTUDIANTES ===")
        print("1. Agregar estudiante regular")
        print("2. Agregar estudiante becado")
        print("3. Agregar nota a estudiante")
        print("4. Ver estudiantes y promedios")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            estudiantes.append(Estudiante(nombre))
            print("Estudiante agregado")
            
        elif opcion == "2":
            nombre = input("Nombre del estudiante becado: ")
            estudiantes.append(EstudianteBecado(nombre))
            print("Estudiante becado agregado")
            
        elif opcion == "3":
            if not estudiantes:
                print("No hay estudiantes registrados")
                continue
                
            print("\nEstudiantes disponibles:")
            for i, est in enumerate(estudiantes):
                print(f"{i+1}. {est.nombre}")
            
            try:
                idx = int(input("Seleccione el número de estudiante: ")) - 1
                nota = float(input("Ingrese la nota (0-10): "))
                
                if 0 <= idx < len(estudiantes):
                    if estudiantes[idx].agregar_nota(nota):
                        print("Nota agregada exitosamente")
                    else:
                        print("Nota inválida")
                else:
                    print("Estudiante no válido")
            except ValueError:
                print("Entrada inválida")
                
        elif opcion == "4":
            if not estudiantes:
                print("No hay estudiantes registrados")
                continue
                
            print("\nLista de estudiantes:")
            for estudiante in estudiantes:
                print(estudiante)
                
            # Estadísticas
            total_estudiantes = len(estudiantes)
            aprobados = sum(1 for e in estudiantes if e.esta_aprobado())
            
            print(f"\nEstadísticas:")
            print(f"Total estudiantes: {total_estudiantes}")
            print(f"Aprobados: {aprobados}")
            print(f"Reprobados: {total_estudiantes - aprobados}")
            
        elif opcion == "5":
            print("¡Gracias por usar el sistema!")
            break
            
        else:
            print("Opción inválida")

if __name__ == "__main__":
    gestionar_estudiantes()
