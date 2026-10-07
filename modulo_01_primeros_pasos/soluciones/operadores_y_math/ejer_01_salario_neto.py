"""
==============================================================================
SOLUCIÓN — MÓDULO 1 — TEMA 2 — EJERCICIO 1: SALARIO NETO DE EMPLEADOS
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Definimos las tasas de descuento como constantes por convención (TASA_AFP, TASA_IVA).
2. Aplicamos la precedencia de operadores para restar primero los aportes obligatorios.
3. Sumamos el bono fijo de transporte al salario resultante.
4. Formateamos las salidas monetarias usando comas de miles y 2 decimales (:,.2f).
"""

# Constantes por convención
TASA_AFP = 0.1271          # 12.71% para fondo de jubilación
TASA_RC_IVA = 0.13         # 13% de impuesto RC-IVA
BONO_TRANSPORTE = 250.00   # Bono de transporte fijo en Bs.

print("=== CALCULADORA DE PLANILLA DE SUELDO Y SALARIO NETO ===\n")

# Captura del salario bruto
entrada_salario = input("Ingrese el Salario Bruto del empleado (Bs.) [Default: 8500.00]: ").strip()
salario_bruto = float(entrada_salario) if entrada_salario else 8500.00

# 1. Cálculo del descuento para fondo de jubilación (AFP)
descuento_afp = salario_bruto * TASA_AFP

# 2. Base imponible para el impuesto RC-IVA
monto_imponible = salario_bruto - descuento_afp
descuento_iva = monto_imponible * TASA_RC_IVA

# 3. Total deducciones
total_deducciones = descuento_afp + descuento_iva

# 4. Salario Neto final
salario_neto = salario_bruto - total_deducciones + BONO_TRANSPORTE

# Despliegue de la liquidación de sueldo
print("\n" + "=" * 45)
print("     LIQUIDACIÓN DE SUELDO Y PLANILLA (BOB)   ")
print("=" * 45)
print(f"• Salario Bruto Ingresado:   Bs. {salario_bruto:>10,.2f}")
print(f"• Deducción AFP (12.71%):     Bs. {descuento_afp:>10,.2f}")
print(f"• Deducción RC-IVA (13%):     Bs. {descuento_iva:>10,.2f}")
print(f"• Total Deducciones:          Bs. {total_deducciones:>10,.2f}")
print(f"• Bono de Transporte (+):     Bs. {BONO_TRANSPORTE:>10,.2f}")
print("-" * 45)
print(f"• SALARIO NETO A COBRAR:      Bs. {salario_neto:>10,.2f}")
print("=" * 45)
