"""
==============================================================================
MÓDULO 1 — LECCIÓN 4: OPERADORES ARITMÉTICOS, PRECEDENCIA Y MÓDULO MATH
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Operadores Aritméticos:
   - Suma (+), Resta (-), Multiplicación (*), División Decimal (/)
   - División Entera (//): Descarta los decimales y devuelve la parte entera.
   - Módulo (%): Devuelve el RESIDUO o sobrante de una división entera.
   - Potenciación (**): Eleva un número a una potencia (ej. 2**3 = 8).

2. Precedencia de Operadores:
   - Python evalúa primero los Paréntesis (), luego Potencias (**), luego Multiplicación/División (*, /, //, %), y finalmente Sumas/Restas (+, -).

3. Módulo 'math' de la Librería Estándar de Python:
   - Proporciona constantes como math.pi y math.e.
   - Proporciona funciones avanzadas: math.sqrt() (raíz), math.ceil() (redondeo hacia arriba),
     math.floor() (redondeo hacia abajo), math.factorial() (factorial).
==============================================================================
"""

import math  # Cargamos la librería matemática nativa de Python

print("=== OPERACIONES ARITMÉTICAS Y LIBRERÍA MATH ===\n")

# Solicitamos dos datos numéricos para procesar
monto_total_bs = float(input("Ingrese el Monto Total de la Venta (Bs.): "))
unidades = int(input("Ingrese la Cantidad de Unidades Compradas: "))


# ==============================================================================
# 1. OPERADORES ARITMÉTICOS Y CÁLCULOS FINANCIEROS
# ==============================================================================
print("\n--- 1. CÁLCULOS ARITMÉTICOS BÁSICOS Y FINANCIEROS ---")

# Precedencia: Los paréntesis se evalúan primero
precio_unitario = monto_total_bs / unidades if unidades > 0 else 0.0

# Impuesto IVA (13%): Se calcula multiplicando por 0.13
impuesto_iva = monto_total_bs * 0.13

# Subtotal Neto: Restamos el IVA del total
monto_neto_sin_iva = monto_total_bs - impuesto_iva

# Potenciación (**): Monto elevado al cuadrado
monto_al_cuadrado = monto_total_bs ** 2

# DIVISIÓN ENTERA (//) Y MÓDULO (%): Aplicación práctica en Logística
# Supongamos que empacamos unidades en cajas con capacidad de 6 unidades cada una:
CAPACIDAD_CAJA = 6
cajas_completas = unidades // CAPACIDAD_CAJA   # // Devuelve cuántas cajas llenas de 6 u. se completan
unidades_sobrantes = unidades % CAPACIDAD_CAJA # % Devuelve cuántas unidades quedan sueltas fuera de caja

print(f"• Monto Total de la Venta:      Bs. {monto_total_bs:.2f}")
print(f"• Unidades ingresadas:          {unidades} unidades")
print(f"• Precio Unitario Calculado:    Bs. {precio_unitario:.2f}")
print(f"• Impuesto IVA Débito (13%):    Bs. {impuesto_iva:.2f}")
print(f"• Monto Neto (Sin IVA):         Bs. {monto_neto_sin_iva:.2f}")
print(f"• Empaque (Cajas de {CAPACIDAD_CAJA} u.):   {cajas_completas} cajas llenas y {unidades_sobrantes} unidades sueltas")


# ==============================================================================
# 2. FUNCIONES Y CONSTANTES DEL MÓDULO MATH
# ==============================================================================
print("\n--- 2. FUNCIONES MATEMÁTICAS AVANZADAS (MÓDULO MATH) ---")

# Constantes universales precargadas en Python
print(f"• Constante Pi (math.pi):         {math.pi}")
print(f"• Número de Euler (math.e):       {math.e}")

# DIFERENCIA ENTRE REDONDEO CEIL Y FLOOR:
# - math.ceil(x): Redondea SIEMPRE HACIA ARRIBA al entero más cercano.
#   ¿Cuándo usarlo?: Para saber cuántas cajas comprar (si tengo 7 u. y caben 6 por caja, necesito 2 cajas).
# - math.floor(x): Redondea SIEMPRE HACIA ABAJO al entero más cercano.

cajas_totales_necesarias = math.ceil(unidades / CAPACIDAD_CAJA) if unidades > 0 else 0
precio_entero_abajado = math.floor(precio_unitario)

print(f"• Cajas totales requeridas (math.ceil):  {cajas_totales_necesarias} cajas")
print(f"• Precio entero redondeado abajo (math.floor): {precio_entero_abajado} Bs.")

# Funciones adicionales: Raíz Cuadrada, Factorial y Logaritmo
if monto_total_bs >= 0:
    print(f"• Raíz Cuadrada del Monto (math.sqrt):    {math.sqrt(monto_total_bs):.4f}")
    
    # Factorial (n! = n * (n-1) * ... * 1) -> Definido solo para enteros no negativos
    if unidades <= 12:
        print(f"• Factorial de unidades ({unidades}!):       {math.factorial(unidades)}")
    else:
        print(f"• Factorial de {unidades}: Valor demasiado grande para calcular en pantalla")

if monto_total_bs > 0:
    print(f"• Logaritmo Natural del Monto (math.log): {math.log(monto_total_bs):.4f}")
