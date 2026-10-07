"""
==============================================================================
SOLUCIÓN — MÓDULO 1 — TEMA 1 — EJERCICIO 2: CONVERSOR DE TEMPERATURA
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Capturamos la entrada del usuario con input() o asignamos un valor inicial flotante.
2. Aplicamos la fórmula matemática para Fahrenheit: (C * 9/5) + 32.
3. Aplicamos la fórmula matemática para Kelvin: C + 273.15.
4. Formateamos la salida redondeando a 2 decimales con el especificador de f-strings ':.2f'.
"""

print("=== CONVERSOR DE TEMPERATURA METEOROLÓGICA ===\n")

# Solicitamos la temperatura o asignamos una entrada por defecto
entrada_str = input("Ingrese la temperatura en grados Celsius (°C) [Default: 21.5]: ").strip()
temperatura_celsius = float(entrada_str) if entrada_str else 21.5

# Cálculos basados en las fórmulas físicas
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
temperatura_kelvin = temperatura_celsius + 273.15

# Despliegue de resultados formateados
print("\n=== REPORTE DE CONVERSIÓN DE TEMPERATURA ===")
print(f"• Temperatura Celsius ingresada: {temperatura_celsius:.2f} °C")
print(f"• Conversión a Fahrenheit:       {temperatura_fahrenheit:.2f} °F")
print(f"• Conversión a Kelvin:           {temperatura_kelvin:.2f} K")
print("============================================")
