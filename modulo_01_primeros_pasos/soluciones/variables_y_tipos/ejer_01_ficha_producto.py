"""
==============================================================================
SOLUCIÓN — MÓDULO 1 — TEMA 1 — EJERCICIO 1: FICHA DE PRODUCTO
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Definimos las variables respetando la convención 'snake_case'.
2. La constante TASA_CAMBIO_BOB se escribe en MAYÚSCULAS según el estándar PEP 8.
3. Usamos la función nativa type() para inspeccionar el tipo de dato de cada variable.
4. Calculamos la conversión multiplicando 'precio_usd * TASA_CAMBIO_BOB'.
"""

# 1. Definición de constante de configuración por convención (MAYÚSCULAS)
TASA_CAMBIO_BOB = 11.06  # float: Tipo de cambio oficial de referencia

# 2. Definición de variables primarias
codigo_sku = "SKU-9045"                 # str: Cadena de texto
nombre_producto = "Laptop HP Pavilion 15" # str: Cadena de texto
precio_usd = 750.50                      # float: Número decimal
stock_disponible = 25                    # int: Número entero
tiene_descuento = True                   # bool: Valor booleano
observacion = None                       # NoneType: Ausencia de valor inicial

# 3. Operación aritmética de conversión
precio_bob = precio_usd * TASA_CAMBIO_BOB

# 4. Despliegue formateado del reporte con inspección de tipos
print("=== FICHA TÉCNICA DE PRODUCTO DE INVENTARIO ===")
print(f"• Código SKU:           {codigo_sku} (Tipo: {type(codigo_sku)})")
print(f"• Producto:             {nombre_producto} (Tipo: {type(nombre_producto)})")
print(f"• Precio Dólares:       $ {precio_usd:.2f} USD (Tipo: {type(precio_usd)})")
print(f"• Precio Bolivianos:    Bs. {precio_bob:.2f} BOB (Tipo: {type(precio_bob)})")
print(f"• Stock Disponible:     {stock_disponible} unidades (Tipo: {type(stock_disponible)})")
print(f"• ¿Aplica Descuento?:   {tiene_descuento} (Tipo: {type(tiene_descuento)})")
print(f"• Observación Inicial:  {observacion} (Tipo: {type(observacion)})")
print("===============================================")
