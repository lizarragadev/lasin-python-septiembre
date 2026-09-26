"""
==============================================================================
MÓDULO 5 — LECCIÓN 3: INTRODUCCIÓN A LA PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE DE POO:
1. Clase (Class): Es el plano, molde o plantilla que define las propiedades y
   comportamientos que tendrán los objetos creados a partir de ella.

2. Objeto (Instancia): Es un elemento concreto construido en memoria usando el molde de la Clase.

3. Atributos y el Método Constructor __init__(self, ...):
   - Atributos: Variables asociadas a cada objeto (ej. marca, modelo, anio).
   - __init__: Método especial que se ejecuta automáticamente al instanciar un objeto.
   - 'self': Referencia obligatoria dentro de la clase que apunta a la instancia actual del objeto.

4. Métodos: Funciones declaradas dentro de una clase que representan las acciones que el objeto puede realizar.

5. Herencia: Permite que una clase hija (Subclase) herede atributos y métodos de una clase padre (Superclase).
   - super().__init__(...): Llama al constructor de la clase padre para reutilizar su lógica.
==============================================================================
"""

print("=== INTRODUCCIÓN A LA PROGRAMACIÓN ORIENTADA A OBJETOS (POO) ===\n")

# ==============================================================================
# 1. SUPERCLASE PADRE: VEHICULO
# ==============================================================================
class Vehiculo:
    """Clase base que define la estructura general de cualquier vehículo."""

    def __init__(self, marca: str, modelo: str, anio: int):
        # Asignamos los argumentos a los atributos del objeto usando 'self.'
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.encendido = False  # Estado inicial por defecto (aperturado apagado)

    def encender(self):
        """Método de instancia que cambia el estado del vehículo a encendido."""
        self.encendido = True
        print(f"✓ El vehículo {self.marca} {self.modelo} ha sido encendido.")

    def obtener_informacion(self) -> str:
        """Devuelve una representación formateada del vehículo."""
        estado = "Encendido" if self.encendido else "Apagado"
        return f"{self.anio} {self.marca} {self.modelo} [{estado}]"


# ==============================================================================
# 2. SUBCLASE HIJA: AUTO (HEREDA DE VEHICULO)
# ==============================================================================
class Auto(Vehiculo):
    """Subclase Auto que extiende de Vehiculo añadiendo el atributo 'num_puertas'."""

    def __init__(self, marca: str, modelo: str, anio: int, num_puertas: int):
        # super().__init__() invoca al constructor de Vehiculo para inicializar marca, modelo y anio
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def abrir_maletero(self):
        """Método exclusivo de la clase Auto."""
        print(f"🚗 Abriendo maletero del auto {self.marca} {self.modelo}.")


# ==============================================================================
# 3. SUBCLASE HIJA: MOTO (HEREDA DE VEHICULO)
# ==============================================================================
class Moto(Vehiculo):
    """Subclase Moto que extiende de Vehiculo añadiendo el atributo 'cilindrada'."""

    def __init__(self, marca: str, modelo: str, anio: int, cilindrada: int):
        super().__init__(marca, modelo, anio)
        self.cilindrada = cilindrada

    def hacer_caballito(self):
        """Método exclusivo de la clase Moto."""
        print(f"🏍️ La moto {self.marca} {self.modelo} ({self.cilindrada}cc) hace una maniobra.")


# ==============================================================================
# PRUEBAS E INSTANCIACIÓN DE OBJETOS EN MEMORIA
# ==============================================================================
print("--- INSTANCIACIÓN Y USO DE OBJETOS ---")

# Instanciamos un objeto de la clase Auto
mi_auto = Auto(marca="Toyota", modelo="Corolla", anio=2023, num_puertas=4)
print("Información del auto:", mi_auto.obtener_informacion())
mi_auto.encender()         # Llamamos al método heredado de Vehiculo
mi_auto.abrir_maletero()   # Llamamos al método propio de Auto

print("-" * 45)

# Instanciamos un objeto de la clase Moto
mi_moto = Moto(marca="Honda", modelo="CB500", anio=2024, cilindrada=500)
print("Información de la moto:", mi_moto.obtener_informacion())
mi_moto.encender()         # Llamamos al método heredado de Vehiculo
mi_moto.hacer_caballito()  # Llamamos al método propio de Moto
