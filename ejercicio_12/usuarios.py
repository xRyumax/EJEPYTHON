class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    
    def mostrar_privilegios(self):
        return ["Ver contenido público"]
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre}"

class Administrador(Usuario):
    def mostrar_privilegios(self):
        return [
            "Ver contenido público",
            "Crear usuarios",
            "Eliminar usuarios",
            "Modificar configuración",
            "Acceso total al sistema"
        ]

class Cliente(Usuario):
    def __init__(self, nombre, email, nivel="básico"):
        super().__init__(nombre, email)
        self.nivel = nivel
    
    def mostrar_privilegios(self):
        privilegios = super().mostrar_privilegios()
        if self.nivel == "premium":
            privilegios.extend([
                "Acceso a contenido premium",
                "Soporte prioritario"
            ])
        return privilegios

def gestionar_usuarios():
    usuarios = [
        Administrador("Admin1", "admin1@sistema.com"),
        Cliente("Cliente1", "cliente1@email.com", "básico"),
        Cliente("Cliente2", "cliente2@email.com", "premium"),
        Administrador("Admin2", "admin2@sistema.com")
    ]
    
    print("=== SISTEMA DE USUARIOS ===")
    for usuario in usuarios:
        print(f"\n{usuario}")
        print("Privilegios:")
        for privilegio in usuario.mostrar_privilegios():
            print(f"- {privilegio}")
    
    # Estadísticas
    print("\nEstadísticas del sistema:")
    total_admins = sum(1 for u in usuarios if isinstance(u, Administrador))
    total_clientes = sum(1 for u in usuarios if isinstance(u, Cliente))
    clientes_premium = sum(1 for u in usuarios if isinstance(u, Cliente) and u.nivel == "premium")
    
    print(f"Total administradores: {total_admins}")
    print(f"Total clientes: {total_clientes}")
    print(f"Clientes premium: {clientes_premium}")

if __name__ == "__main__":
    gestionar_usuarios()
