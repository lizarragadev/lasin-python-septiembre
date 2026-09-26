"""
==============================================================================
MÓDULO 1 — LECCIÓN 2: VARIABLES Y TIPOS DE DATOS PRIMITIVOS
Curso: Python Nivel Básico - LASIN
==============================================================================

¿QUÉ ES UNA VARIABLE?
- Una variable es un contenedor o espacio nombrado en la memoria RAM de la
  computadora donde almacenamos un dato para reutilizarlo o modificarlo más adelante.
- En Python NO es necesario declarar el tipo de variable previamente (Tipado Dinámico).
  Python deduce el tipo de dato automáticamente según el valor que le asignemos.

¿QUÉ ES UNA CONSTANTE POR CONVENCIÓN?
- En Python no existe una palabra clave para bloquear una variable (como 'const' o 'final').
- Por convención estándar (PEP 8), si una variable se escribe totalmente en MAYÚSCULAS
  (ej. TASA_CAMBIO_USD_BOB), le indicamos a otros programadores que su valor NO debe cambiarse.

TIPOS DE DATOS PRIMITIVOS EN PYTHON:
1. int   (Enteros): Números sin decimales (ej. 10, -5, 1000).
2. float (Flotantes/Decimale): Números con punto decimal (ej. 3.1416, 11.06).
3. str   (Strings/Texto): Cadenas de caracteres encerradas entre comillas simple ' ' o comillas dobles " ".
4. bool  (Booleano): Representa estados lógicos de verdad: True (Verdadero) o False (Falso).
5. None  (NoneType): Representa la ausencia explícita de un valor (valor nulo o no asignado).
==============================================================================
"""

# ==============================================================================
# 1. CONSTANTES POR CONVENCIÓN (VALORES DE CONFIGURACIÓN DEL SISTEMA)
# ==============================================================================
# Escribimos los nombres en MAYÚSCULAS para señalar que son parámetros fijos

INSTITUCION = "LASIN"               # str: Nombre de la institución del curso
TASA_CAMBIO_USD_BOB = 11.06         # float: Tipo de cambio oficial de referencia Dólar a Bolivianos
IMPUESTO_IVA = 0.13                 # float: 13% de Impuesto al Valor Agregado en Bolivia


# ==============================================================================
# 2. DECLARACIÓN DE VARIABLES CON EL ESTÁNDAR 'snake_case'
# ==============================================================================
# En Python, el estándar oficial para nombrar variables es usar letras minúsculas
# separadas por guiones bajos (_) -> Ejemplo: 'monto_usd' en lugar de 'montoUSD'.

id_transaccion = 10015              # int: Identificador único del registro
empresa_cliente = "Comercial Alfa"  # str: Nombre del cliente o razón social
monto_usd = 4500.50                 # float: Monto facturado en dólares
ciudad = "La Paz"                   # str: Ciudad de emisión de la transacción
es_transaccion_valida = True        # bool: Flag que indica si la transacción superó las validaciones
observacion_error = None            # NoneType: Inicialmente no hay errores (está nulo/vacío)


# ==============================================================================
# 3. VERIFICACIÓN DEL TIPO DE DATO MEDIANTE LA FUNCIÓN type()
# ==============================================================================
# type() es una función nativa que nos retorna la clase/tipo del valor que contiene una variable.
# Es fundamental para hacer debugging cuando recibimos un dato y no sabemos si es texto o número.

print("=== INSPECCIÓN DE TIPOS DE DATOS CON type() ===\n")

print(f"• Variable 'id_transaccion' (Valor: {id_transaccion}) -> Tipo:", type(id_transaccion))
print(f"• Variable 'empresa_cliente' (Valor: '{empresa_cliente}') -> Tipo:", type(empresa_cliente))
print(f"• Variable 'monto_usd' (Valor: {monto_usd}) -> Tipo:", type(monto_usd))
print(f"• Variable 'es_transaccion_valida' (Valor: {es_transaccion_valida}) -> Tipo:", type(es_transaccion_valida))
print(f"• Variable 'observacion_error' (Valor: {observacion_error}) -> Tipo:", type(observacion_error))
print(f"• Constante 'TASA_CAMBIO_USD_BOB' (Valor: {TASA_CAMBIO_USD_BOB}) -> Tipo:", type(TASA_CAMBIO_USD_BOB))


# ==============================================================================
# 4. OPERACIONES BÁSICAS Y DESPLIEGUE DEL REGISTRO
# ==============================================================================
# Podemos realizar operaciones matemáticas con variables numéricas
monto_bob = monto_usd * TASA_CAMBIO_USD_BOB

print("\n--------------------------------------------------")
print("        FICHA RESUMEN DEL REGISTRO PROCESADO      ")
print("--------------------------------------------------")
print("• ID de Registro:         ", id_transaccion)
print("• Empresa Cliente:         ", empresa_cliente)
print("• Sede / Ciudad:           ", ciudad)
print("• Monto en Dólares:        $", monto_usd, "USD")
print("• Monto en Bolivianos:     Bs.", monto_bob, "BOB")
print("• Entidad Emisora:         ", INSTITUCION)
print("• ¿Transacción Válida?:   ", es_transaccion_valida)
# Evaluamos si observacion_error es distinto de None usando 'is not None'
print("• ¿Tiene Observaciones?:   ", observacion_error is not None)
print("--------------------------------------------------")
