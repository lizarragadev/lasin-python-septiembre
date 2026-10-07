# Ejercicios Módulo 1 — Tema 1: Variables, Tipos de Datos y Conversiones

En esta sección encontrarás ejercicios prácticos para afianzar el uso de variables, identificación de tipos de datos (`type()`), constantes por convención (`MAYÚSCULAS`) y conversiones explícitas (`int()`, `float()`, `str()`).

---

## 📝 Ejercicio 1: Ficha de Registro de Producto de Inventario

### Descripción del Problema
Una empresa comercializadora necesita registrar los datos de un nuevo producto en su inventario. Debes crear un script que defina o solicite los datos de un producto y muestre una ficha descriptiva en pantalla, verificando los tipos de datos de cada variable.

### Requerimientos
1. Define las siguientes variables con sus tipos correspondientes:
   - `codigo_sku` (Texto / `str`): Identificador del producto (ej. `"SKU-9045"`).
   - `nombre_producto` (Texto / `str`): Razón o nombre del producto (ej. `"Laptop HP Pavilion 15"`).
   - `precio_usd` (Número Decimal / `float`): Precio original en Dólares (ej. `750.50`).
   - `stock_disponible` (Número Entero / `int`): Unidades en almacén (ej. `25`).
   - `tiene_descuento` (Booleano / `bool`): Indica si el producto aplica para descuento (`True` o `False`).
   - `observacion` (Sin valor / `NoneType`): Inicialmente establecido en `None`.
2. Define una constante `TASA_CAMBIO_BOB = 11.06`.
3. Calcula el precio equivalente en Bolivianos (`precio_bob = precio_usd * TASA_CAMBIO_BOB`).
4. Muestra en pantalla el tipo de dato de cada variable usando `type()`.

### Ejemplo de Salida Esperada en Consola
```text
=== FICHA TÉCNICA DE PRODUCTO DE INVENTARIO ===
• Código SKU:           SKU-9045 (Tipo: <class 'str'>)
• Producto:             Laptop HP Pavilion 15 (Tipo: <class 'str'>)
• Precio Dólares:       $ 750.50 USD (Tipo: <class 'float'>)
• Precio Bolivianos:    Bs. 8300.53 BOB (Tipo: <class 'float'>)
• Stock Disponible:     25 unidades (Tipo: <class 'int'>)
• ¿Aplica Descuento?:   True (Tipo: <class 'bool'>)
• Observación Inicial:  None (Tipo: <class 'NoneType'>)
===============================================
```

---

## 📝 Ejercicio 2: Conversor de Temperatura Científico

### Descripción del Problema
Un laboratorio meteorológico en La Paz registra temperaturas en grados Celsius (°C). Necesitas crear un programa que capture o defina una temperatura en Celsius, la convierta explícitamente a grados Fahrenheit (°F) y Kelvin (K), y muestre el reporte en pantalla.

### Fórmulas Matemáticas
- **Fahrenheit (°F):** $F = (C \times \frac{9}{5}) + 32$
- **Kelvin (K):** $K = C + 273.15$

### Ejemplo de Entrada y Salida
- **Entrada simulada:** `temperatura_celsius = 21.5`
- **Salida esperada:**
```text
=== REPORTE DE CONVERSIÓN DE TEMPERATURA ===
• Temperatura Celsius ingresada: 21.5 °C
• Conversión a Fahrenheit:       70.7 °F
• Conversión a Kelvin:           294.65 K
============================================
```
