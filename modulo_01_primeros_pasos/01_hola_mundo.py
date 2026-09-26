"""
==============================================================================
MÓDULO 1 — LECCIÓN 1: HOLA MUNDO Y ESTRUCTURA BÁSICA EN PYTHON
Curso: Python Nivel Básico - LASIN
==============================================================================

¿QUÉ ES PYTHON Y CÓMO FUNCIONA?
- Python es un lenguaje de programación interpretado, lo que significa que un
  programa llamado 'Intérprete' lee nuestro archivo de código (.py) línea por
  línea y lo traduce en tiempo real a instrucciones que la computadora entiende.
- Es un lenguaje limpio, legible y muy utilizado en Análisis de Datos, IA,
  Desarrollo Web y Automatización.

CONCEPTOS QUE APRENDERÁS EN ESTE ARCHIVO:
1. Comentarios de una línea (#) y comentarios multilínea (tres comillas)
2. La función nativa print() para desplegar información en la pantalla (consola)
3. Caracteres de escape especiales como el salto de línea (\\n) y la sangría (\\t)
==============================================================================
"""

# Importamos librerías nativas del sistema para obtener información del entorno
import sys                 # El módulo 'sys' da acceso a variables y funciones del intérprete
from datetime import datetime  # El módulo 'datetime' permite trabajar con fechas y horas reales

# ==============================================================================
# 1. COMENTARIOS EN PYTHON: ¿PARA QUÉ SIRVEN Y POR QUÉ USARLOS?
# ==============================================================================
# Un comentario de una línea comienza con el símbolo numeral (#).
# Todo lo que escribas a la derecha de '#' es ignorado por Python durante la ejecución.
# ¿Para qué sirve?: Para explicar qué hace una línea difícil, dar notas a otros
# programadores o desactivar temporalmente una línea de código sin borrarla.

"""
Las comillas triples permiten escribir comentarios que ocupan varias líneas.
Aunque técnicamente Python las interpreta como cadenas de texto no asignadas,
en la práctica se utilizan como 'docstrings' para describir el propósito completo
de un archivo script o de una función.
"""

# ==============================================================================
# 2. LA FUNCIÓN print(): SALIDA DE DATOS POR CONSOLA
# ==============================================================================
# print() es una función nativa (built-in) de Python. Su trabajo es tomar el texto,
# número o variable que le pases entre paréntesis y mostrarlo en la terminal (stdout).

print("==================================================")
print("   SISTEMA DE PROCESAMIENTO DE DATOS - DATAFLOW   ")
print("               CURSO PYTHON LASIN                 ")
print("==================================================\n")

# Imprimimos información útil del entorno de ejecución
print("✓ Estado del sistema: Inicializado y listo para procesar datos.")

# sys.version.split()[0] extrae únicamente el número de versión (ej. '3.11.4')
print("✓ Versión del intérprete de Python:", sys.version.split()[0])

# datetime.now() obtiene la fecha y hora exacta del sistema en este momento
print("✓ Fecha y hora de ejecución:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# ==============================================================================
# 3. CARACTERES DE ESCAPE ESPECIALES EN TEXTO
# ==============================================================================
# Dentro de un texto (String), la barra invertida '\\' activa caracteres especiales:
# - '\\n' (Line Feed / Salto de línea): Equivale a presionar ENTER en el texto.
# - '\\t' (Tabulación / Sangría): Inserta un espacio de tabulador de 4 u 8 espacios.

print("\n--- INFORMACIÓN GENERAL DEL CURSO ---")
print("\t• Módulo activo:   Módulo 1 — Primeros Pasos con Python")
print("\t• Enfoque principal: Procesamiento de Datos, Automatización y APIs")
print("\t• Metodología:      70% Práctica / 30% Teoría (Hands-on)")
print("\n--------------------------------------------------")
print("¡Felicidades! Has ejecutado exitosamente tu primer archivo en Python.")
