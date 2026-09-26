"""
==============================================================================
MÓDULO 1 — LECCIÓN 3: CAPTURA (input) Y DESPLIEGUE (print) DE DATOS
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. input(): Función que pausa la ejecución del programa y espera a que el usuario
   escriba un valor en la terminal y presione ENTER.
   ⚠️ REGLA DE ORO DE input(): SIEMPRE devuelve un valor de tipo Texto (str),
   incluso si el usuario escribe un número como "25" o "150.50".

2. Conversión de Tipos (Casting): Proceso de transformar explícitamente un dato de
   un tipo a otro (ej. convertir "150.50" de texto a float) para poder realizar
   cálculos matemáticos.

3. Formas de Formatear la Salida con print():
   - Concatenación (+): Une textos. Exige que todos los elementos sean de tipo str.
   - Comas (,): Imprime múltiples argumentos, añade espacios entre ellos y convierte automáticamente a texto.
   - Caracteres de escape (\\n): Permite estructurar bloques multilínea.
==============================================================================
"""

print("==================================================")
print("     SISTEMA INTERACTIVO DE CAPTURA DE REGISTROS  ")
print("==================================================\n")

# ==============================================================================
# 1. CAPTURA DE DATOS INTERACTIVA CON input()
# ==============================================================================
# El texto que pasamos dentro de input("...") es el mensaje o prompt que ve el usuario.

nombre_empresa = input("Ingrese el Nombre de la Empresa Cliente: ") # Devuelve str (ej. "Comercial Alfa")
ciudad = input("Ingrese la Ciudad sede (ej. La Paz, Santa Cruz): ")   # Devuelve str (ej. "La Paz")
monto_str = input("Ingrese el Monto de la Venta (Bs.): ")            # Devuelve str (ej. "4500.50")
nit_str = input("Ingrese el NIT / Nro de Registro Fiscal: ")         # Devuelve str (ej. "1020304050")

# Constantes adicionales de apoyo
ENTIDAD_PROCESADORA = "LASIN Data Engine"
es_estudiante = False


# ==============================================================================
# 2. CONVERSIÓN EXPLÍCITA DE TIPOS (CASTING)
# ==============================================================================
# Si intentáramos multiplicar 'monto_str * 2', Python repetiría el texto dos veces ("4500.504500.50")
# en lugar de hacer la multiplicación matemática. Por eso DEBEMOS hacer casting.

# .replace('.', '', 1).isdigit() verifica si el texto contiene solo dígitos numéricos (permitiendo un punto)
if monto_str.replace('.', '', 1).isdigit():
    monto_venta = float(monto_str)  # Casting de str -> float
else:
    print("⚠️ Advertencia: Monto no válido. Se asignó 0.0 por defecto.")
    monto_venta = 0.0

if nit_str.isdigit():
    nit_registro = int(nit_str)     # Casting de str -> int
else:
    print("⚠️ Advertencia: NIT no válido. Se asignó 0 por defecto.")
    nit_registro = 0


# ==============================================================================
# 3. FORMAS DE MOSTRAR LA INFORMACIÓN EN PANTALLA
# ==============================================================================

# ------------------------------------------------------------------------------
# FORMA 1: Concatenación manual usando el operador '+'
# ------------------------------------------------------------------------------
# NOTA IMPORTANTE: Si intentas hacer: print("Monto: " + monto_venta) Python lanzará un
# TypeError porque no se puede sumar automáticamente texto con números flotantes.
# Debemos envolve cada número en str(monto_venta).

print("\n--- FORMA 1: Concatenación manual con '+' (Requiere str() explícito) ---")
print("Cliente: " + nombre_empresa)
print("Sede: " + ciudad)
print("Monto Registrado: Bs. " + str(monto_venta))  # str() convierte float a texto
print("NIT Registrado: " + str(nit_registro))      # str() convierte int a texto
print("Procesador: " + ENTIDAD_PROCESADORA)


# ------------------------------------------------------------------------------
# FORMA 2: Múltiples argumentos en print() separados por comas ','
# ------------------------------------------------------------------------------
# Al separar por comas, Python convierte los tipos internamente a texto e inserta
# un espacio en blanco entre cada argumento automáticamente.

print("\n--- FORMA 2: Impresión limpia con comas ',' ---")
print("El cliente", nombre_empresa, "ubicado en", ciudad, "registró Bs.", monto_venta)


# ------------------------------------------------------------------------------
# FORMA 3: Salida Multilínea en un solo bloque usando '\\n'
# ------------------------------------------------------------------------------
# '\\n' representa un salto de línea (Enter). Es muy útil para armar plantillas o comprobantes.

print("\n--- FORMA 3: Comprobante Multilínea en un solo print() con '\\n' ---")
comprobante = (
    "==================================================\n" +
    "           COMPROBANTE DE REGISTRO EMITIDO        \n" +
    "==================================================\n" +
    "Empresa Cliente: " + nombre_empresa + "\n" +
    "Ciudad Sede:     " + ciudad + "\n" +
    "NIT Registrado:  " + str(nit_registro) + "\n" +
    "Monto Venta:     Bs. " + str(monto_venta) + "\n" +
    "Procesador:      " + ENTIDAD_PROCESADORA + "\n" +
    "=================================================="
)

print(comprobante)
