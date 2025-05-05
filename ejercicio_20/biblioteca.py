class Material:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.prestado = False
    
    def tipo_material(self):
        return "Material genérico"
    
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False
    
    def devolver(self):
        if self.prestado:
            self.prestado = False
            return True
        return False
    
    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"{self.tipo_material()}: {self.titulo} ({self.anio}) - {estado}"

class Libro(Material):
    def __init__(self, titulo, autor, anio, isbn, editorial):
        super().__init__(titulo, autor, anio)
        self.isbn = isbn
        self.editorial = editorial
    
    def tipo_material(self):
        return "Libro"

class Revista(Material):
    def __init__(self, titulo, autor, anio, numero, volumen):
        super().__init__(titulo, autor, anio)
        self.numero = numero
        self.volumen = volumen
    
    def tipo_material(self):
        return "Revista"

class Tesis(Material):
    def __init__(self, titulo, autor, anio, universidad, grado):
        super().__init__(titulo, autor, anio)
        self.universidad = universidad
        self.grado = grado
    
    def tipo_material(self):
        return "Tesis"

class Biblioteca:
    def __init__(self):
        self.materiales = []
    
    def agregar_material(self, material):
        self.materiales.append(material)
        print(f"Material agregado: {material}")
    
    def buscar_por_titulo(self, titulo):
        return [m for m in self.materiales if titulo.lower() in m.titulo.lower()]
    
    def contar_por_tipo(self):
        conteo = {"Libro": 0, "Revista": 0, "Tesis": 0}
        for material in self.materiales:
            conteo[material.tipo_material()] += 1
        return conteo
    
    def listar_prestados(self):
        return [m for m in self.materiales if m.prestado]
    
    def menu(self):
        while True:
            print("\n=== BIBLIOTECA PYTHON ===")
            print("1. Agregar material")
            print("2. Buscar por título")
            print("3. Ver estadísticas")
            print("4. Prestar material")
            print("5. Devolver material")
            print("6. Ver materiales prestados")
            print("7. Salir")
            
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                print("\nTipo de material:")
                print("1. Libro")
                print("2. Revista")
                print("3. Tesis")
                
                tipo = input("Seleccione el tipo: ")
                titulo = input("Título: ")
                autor = input("Autor: ")
                try:
                    anio = int(input("Año: "))
                    
                    if tipo == "1":
                        isbn = input("ISBN: ")
                        editorial = input("Editorial: ")
                        self.agregar_material(Libro(titulo, autor, anio, isbn, editorial))
                    elif tipo == "2":
                        numero = input("Número: ")
                        volumen = input("Volumen: ")
                        self.agregar_material(Revista(titulo, autor, anio, numero, volumen))
                    elif tipo == "3":
                        universidad = input("Universidad: ")
                        grado = input("Grado académico: ")
                        self.agregar_material(Tesis(titulo, autor, anio, universidad, grado))
                    else:
                        print("Tipo no válido")
                except ValueError:
                    print("Año inválido")
                    
            elif opcion == "2":
                titulo = input("Ingrese el título a buscar: ")
                resultados = self.buscar_por_titulo(titulo)
                if resultados:
                    print("\nResultados encontrados:")
                    for material in resultados:
                        print(material)
                else:
                    print("No se encontraron materiales")
                    
            elif opcion == "3":
                conteo = self.contar_por_tipo()
                print("\nEstadísticas de la biblioteca:")
                for tipo, cantidad in conteo.items():
                    print(f"{tipo}s: {cantidad}")
                print(f"Total de materiales: {len(self.materiales)}")
                print(f"Materiales prestados: {len(self.listar_prestados())}")
                
            elif opcion == "4":
                if not self.materiales:
                    print("No hay materiales en la biblioteca")
                    continue
                    
                print("\nMateriales disponibles:")
                disponibles = [m for m in self.materiales if not m.prestado]
                for i, material in enumerate(disponibles, 1):
                    print(f"{i}. {material}")
                
                try:
                    idx = int(input("Seleccione el número del material: ")) - 1
                    if 0 <= idx < len(disponibles):
                        if disponibles[idx].prestar():
                            print("Material prestado exitosamente")
                        else:
                            print("El material ya está prestado")
                    else:
                        print("Número no válido")
                except ValueError:
                    print("Entrada inválida")
                    
            elif opcion == "5":
                prestados = self.listar_prestados()
                if not prestados:
                    print("No hay materiales prestados")
                    continue
                
                print("\nMateriales prestados:")
                for i, material in enumerate(prestados, 1):
                    print(f"{i}. {material}")
                
                try:
                    idx = int(input("Seleccione el número del material: ")) - 1
                    if 0 <= idx < len(prestados):
                        if prestados[idx].devolver():
                            print("Material devuelto exitosamente")
                        else:
                            print("El material no estaba prestado")
                    else:
                        print("Número no válido")
                except ValueError:
                    print("Entrada inválida")
                    
            elif opcion == "6":
                prestados = self.listar_prestados()
                if prestados:
                    print("\nMateriales actualmente prestados:")
                    for material in prestados:
                        print(material)
                else:
                    print("No hay materiales prestados")
                    
            elif opcion == "7":
                print("\n¡Gracias por usar la biblioteca!")
                break
                
            else:
                print("Opción inválida")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    # Agregar algunos materiales de ejemplo
    biblioteca.agregar_material(Libro("Python para todos", "John Smith", 2020, "123-456", "Tech Books"))
    biblioteca.agregar_material(Revista("Ciencia Hoy", "Varios", 2023, "45", "12"))
    biblioteca.agregar_material(Tesis("IA en educación", "María García", 2022, "Universidad Nacional", "Doctorado"))
    biblioteca.menu()
