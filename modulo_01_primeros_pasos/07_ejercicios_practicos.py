"""
Módulo 1 — Lección 7: Ejercicios Prácticos de Aplicación
Curso: Python Nivel Básico - LASIN

En este archivo se agrupan los ejercicios resueltos y demostraciones prácticas
vistas en clase, además de utilidades cotidianas:
1. Calculadora de Edad (a partir del año de nacimiento o edad actual).
2. Conversor de Monedas (USD a Bolivianos Bs.).
3. Cálculo del Área y Perímetro de un Círculo (usando math.pi).
4. Calculadora de Propina y División de Cuenta.
"""

import math
from datetime import datetime

print("==================================================")
print("     EJERCICIOS PRÁCTICOS INTEGRADOS - MÓDULO 1   ")
print("==================================================\n")


# ==================================================
# EJERCICIO 1: CALCULADORA DE EDAD
# ==================================================
print("--- 1. CALCULADORA DE EDAD ---")
# Método A: Calcular año aproximado de nacimiento dada la edad
edad_usuario = int(input("Ingrese su edad actual: "))
anio_actual = datetime.now().year
anio_nacimiento = anio_actual - edad_usuario

print(f"-> Si tienes {edad_usuario} años, naciste aproximadamente en el año {anio_nacimiento}.")
print(f"-> Te faltan {100 - edad_usuario} años para cumplir 100 años.\n")


# ==================================================
# EJERCICIO 2: CONVERSOR DE MONEDAS (USD -> BOB)
# ==================================================
print("--- 2. CONVERSOR DE DÓLARES A BOLIVIANOS ---")
TASA_OFICIAL_BOB = 11.06  # Constante por convención

dolares = float(input("Monto en dólares ($ USD): "))
bolivianos = dolares * TASA_OFICIAL_BOB

# Formateamos la salida a 2 decimales usando f-strings
print(f"-> Tipo de cambio aplicado: 1 USD = Bs. {TASA_OFICIAL_BOB}")
print(f"-> {dolares:.1f} USD equivalen a: Bs. {bolivianos:.2f}\n")


# ==================================================
# EJERCICIO 3: CÁLCULO DE ÁREA Y PERÍMETRO DE UN CÍRCULO
# ==================================================
print("--- 3. CÁLCULO DE GEOMETRÍA: CÍRCULO ---")
radio = float(input("Ingrese el Radio del círculo (en cm): "))

# Fórmulas geométricas:
# Área = π * r^2
# Perímetro (Circunferencia) = 2 * π * r
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print(f"-> Radio ingresado: {radio} cm")
print(f"-> Área del círculo: {area:.2f} cm²")
print(f"-> Perímetro (circunferencia): {perimetro:.2f} cm\n")


# ==================================================
# EJERCICIO 4: CALCULADORA DE PROPINA Y DIVISIÓN DE CUENTA
# ==================================================
print("--- 4. DIVISOR DE CUENTAS DE RESTAURANTE ---")
total_cuenta = float(input("Monto total de la cuenta (Bs.): "))
porcentaje_propina = float(input("Porcentaje de propina a incluir (%): "))
num_personas = int(input("Número de personas para dividir la cuenta: "))

# Cálculos
monto_propina = total_cuenta * (porcentaje_propina / 100)
gran_total = total_cuenta + monto_propina
pago_por_persona = gran_total / num_personas

print(f"\nResumen de la cuenta:")
print(f"-> Subtotal: Bs. {total_cuenta:.2f}")
print(f"-> Propina ({porcentaje_propina:.0f}%): Bs. {monto_propina:.2f}")
print(f"-> Total General: Bs. {gran_total:.2f}")
print(f"-> Cada persona debe pagar: Bs. {pago_por_persona:.2f}")
