"""
==============================================================================
MÓDULO 1 — LECCIÓN 7: DEMO — ANÁLISIS BÁSICO DE REGISTROS DE VENTAS
Curso: Python Nivel Básico - LASIN
==============================================================================

OBJETIVO DIDÁCTICO:
- Integrar la captura de datos (input), el manejo de excepciones de conversión,
  las funciones matemáticas nativas min() y max(), y el formateo de tablas
  con f-strings para construir un primer reporte cuantitativo de ventas.

CONCEPTOS UTILIZADOS:
1. input() con valores defensivos por defecto (si el usuario presiona Enter).
2. Funciones nativas min(v1, v2, ...) y max(v1, v2, ...).
3. Cálculo de la participación porcentual (%): (Venta / Total) * 100.
4. Formateo de columnas con anchos fijos (<15, >18,.2f).
==============================================================================
"""

print("==================================================")
print("     DEMO: ANÁLISIS BÁSICO DE VENTAS (MÓDULO 1)   ")
print("==================================================\n")

print("Capturando o asignando los montos de 4 ventas registradas en la jornada:")
print("(Presiona ENTER para aceptar el valor predeterminado de prueba)\n")

# Captura interactiva con valores por defecto defensivos
v1_str = input("Monto Venta 1 (Bs.) [Default: 1500.50]: ").strip()
v2_str = input("Monto Venta 2 (Bs.) [Default: 3200.00]: ").strip()
v3_str = input("Monto Venta 3 (Bs.) [Default: 450.00]:  ").strip()
v4_str = input("Monto Venta 4 (Bs.) [Default: 8900.25]: ").strip()

# Asignación defensiva: Si la cadena no está vacía, convierte a float; de lo contrario usa el valor por defecto
v1 = float(v1_str) if v1_str else 1500.50
v2 = float(v2_str) if v2_str else 3200.00
v3 = float(v3_str) if v3_str else 450.00
v4 = float(v4_str) if v4_str else 8900.25

# ==============================================================================
# 1. CÁLCULO DE MÉTRICAS ESTADÍSTICAS Y PORCENTAJES
# ==============================================================================
cantidad_registros = 4
total_ventas = v1 + v2 + v3 + v4
promedio_ventas = total_ventas / cantidad_registros

# min() y max() evalúan los argumentos pasados y retornan el menor o mayor valor
venta_maxima = max(v1, v2, v3, v4)
venta_minima = min(v1, v2, v3, v4)

# Cálculo de la cuota de participación (%) de cada venta sobre el total recaudado
pct_v1 = (v1 / total_ventas) * 100
pct_v2 = (v2 / total_ventas) * 100
pct_v3 = (v3 / total_ventas) * 100
pct_v4 = (v4 / total_ventas) * 100


# ==============================================================================
# 2. DESPLIEGUE DEL REPORTE DETALLADO EN PANTALLA
# ==============================================================================
print("\n" + "=" * 55)
print("       TABLA DE CONTRIBUCIÓN INDIVIDUAL DE VENTAS     ")
print("=" * 55)
print(f"{'REGISTRO':<15} | {'MONTO REGISTRADO':>18} | {'CONTRIBUCIÓN (%)'}")
print("-" * 55)
print(f"{'Venta N°1':<15} | Bs. {v1:>14,.2f} | {pct_v1:>15.2f}%")
print(f"{'Venta N°2':<15} | Bs. {v2:>14,.2f} | {pct_v2:>15.2f}%")
print(f"{'Venta N°3':<15} | Bs. {v3:>14,.2f} | {pct_v3:>15.2f}%")
print(f"{'Venta N°4':<15} | Bs. {v4:>14,.2f} | {pct_v4:>15.2f}%")
print("-" * 55)

print("\n" + "=" * 55)
print("            MÉTRICAS CONSOLIDADAS DEL DÍA          ")
print("=" * 55)
print(f"• Total de registros analizados:  {cantidad_registros} ventas")
print(f"• Total acumulado recaudado:       Bs. {total_ventas:,.2f}")
print(f"• Promedio por ticket de venta:    Bs. {promedio_ventas:,.2f}")
print(f"• Venta más alta del día (max()):  Bs. {venta_maxima:,.2f}")
print(f"• Venta más baja del día (min()):  Bs. {venta_minima:,.2f}")
print("=" * 55)
