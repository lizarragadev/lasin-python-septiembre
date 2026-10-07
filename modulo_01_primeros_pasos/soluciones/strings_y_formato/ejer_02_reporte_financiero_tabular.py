"""
==============================================================================
SOLUCIÓN — MÓDULO 1 — TEMA 3 — EJERCICIO 2: REPORTE FINANCIERO TABULAR
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Definimos las variables de sucursales e ingresos.
2. Calculamos el total acumulado sumando las 3 sucursales.
3. Calculamos la participación porcentual (%) de cada sucursal.
4. Diseñamos la tabla usando especificadores de ancho en f-strings (<20, >15,.2f).
"""

print("=== GENERADOR DE REPORTE CONSOLIDADO TABULAR ===\n")

sucursal1, ingreso1 = "La Paz", 15400.50
sucursal2, ingreso2 = "Santa Cruz", 28900.00
sucursal3, ingreso3 = "Cochabamba", 8350.75

total_consolidado = ingreso1 + ingreso2 + ingreso3

pct1 = (ingreso1 / total_consolidado) * 100
pct2 = (ingreso2 / total_consolidado) * 100
pct3 = (ingreso3 / total_consolidado) * 100
pct_total = pct1 + pct2 + pct3

print("====================================================")
print("           REPORTE CONSOLIDADO DE SUCURSALES        ")
print("====================================================")
print(f"{'SUCURSAL Sede':<20} | {'INGRESO REGISTRADO':>18} | {'% TOTAL':>8}")
print("-" * 52)
print(f"{sucursal1:<20} | Bs. {ingreso1:>14,.2f} | {pct1:>7.2f}%")
print(f"{sucursal2:<20} | Bs. {ingreso2:>14,.2f} | {pct2:>7.2f}%")
print(f"{sucursal3:<20} | Bs. {ingreso3:>14,.2f} | {pct3:>7.2f}%")
print("-" * 52)
print(f"{'TOTAL CONSOLIDADO':<20} | Bs. {total_consolidado:>14,.2f} | {pct_total:>7.2f}%")
print("====================================================")
