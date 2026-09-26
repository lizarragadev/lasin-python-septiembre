"""
==============================================================================
MÓDULO 1 — LECCIÓN 8: RETO — GENERADOR DE RESUMEN EJECUTIVO Y FINANCIERO
Curso: Python Nivel Básico - LASIN
==============================================================================

RETO INTEGRADOR DEL MÓDULO 1:
- El estudiante debe aplicar todos los conceptos aprendidos en el Módulo 1:
  Variables, constantes por convención, captura con input(), conversión de tipos,
  operaciones de strings (.strip(), .upper(), .title()), cálculos financieros
  (conversión de moneda, impuesto IVA 13%, productividad laboral) y formateo
  multilínea avanzado con f-strings.
==============================================================================
"""

print("==================================================")
print("    RETO: GENERADOR DE RESUMEN EJECUTIVO EMPRESARIAL")
print("==================================================\n")

# Captura de datos con fallbacks predeterminados para facilitar la prueba
nombre_empresa_in = input("Nombre de la empresa [Enter para 'Comercial Los Andes SRL']: ").strip()
rubro_in = input("Rubro o sector comercial [Enter para 'Distribucion y Comercio']: ").strip()
ciudad_in = input("Ciudad sede [Enter para 'La Paz']: ").strip()
empleados_in = input("Número de empleados [Enter para 15]: ").strip()
ingreso_usd_in = input("Ingreso estimado anual en USD [Enter para 150000.00]: ").strip()

# Asignación y limpieza de datos
nombre_empresa = nombre_empresa_in if nombre_empresa_in else "Comercial Los Andes SRL"
rubro = rubro_in if rubro_in else "Distribucion y Comercio"
ciudad = ciudad_in if ciudad_in else "La Paz"
empleados = int(empleados_in) if empleados_in.isdigit() else 15
ingreso_anual_usd = float(ingreso_usd_in) if ingreso_usd_in.replace('.', '', 1).isdigit() else 150000.00

# ==============================================================================
# 1. CONSTANTES Y CÁLCULOS FINANCIEROS Y FISCALES
# ==============================================================================
TASA_CAMBIO_USD_BOB = 11.06     # Constante fiduciaria
IMPUESTO_IVA = 0.13             # 13% de IVA

# Conversión de divisa USD -> BOB
ingreso_anual_bob = ingreso_anual_usd * TASA_CAMBIO_USD_BOB

# Proyección fiscal de IVA
impuesto_iva_estimado = ingreso_anual_bob * IMPUESTO_IVA

# Ingreso neto libre de IVA
ingreso_neto_bob = ingreso_anual_bob - impuesto_iva_estimado

# Indicador de productividad por trabajador (Ingreso / Nro Empleados)
productividad_por_empleado = ingreso_anual_bob / empleados if empleados > 0 else 0.0


# ==============================================================================
# 2. GENERACIÓN DEL DASHBOARD DE SALIDA CON F-STRINGS
# ==============================================================================
# Aplicamos .upper() para resaltar la Razón Social y .title() para la Ciudad y Rubro
resumen_ejecutivo = f"""
+-----------------------------------------------------------------+
|               DASHBOARD ORGANIZACIONAL - LASIN                  |
+-----------------------------------------------------------------+
 Razón Social:            {nombre_empresa.upper()}
 Sector / Rubro:          {rubro.title()}
 Sede Operativa:          {ciudad.title()}
 Personal Contratado:     {empleados} colaboradores
-------------------------------------------------------------------
 PROYECCIÓN FINANCIERA CONSOLIDADA (USD / BOB)
 • Ingreso Bruto (USD):   $ {ingreso_anual_usd:>15,.2f} USD
 • Ingreso Bruto (BOB):   Bs. {ingreso_anual_bob:>14,.2f}
 • IVA Estimado (13%):    Bs. {impuesto_iva_estimado:>14,.2f}
 • Ingreso Neto Libre:    Bs. {ingreso_neto_bob:>14,.2f}
-------------------------------------------------------------------
 INDICADORES DE PRODUCTIVIDAD
 • Promedio Venta / Emp:  Bs. {productividad_por_empleado:>14,.2f} por trabajador
+-----------------------------------------------------------------+
"""

print(resumen_ejecutivo)
