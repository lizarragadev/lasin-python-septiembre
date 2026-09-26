"""
Módulo 1 — Lección 8: Mini Proyecto Integrador (Calculadora Interactiva de Consola)
Curso: Python Nivel Básico - LASIN

Este mini proyecto integra todos los conceptos aprendidos en el Módulo 1:
- Entrada y salida de datos (input / print)
- Conversión explícita de tipos (float, int)
- Operadores aritméticos (+, -, *, /, **, %)
- Librería de funciones matemáticas (math.sqrt, math.pow, math.ceil, math.floor)
- Formateo de salidas profesionales con f-strings
"""

import math

print("==================================================")
print("     MINI PROYECTO: CALCULADORA DE CONSOLA      ")
print("                  CURSO LASIN                     ")
print("==================================================\n")

# 1. BIENVENIDA E INGRESO DE DATOS
print("Bienvenido a la calculadora interactiva.")
nombre_usuario = input("Por favor, ingresa tu nombre: ").strip().title()

print(f"\n¡Hola, {nombre_usuario}! Vamos a realizar un análisis numérico de dos valores.\n")

# Solicitamos dos números al usuario
num1_str = input("Ingresa el PRIMER número: ")
num2_str = input("Ingresa el SEGUNDO número: ")

# Conversión a flotante (decimal)
num1 = float(num1_str)
num2 = float(num2_str)

print("\n" + "=" * 50)
print(f"       RESULTADOS PARA {num1} Y {num2}")
print("=" * 50)

# 2. OPERACIONES ARITMÉTICAS BÁSICAS
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else None
potencia = math.pow(num1, num2)
modulo = num1 % num2 if num2 != 0 else None

print(f"1. Suma ({num1} + {num2}):              {suma:.2f}")
print(f"2. Resta ({num1} - {num2}):             {resta:.2f}")
print(f"3. Multiplicación ({num1} * {num2}):     {multiplicacion:.2f}")

if division is not None:
    print(f"4. División ({num1} / {num2}):           {division:.4f}")
    print(f"   -> Redondeo hacia arriba (ceil):    {math.ceil(division)}")
    print(f"   -> Redondeo hacia abajo (floor):   {math.floor(division)}")
else:
    print("4. División:                       No es posible dividir entre 0")

print(f"5. Potenciación ({num1} ^ {num2}):        {potencia:.2f}")

if modulo is not None:
    print(f"6. Módulo / Residuo ({num1} % {num2}):    {modulo:.2f}")
else:
    print("6. Módulo:                         Indefinido para divisor 0")


# 3. ANÁLISIS CON LA LIBRERÍA MATH
print("\n" + "-" * 50)
print("       OPERACIONES AVANZADAS (CON MÓDULO MATH)")
print("-" * 50)

# Raíz cuadrada del primer número (solo si es positivo)
if num1 >= 0:
    raiz_num1 = math.sqrt(num1)
    print(f"• Raíz cuadrada de {num1}:            {raiz_num1:.4f}")
else:
    print(f"• Raíz cuadrada de {num1}:            No definida para números negativos")

# Raíz cuadrada del segundo número (solo si es positivo)
if num2 >= 0:
    raiz_num2 = math.sqrt(num2)
    print(f"• Raíz cuadrada de {num2}:            {raiz_num2:.4f}")
else:
    print(f"• Raíz cuadrada de {num2}:            No definida para números negativos")

# Constantes de referencia
print(f"• Constante Pi (π) multiplicada por {num1}: {math.pi * num1:.4f}")

print("\n" + "=" * 50)
print(f"  ¡Gracias por usar la calculadora, {nombre_usuario}!")
print("=" * 50)
