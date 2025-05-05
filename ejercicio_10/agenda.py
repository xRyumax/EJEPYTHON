class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def saludo(self):
        return f"Hola, soy {self.nombre}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre} - Tel: {self.telefono}"

class Amigo(Contacto):
    def __init__(self, nombre, telefono, email, cumpleanos):
        super().__init__(nombre, telefono, email)
        self.cumpleanos = cumpleanos
    
    def saludo(self):
        return f"¡Hola! Soy tu amigo {self.nombre}"

class Familiar(Contacto):
    def __init__(self, nombre, telefono, email, parentesco):
        super().__init__(nombre, telefono, email)
        self.parentesco = parentesco
    
    def saludo(self):
        return f"¡Hola querido/a! Soy tu {self.parentesco} {self.nombre}"

class Trabajo(Contacto):
    def __init__(self, nombre, telefono, email, empresa):
        super().__init__(nombre, telefono, email)
        self.empresa = empresa
    
    def saludo(self):
        return f"Buenos días, soy {self.nombre} de {self.empresa}"

class Agenda:
    def __init__(self):
        self.contactos = []
    
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
    
    def buscar_contacto(self, nombre):
        return [c for c in self.contactos if nombre.lower() in c.nombre.lower()]
    
    def menu(self):
        while True:
            print("\n=== AGENDA DE CONTACTOS ===")
            print("1. Agregar contacto")
            print("2. Buscar contacto")
            print("3. Ver todos los contactos")
            print("4. Hacer que contacto salude")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print("\nTipo de contacto:")
                print("1. Amigo")
                print("2. Familiar")
                print("3. Trabajo")
                
                tipo = input("Seleccione el tipo: ")
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                
                if tipo == "1":
                    cumpleanos = input("Fecha de cumpleaños: ")
                    contacto = Amigo(nombre, telefono, email, cumpleanos)
                elif tipo == "2":
                    parentesco = input("Parentesco: ")
                    contacto = Familiar(nombre, telefono, email, parentesco)
                elif tipo == "3":
                    empresa = input("Empresa: ")
                    contacto = Trabajo(nombre, telefono, email, empresa)
                else:
                    print("Tipo no válido")
                    continue
                
                self.agregar_contacto(contacto)
                print("Contacto agregado exitosamente")
                
            elif opcion == "2":
                nombre = input("Ingrese el nombre a buscar: ")
                resultados = self.buscar_contacto(nombre)
                if resultados:
                    print("\nContactos encontrados:")
                    for contacto in resultados:
                        print(contacto)
                else:
                    print("No se encontraron contactos")
                    
            elif opcion == "3":
                if not self.contactos:
                    print("No hay contactos en la agenda")
                else:
                    print("\nTodos los contactos:")
                    for contacto in self.contactos:
                        print(contacto)
                        
            elif opcion == "4":
                if not self.contactos:
                    print("No hay contactos en la agenda")
                else:
                    print("\nSeleccione un contacto:")
                    for i, contacto in enumerate(self.contactos, 1):
                        print(f"{i}. {contacto}")
                    
                    try:
                        idx = int(input("Número de contacto: ")) - 1
                        if 0 <= idx < len(self.contactos):
                            print("\nSaludo del contacto:")
                            print(self.contactos[idx].saludo())
                        else:
                            print("Contacto no válido")
                    except ValueError:
                        print("Entrada inválida")
                        
            elif opcion == "5":
                print("¡Hasta luego!")
                break
                
            else:
                print("Opción inválida")

if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()
