"""
==============================================================================
SOLUCIÓN — MÓDULO 1 — TEMA 3 — EJERCICIO 1: LIMPIADOR Y CÓDIGO DE USUARIO
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Usamos .strip() para eliminar espacios al inicio y final.
2. Usamos .title() para capitalizar el nombre.
3. Usamos slicing [0:3] sobre la primera palabra para obtener el prefijo de 3 letras.
4. Usamos .replace(" ", "_") para crear un nombre de usuario compatible con sistemas Web.
5. Usamos f-strings para ensamblar el código único final.
"""

print("=== GENERADOR DE IDENTIDAD DE USUARIO ===\n")

nombre_raw = "  gustavo adolfo lizarraga "
ciudad_raw = " la paz "
anio_nacimiento = 1992

# 1. Limpieza de cadenas
nombre_limpio = nombre_raw.strip().title()
ciudad_limpia = ciudad_raw.strip().replace(" ", "").upper()

# 2. Nombre para sistema (con guiones bajos)
nombre_sistema = nombre_limpio.replace(" ", "_")

# 3. Extracción de prefijo de 3 letras con slicing [0:3]
primer_nombre = nombre_limpio.split()[0]
prefijo = primer_nombre[0:3].upper()

# 4. Ensamble de código único
codigo_unico = f"{prefijo}-{anio_nacimiento}-{ciudad_limpia}"

# Despliegue de resultados
print(f"• Nombre Original Sucio:    '{nombre_raw}'")
print(f"• Nombre Limpio Formateado: '{nombre_limpio}'")
print(f"• Nombre de Usuario Sistema:'{nombre_sistema}'")
print(f"• Código Único Generado:    {codigo_unico}")
print(f"• Longitud Total Nombre:    {len(nombre_limpio)} caracteres")
print("==========================================")
