# Ejercicios Módulo 1 — Tema 2: Operadores Aritméticos y Módulo Math

En esta sección practicarás la precedencia de operadores, cálculos de salarios con descuentos de ley (impuestos), división entera `//`, módulo `%` y funciones avanzadas del módulo `math` (`math.ceil`, `math.floor`, `math.sqrt`).

---

## 📝 Ejercicio 1: Calculadora de Salario Neto de Empleados

### Descripción del Problema
Una empresa en Bolivia necesita calcular la planilla de sueldo de un empleado a partir de su salario bruto mensual. Debes calcular las deducciones de ley obligatorias:
1. **Aporte a Jubilación / AFP (12.71%):** Calculado sobre el salario bruto.
2. **Retención de Impuesto RC-IVA Estimado (13%):** Aplicado sobre el saldo líquido imponible después de la AFP.
3. **Bono de Transporte Fijo:** Se le suma `250.00 Bs.` al salario final.

### Fórmulas
- `descuento_afp = salario_bruto * 0.1271`
- `monto_imponible = salario_bruto - descuento_afp`
- `descuento_iva = monto_imponible * 0.13`
- `salario_neto = salario_bruto - descuento_afp - descuento_iva + BONO_TRANSPORTE`

### Ejemplo de Entrada y Salida
- **Salario Bruto Ingresado:** `8500.00 Bs.`
- **Salario Neto Calculado Esperado:**
```text
=== LIQUIDACIÓN DE SUELDO Y PLANILLA ===
• Salario Bruto Ingresado:   Bs. 8,500.00
• Deducción AFP (12.71%):     Bs. 1,080.35
• Deducción RC-IVA (13%):     Bs.  964.55
• Subtotal Deducciones:       Bs. 2,044.90
• Bono de Transporte (+):     Bs.   250.00
-----------------------------------------
• SALARIO NETO A COBRAR:      Bs. 6,705.10
=========================================
```

---

## 📝 Ejercicio 2: Planificador de Lotes y Cajas de Envío (Librería Math)

### Descripción del Problema
Una fábrica de conservas necesita empacar sus productos en cajas de cartón. Cada caja tiene una capacidad máxima fija de `12 unidades`. El departamento de logística necesita calcular:
1. Cuántas cajas se llenan por completo (`//`).
2. Cuántas unidades quedan sueltas fuera de caja (`%`).
3. Cuántas cajas totales de empaque se deben comprar al proveedor (`math.ceil()`).

### Ejemplo de Entrada y Salida
- **Unidades producidas:** `125 unidades`
- **Salida esperada:**
```text
=== PLANIFICACIÓN LOGÍSTICA DE EMPAQUE ===
• Total de Unidades Producidas:  125 unidades
• Cajas Llenas Completas (//):   10 cajas (120 unidades empacadas)
• Unidades Sobrantes (modulo %): 5 unidades sueltas
• Cajas Totales a Comprar (ceil): 11 cajas requeridas
==========================================
```
