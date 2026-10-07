# Ejercicios Módulo 1 — Tema 3: Manipulación de Strings y f-strings

En esta sección practicarás métodos de limpieza de texto (`.strip()`, `.upper()`, `.title()`, `.replace()`, `.split()`), medición de caracteres (`len()`), slicing `[inicio:fin]` y el formateo de tablas profesionales con `f-strings`.

---

## 📝 Ejercicio 1: Limpiador y Generador de Código de Usuario

### Descripción del Problema
Un sistema de registro recibe nombres de usuarios con espacios accidentales al inicio/final y con formato inconsistente. Debes crear un script que limpie el nombre del usuario y genere automáticamente un **Código de Usuario Único** combinado con su año de nacimiento y ciudad.

### Pasos a Realizar
1. Recibe un nombre sucio (ej. `"   gustavo adolfo lizarraga  "`), una ciudad (ej. `"  la paz "`) y un año de nacimiento (ej. `1992`).
2. Limpia los espacios con `.strip()`.
3. Convierte el nombre completo a formato título (`.title()`).
4. Extrae las 3 primeras letras del primer nombre en mayúsculas usando slicing `[0:3]`.
5. Reemplaza todos los espacios del nombre limpio por guiones bajos `_` usando `.replace()`.
6. Genera el código único combinando: `PREFIJO_AÑO_CIUDAD` (ej. `"GUS-1992-LAPAZ"`).

### Ejemplo de Entrada y Salida
- **Entrada:** `nombre = "  gustavo adolfo lizarraga "`, `ciudad = " la paz "`, `anio = 1992`
- **Salida esperada:**
```text
=== GENERADOR DE IDENTIDAD DE USUARIO ===
• Nombre Original Sucio:  '  gustavo adolfo lizarraga '
• Nombre Limpio Formateado: 'Gustavo Adolfo Lizarraga'
• Nombre de Usuario Sistema: 'Gustavo_Adolfo_Lizarraga'
• Código Único Generado:    GUS-1992-LAPAZ
• Longitud Total Nombre:    24 caracteres
==========================================
```

---

## 📝 Ejercicio 2: Generador de Reporte Financiero Tabular Alineado

### Descripción del Problema
Una empresa de auditoría en Bolivia necesita imprimir un resumen ejecutivo de ingresos de 3 sucursales (La Paz, Santa Cruz, Cochabamba) perfectamente alineado en columnas usando especificadores de ancho de f-strings (`:<20`, `:>15,.2f`).

### Ejemplo de Datos de Entrada
- **Sucursal 1:** `"La Paz"` -> Ingreso: `15400.50 Bs.`
- **Sucursal 2:** `"Santa Cruz"` -> Ingreso: `28900.00 Bs.`
- **Sucursal 3:** `"Cochabamba"` -> Ingreso: `8350.75 Bs.`

### Salida Esperada
```text
====================================================
           REPORTE CONSOLIDADO DE SUCURSALES        
====================================================
SUCURSAL Sede        | INGRESO REGISTRADO | % TOTAL 
----------------------------------------------------
La Paz               | Bs.    15,400.50 |    29.25%
Santa Cruz           | Bs.    28,900.00 |    54.89%
Cochabamba           | Bs.     8,350.75 |    15.86%
----------------------------------------------------
TOTAL CONSOLIDADO    | Bs.    52,651.25 |   100.00%
====================================================
```
