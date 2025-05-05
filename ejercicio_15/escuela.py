class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def rol(self):
        return "Persona en la institución"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        self.notas = []
    
    def rol(self):
        return "Estudiante: Aprende y se desarrolla"
    
    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            return True
        return False
    
    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def esta_aprobado(self):
        return self.promedio() >= 6

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia
        self.estudiantes = []
    
    def rol(self):
        return f"Profesor: Enseña {self.materia}"
    
    def agregar_estudiante(self, estudiante):
        if isinstance(estudiante, Estudiante):
            self.estudiantes.append(estudiante)
            return True
        return False

class SistemaEscolar:
    def __init__(self):
        self.personas = []
    
    def agregar_persona(self, persona):
        self.personas.append(persona)
    
    def mostrar_estadisticas(self):
        print("\n=== ESTADÍSTICAS DEL SISTEMA ESCOLAR ===")
        
        estudiantes = [p for p in self.personas if isinstance(p, Estudiante)]
        profesores = [p for p in self.personas if isinstance(p, Profesor)]
        
        print(f"\nTotal de personas: {len(self.personas)}")
        print(f"Total de estudiantes: {len(estudiantes)}")
        print(f"Total de profesores: {len(profesores)}")
        
        if estudiantes:
            aprobados = sum(1 for e in estudiantes if e.esta_aprobado())
            print(f"\nEstudiantes aprobados: {aprobados}")
            print(f"Estudiantes reprobados: {len(estudiantes) - aprobados}")
            
            promedio_general = sum(e.promedio() for e in estudiantes) / len(estudiantes)
            print(f"Promedio general: {promedio_general:.2f}")

def demo_sistema():
    sistema = SistemaEscolar()
    
    # Crear algunos profesores
    prof_mate = Profesor("Juan Pérez", 45, "Matemáticas")
    prof_hist = Profesor("María García", 38, "Historia")
    
    # Crear algunos estudiantes
    estudiantes = [
        Estudiante("Ana López", 15, "1°A"),
        Estudiante("Carlos Ruiz", 16, "1°A"),
        Estudiante("Laura Torres", 15, "1°A")
    ]
    
    # Agregar notas a los estudiantes
    for estudiante in estudiantes:
        # Agregar notas aleatorias entre 4 y 10
        from random import uniform
        for _ in range(4):
            estudiante.agregar_nota(uniform(4, 10))
    
    # Agregar todas las personas al sistema
    sistema.agregar_persona(prof_mate)
    sistema.agregar_persona(prof_hist)
    for estudiante in estudiantes:
        sistema.agregar_persona(estudiante)
    
    # Mostrar información
    print("=== SISTEMA ESCOLAR ===")
    print("\nPersonas en el sistema:")
    for persona in sistema.personas:
        print(f"{persona} - {persona.rol()}")
        if isinstance(persona, Estudiante):
            print(f"  Promedio: {persona.promedio():.2f}")
            print(f"  Estado: {'Aprobado' if persona.esta_aprobado() else 'Reprobado'}")
    
    # Mostrar estadísticas
    sistema.mostrar_estadisticas()

if __name__ == "__main__":
    demo_sistema()
