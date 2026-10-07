"""
==============================================================================
SOLUCIÓN — MÓDULO 1 — TEMA 2 — EJERCICIO 2: PLANIFICADOR DE LOTES DE ENVÍO
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Usamos la división entera (//) para determinar cuántas cajas completas de 12 u. se forman.
2. Usamos el operador módulo (%) para saber cuántas unidades quedan sobrantes fuera de caja.
3. Usamos math.ceil() para calcular cuántas cajas completas e incompletas se necesitan en total.
"""

import math

print("=== PLANIFICACIÓN LOGÍSTICA DE EMPAQUE ===\n")

CAPACIDAD_CAJA = 12  # Constante: Unidades por caja

entrada_unidades = input("Ingrese la cantidad de unidades producidas [Default: 125]: ").strip()
unidades = int(entrada_unidades) if entrada_unidades.isdigit() else 125

# 1. Cajas completas (División entera //)
cajas_llenas = unidades // CAPACIDAD_CAJA

# 2. Unidades sobrantes (Residuo %)
unidades_sobrantes = unidades % CAPACIDAD_CAJA

# 3. Cajas totales necesarias (math.ceil redondea SIEMPRE hacia arriba)
cajas_totales = math.ceil(unidades / CAPACIDAD_CAJA) if unidades > 0 else 0

# Despliegue de resultados
print("\n" + "=" * 45)
print("     REPORTE LOGÍSTICO DE EMPAQUE (MATH)      ")
print("=" * 45)
print(f"• Total de Unidades Producidas:  {unidades} unidades")
print(f"• Cajas Llenas Completas (//):   {cajas_llenas} cajas ({cajas_llenas * CAPACIDAD_CAJA} u.)")
print(f"• Unidades Sobrantes (%):        {unidades_sobrantes} unidades sueltas")
print(f"• Cajas Totales a Comprar (ceil): {cajas_totales} cajas requeridas")
print("=" * 45)
