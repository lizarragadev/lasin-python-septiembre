"""
==============================================================================
MÓDULO 1 — LECCIÓN 5: LIMPIEZA Y PARSEO DE CADENAS DE TEXTO (STRINGS)
Curso: Python Nivel Básico - LASIN
==============================================================================

INMUTABILIDAD DE LOS STRINGS EN PYTHON:
- En Python, los strings son INMUTABLES. Esto significa que ningún método de cadena
  modifica el string original en su lugar. Todos los métodos devuelven una NUEVA
  cadena con las modificaciones aplicadas.

MÉTODOS FUNDAMENTALES DE LIMPIEZA Y PARSEO:
1. .strip(): Elimina espacios en blanco invisibles al inicio y al final de la cadena.
2. .upper() / .lower() / .title(): Cambia la capitalización de las letras.
3. .replace(buscar, reemplazar): Sustituye una subcadena por otra dentro del texto.
4. .split(separador): Divide una cadena en una Lista de subcadenas según un separador (ej. ',').
5. len(cadena): Función nativa que retorna la cantidad total de caracteres.
6. Indexación [i] y Slicing [inicio:fin]: Extrae caracteres o subsecciones del texto.
==============================================================================
"""

print("=== LIMPIEZA Y PARSEO DE DATOS TEXTUALES (STRINGS) ===\n")

# Cadenas de prueba típicas con imperfecciones de entrada
nombre_usuario_sucio = "   gustavo lizarraga  "
observacion_raw = "El cliente solicita factura sin impuestos"
registro_csv_raw = "TX-90412,Comercial Los Andes SRL, 4500.50 ,La Paz,PENDIENTE"

print("--- 1. MOSTRAR DATOS CRUDOS RECIBIDOS ---")
print(f"• Nombre sucio ingresado: '{nombre_usuario_sucio}'")
print(f"• Fila CSV sin procesar:  '{registro_csv_raw}'")


# ==============================================================================
# 2. NORMALIZACIÓN DE TEXTO Y LIMPIEZA (.strip, .title, .upper)
# ==============================================================================
# .strip() elimina espacios sobrantes ("   hola  " -> "hola")
# .title() capitaliza cada palabra ("gustavo lizarraga" -> "Gustavo Lizarraga")
# .upper() convierte a MAYÚSCULAS ("La Paz" -> "LA PAZ")

nombre_limpio = nombre_usuario_sucio.strip().title()

print("\n--- 2. NORMALIZACIÓN DE TEXTO Y LIMPIEZA ---")
print(f"• Nombre limpio (.strip() + .title()): '{nombre_limpio}'")
print(f"• Nombre en MAYÚSCULAS (.upper()):     '{nombre_limpio.upper()}'")


# ==============================================================================
# 3. REEMPLAZO DE CARACTERES (.replace)
# ==============================================================================
# .replace(cadena_vieja, cadena_nueva) busca todas las ocurrencias y las sustituye

observacion_modificada = observacion_raw.replace("sin impuestos", "con IVA incluido")

print("\n--- 3. REEMPLAZO DE TEXTO CON .replace() ---")
print(f"• Observación original:   '{observacion_raw}'")
print(f"• Observación modificada: '{observacion_modificada}'")


# ==============================================================================
# 4. PARSEO DE FORMATO CSV CON .split(',')
# ==============================================================================
# .split(',') toma la cadena y la corta por cada coma encontrada, devolviendo una Lista.
# Es la base para procesar archivos de texto o datasets planos en Python.

columnas = registro_csv_raw.split(",")

# Extraemos cada elemento usando su posición de índice (0-indexado) y limpiamos espacios
id_tx = columnas[0].strip()
empresa = columnas[1].strip().upper()
monto_str = columnas[2].strip()
ciudad = columnas[3].strip()
estado = columnas[4].strip()

print("\n--- 4. RESULTADOS DEL PARSEO CON .split(',') ---")
print(f"  • Columna [0] - ID Transacción: {id_tx}")
print(f"  • Columna [1] - Empresa:        {empresa}")
print(f"  • Columna [2] - Monto en Texto: Bs. {monto_str}")
print(f"  • Columna [3] - Ciudad Sede:    {ciudad}")
print(f"  • Columna [4] - Estado Proceso: {estado}")


# ==============================================================================
# 5. LONGITUD, INDEXACIÓN Y SLICING DE STRINGS
# ==============================================================================
# Indexación: En Python las posiciones empiezan en 0.
# Índices negativos: [-1] es el último carácter, [-2] el penúltimo.
# Slicing [inicio:fin]: Extrae una subcadena desde 'inicio' hasta 'fin - 1'.

print("\n--- 5. LONGITUD, INDEXACIÓN Y EXTRACCIÓN (SLICING) ---")

print(f"• Cantidad total de caracteres con len(): {len(registro_csv_raw)} caracteres")

# Extraemos el prefijo del ID (Ejemplo: "TX-90412" -> subcadena "TX")
prefijo_codigo = id_tx[0:2]             # Toma del índice 0 hasta el 1 (2 es exclusivo)
codigo_numerico = id_tx[3:]              # Omite el inicio, toma desde el índice 3 hasta el final
ultimo_caracter = id_tx[-1]              # [-1] accede al último carácter sin saber la longitud

print(f"• Prefijo del Código [0:2]:      '{prefijo_codigo}'")
print(f"• Secuencia Numérica [3:]:       '{codigo_numerico}'")
print(f"• Último Carácter con [-1]:       '{ultimo_caracter}'")
