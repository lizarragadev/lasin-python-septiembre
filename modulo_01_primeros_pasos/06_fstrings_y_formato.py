"""
==============================================================================
MÓDULO 1 — LECCIÓN 6: FORMATEO AVANZADO DE REPORTES CON F-STRINGS (f"...")
Curso: Python Nivel Básico - LASIN
==============================================================================

¿QUÉ SON LOS F-STRINGS Y POR QUÉ USARLOS?
- Introducidos en Python 3.6, los f-strings (Formatted String Literals) son la forma
  oficial, moderna y más rápida de formatear cadenas de texto en Python.
- Sintaxis: Anteponer la letra 'f' o 'F' antes de las comillas: f"Texto {variable}"
- Dentro de las llaves { } se pueden colocar variables, expresiones matemáticas
  e incluso llamadas a funciones.

ESPECIFICADORES DE FORMATO DESTACADOS:
1. :.2f    -> Formatea un número flotante a exactamente 2 decimales (redondeando).
2. :,.2f   -> Aplica comas ',' como separadores de miles Y 2 decimales.
3. :<ANCHO -> Alinea el texto a la IZQUIERDA en una columna de ancho fijo.
4. :>ANCHO -> Alinea el texto a la DERECHA en una columna de ancho fijo.
5. :^ANCHO -> CENTRA el texto en una columna de ancho fijo.
==============================================================================
"""

print("=== FORMATEO AVANZADO DE REPORTES CON F-STRINGS ===\n")

empresa = "Comercial Los Andes"
monto_usd = 12500.758
tasa_cambio = 11.06
descuento_porcentaje = 5.0  # 5%

# Cálculos intermedios
monto_bob = monto_usd * tasa_cambio
monto_descuento_bob = monto_bob * (descuento_porcentaje / 100)
monto_final_bob = monto_bob - monto_descuento_bob


# ==============================================================================
# 1. COMPARATIVA DE FORMAS DE CONSTRUIR SALIDAS
# ==============================================================================
print("--- 1. COMPARACIÓN DE TÉCNICAS DE IMPRESIÓN ---")

# Forma A: Concatenación manual (+) -> Verbosa, tediosa y exige str() explícito
print("Forma A (Concatenación con '+'):")
print("Empresa: " + empresa + " | Monto USD: $" + str(round(monto_usd, 2)))

# Forma B: f-strings f"..." -> Limpia, legibilidad máxima y sintaxis moderna
print("\nForma B (f-strings f'...'):")
print(f"Empresa: {empresa} | Monto USD: ${monto_usd:.2f} USD")


# ==============================================================================
# 2. ESPECIFICADORES DE FORMATO DE NÚMEROS (DECIMALES Y MILES)
# ==============================================================================
print("\n--- 2. ESPECIFICADORES DE FORMATO DECIMAL Y SEPARADORES DE MILES ---")

# :.2f redondea a 2 decimales
# :,.2f añade comas para miles y redondea a 2 decimales

print(f"• Monto bruto sin formato (raw float): Bs. {monto_bob}")
print(f"• Monto a 2 decimales (:.2f):         Bs. {monto_bob:.2f}")
print(f"• Monto con miles y decimales (:,.2f): Bs. {monto_bob:,.2f}")
print(f"• Descuento aplicado ({descuento_porcentaje}%):  Bs. {monto_descuento_bob:,.2f}")
print(f"• Monto Neto a Pagar:             Bs. {monto_final_bob:,.2f}")


# ==============================================================================
# 3. ALINEACIÓN Y ANCHO DE COLUMNAS EN F-STRINGS (REPORTES DE TABLA)
# ==============================================================================
print("\n--- 3. REPORTE EN FORMATO DE TABLA CON ALINEACIÓN (<, >) ---")
# :<30 indica que la columna ocupa 30 caracteres alineada a la IZQUIERDA.
# :>18 indica que la columna ocupa 18 caracteres alineada a la DERECHA.

print(f"{'CONCEPTO / INDICADOR':<30} | {'VALOR REGISTRADO':>18}")
print("-" * 52)
print(f"{'Empresa Razón Social':<30} | {empresa:>18}")
print(f"{'Monto Transacción (USD)':<30} | ${monto_usd:>17,.2f}")
print(f"{'Tipo de Cambio Aplicado':<30} | {tasa_cambio:>18.2f}")
print(f"{'Monto Equivalente (BOB)':<30} | Bs. {monto_bob:>14,.2f}")
print(f"{'Monto Final con Descuento':<30} | Bs. {monto_final_bob:>14,.2f}")
print("-" * 52)

# Expresiones directas evaluadas dentro de las llaves {} del f-string
print(f"Nota: Si la tasa subiera a 12.00 BOB, el valor sería Bs. {monto_usd * 12:,.2f}")
