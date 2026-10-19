# 📦 Ejercicio Integrador: Sistema de Auditoría y Procesamiento Logístico (LogiFlow)

Bienvenido al ejercicio práctico integrador del **Curso de Python — Nivel Básico (LASIN)**. 

Este ejercicio ha sido concebido para desafiarte y permitirte integrar los conceptos clave aprendidos a lo largo de las 20 horas académicas del curso en un único proyecto realista y profesional.

---

## 🏢 Contexto del Problema

Trabajas como desarrollador Python para **LogiFlow**, un operador logístico nacional. Diariamente, las agencias envían registros de envíos en un archivo CSV que contiene inconsistencias: espacios innecesarios en nombres de clientes, registros duplicados, valores atípicos (outliers) y datos con formatos erróneos.

Tu misión es construir una aplicación modular por consola en Python que:
1. **Lea y limpie** el archivo de datos sin detenerse ante filas corruptas.
2. **Audite y clasifique** cada envío mediante Programación Orientada a Objetos (`dataclasses` y `Enum`).
3. **Enriquezca** los costos convirtiendo los valores a moneda local consultando una API REST en línea (con mecanismo de contingencia offline).
4. **Almacene** únicamente los envíos válidos y aprobados en una base de datos relacional **SQLite**.
5. **Genere reportes ejecutivos** con visualización espacial en formato **GeoJSON** y tablas alineadas con `f-strings`.
6. **Proporcione un menú interactivo** por consola gobernado por `match-case`.

---

## 🎯 Mapa de Conocimientos Aplicados

| Módulo del Curso | Conceptos que pondrás en práctica |
| :--- | :--- |
| **Módulo 1: Primeros Pasos** | Tipado con type hints, casting seguro, operadores aritméticos y alineación avanzada con `f-strings`. |
| **Módulo 2: Lógica y Flujo** | Menú interactivo continuo (`while`), control de opciones con `match-case` y reglas de validación (`if/elif/else`). |
| **Módulo 3: Colecciones y Funciones** | Eliminación de duplicados con `set`, transformaciones con comprensiones de listas/diccionarios, modularización con funciones y gestión de errores con `try-except-else-finally`. |
| **Módulo 4: Archivos y APIs** | Manejo de rutas con `pathlib`, lectura/escritura con `csv` y `json`, y consumo HTTP con `urllib.request`. |
| **Módulo 5: Temas Avanzados** | Modelado con `Enum` y `@dataclass`, encapsulamiento con `@property`, persistencia transaccional con `sqlite3` y coordenadas en estándar **GeoJSON**. |

---

## 📋 Especificación Técnica Detallada

El sistema debe implementarse en un archivo ejecutable (por ejemplo `solucion_ejercicio_integrador.py`) o de forma modular, cumpliendo los siguientes 7 requerimientos:

### 1. Modelado con POO (`dataclasses` y `Enum`)
* Define un `Enum` llamado `TipoEnvio` con tres valores:
  * `ESTANDAR`
  * `EXPRESS`
  * `REFRIGERADO`
* Define un `Enum` llamado `EstadoAuditoria` con tres valores:
  * `APROBADO`
  * `OBSERVADO`
  * `RECHAZADO`
* Define una clase `@dataclass` llamada `Envio`:
  * **Atributos:**
    * `id_envio: str`
    * `cliente: str`
    * `peso_kg: float`
    * `costo_base: float`
    * `tipo: TipoEnvio`
    * `latitud: float`
    * `longitud: float`
  * **Método `calcular_costo_final() -> float`:**
    * Si es `ESTANDAR`: retorna el `costo_base` sin recargo.
    * Si es `EXPRESS`: aplica un recargo del **20%** sobre el costo base (`costo_base * 1.20`).
    * Si es `REFRIGERADO`: aplica un recargo del **35%** por cadena de frío (`costo_base * 1.35`).
  * **Método `auditar() -> EstadoAuditoria`:**
    * Retorna `RECHAZADO` si el `peso_kg > 500.0` o si las coordenadas son geográficamente imposibles (latitud fuera del rango `[-90.0, 90.0]` o longitud fuera de `[-180.0, 180.0]`).
    * Retorna `OBSERVADO` si el `costo_base > 5000.0` (montos extraordinarios que requieren doble aprobación financiera).
    * Retorna `APROBADO` en cualquier otro caso válido.

---

### 2. Ingesta Segura de Archivos (`pathlib` y `csv`)
* La función `cargar_datos_csv(ruta_archivo: Path)` debe abrir y leer `datos_envios.csv`.
* Limpiar los nombres de clientes eliminando espacios en blanco al inicio y al final con `.strip()`.
* **Manejo defensivo de excepciones:**
  * Si un registro contiene valores numéricos inválidos o negativos (por ejemplo, `peso_kg = -10.0`), la fila debe ser descartada capturando el error (`ValueError`) y mostrando una advertencia informativa en consola, **sin detener** el procesamiento del resto del archivo.
  * Si el archivo no existe, debe atrapar `FileNotFoundError` y retornar una lista vacía.

---

### 3. Enriquecimiento con API Externa (`urllib.request`)
* Implementa la función `obtener_tipo_cambio_usd_a_bob() -> float`:
  * Debe intentar consultar un endpoint REST público de tasas de cambio (ejemplo: `https://open.er-api.com/v6/latest/USD` o similar).
  * Si la conexión tiene éxito y el status es 200, extrae la tasa de cambio para Bolivianos (`BOB`) u otra moneda local de tu elección.
  * **Fallback resiliente:** En caso de no haber conexión a internet, error de timeout o fallo DNS (`URLError`, `TimeoutError`), debe atrapar la excepción y retornar una tasa fija por defecto (por ejemplo `6.96`), asegurando que el programa continúe funcionando sin interrupciones.

---

### 4. Transformaciones y Colecciones Pythonic
* Utiliza un conjunto (`set`) para detectar y descartar registros duplicados basados en el `id_envio`.
* Utiliza una **comprensión de listas** (`list comprehension`) para filtrar únicamente la lista de envíos con estado `EstadoAuditoria.APROBADO`.
* Utiliza una **comprensión de diccionarios** (`dict comprehension`) para calcular el monto total facturado agrupado por cada `TipoEnvio`.

---

### 5. Persistencia Relacional con SQLite (`sqlite3`)
* Implementa la función `guardar_en_sqlite(envios: list[Envio], ruta_db: Path)`:
  * Abre una conexión a la base de datos `auditoria_envios.db`.
  * Crea la tabla `envios_aprobados` si no existe con las columnas:
    `id TEXT PRIMARY KEY, cliente TEXT, tipo TEXT, peso_kg REAL, costo_usd REAL, costo_bob REAL, latitud REAL, longitud REAL`.
  * Inserta los envíos aprobados utilizando consultas parametrizadas con `?` o `executemany()` para garantizar seguridad contra inyecciones SQL.

---

### 6. Exportación GeoJSON y Reporte con F-Strings
* **Exportación GeoJSON (`exportar_geojson(envios: list[Envio], ruta_salida: Path)`):**
  * Genera un archivo `.geojson` válido con estructura `FeatureCollection`.
  * Cada envío aprobado debe representarse como un `Feature` con geometría `Point` (`coordinates: [longitud, latitud]`) y propiedades con su `id`, `cliente` y `costo_final_usd`.
* **Reporte Tabular por Consola:**
  * Mostrar una tabla con bordes y columnas alineadas (`:<10`, `:<22`, `:>12`, `:>14`) usando f-strings:
    * ID del Envío
    * Cliente
    * Tipo de Envío
    * Costo Final (USD)
    * Costo Final (BOB)

---

### 7. Menú Interactivo por Consola
El programa debe iniciarse con un menú continuo controlado por un bucle `while` y la instrucción `match-case`:

```text
============================================================
           LOGIFLOW — SISTEMA DE AUDITORÍA Y CONTROL        
============================================================
[1] Ingerir y Auditar Lote de Envíos (CSV)
[2] Mostrar Reporte Tabular de Envíos Aprobados
[3] Guardar Envíos Aprobados en Base de Datos (SQLite)
[4] Exportar Coordenadas a GeoJSON (Mapa)
[5] Salir del Sistema
------------------------------------------------------------
Seleccione una opción: 
```

---

## 📥 Dataset de Prueba Provisto (`datos_envios.csv`)

El archivo `datos_envios.csv` provisto en este directorio contiene los siguientes casos:

```csv
id_envio,cliente,peso_kg,costo_base,tipo,latitud,longitud
ENV-001,  Farmacia Central  ,12.5,150.0,REFRIGERADO,-16.5000,-68.1500
ENV-002,Distribuidora Norte,45.0,320.0,ESTANDAR,-17.3895,-66.1568
ENV-003,Supermercado Fidalga,120.0,850.0,EXPRESS,-17.7833,-63.1821
ENV-004,  Farmacia Central  ,12.5,150.0,REFRIGERADO,-16.5000,-68.1500
ENV-005,Laboratorios Vita,8.0,6200.0,REFRIGERADO,-16.4955,-68.1336
ENV-006,Minera San Cristobal,750.0,2400.0,ESTANDAR,-21.1500,-66.7833
ENV-007,Tienda Electronica Sur,5.2,450.0,EXPRESS,112.5000,-68.1120
ENV-008,Importadora Los Andes,25.0,210.0,ESTANDAR,-19.0333,-65.2627
ENV-009,Textiles Andinos,-10.0,300.0,ESTANDAR,-16.5100,-68.1400
ENV-010,Clinica Copacabana,18.3,280.0,REFRIGERADO,-16.1667,-69.0833
```

### 🔍 Análisis previo esperado de los datos:
* **ENV-001:** Válido (`REFRIGERADO`), recargo +35% -> Costo final: $150 \times 1.35 = 202.50$ USD.
* **ENV-002:** Válido (`ESTANDAR`), sin recargo -> Costo final: $320.00$ USD.
* **ENV-003:** Válido (`EXPRESS`), recargo +20% -> Costo final: $850 \times 1.20 = 1020.00$ USD.
* **ENV-004:** **Duplicado** de ENV-001 -> Debe ser descartado por el `set`.
* **ENV-005:** `costo_base = 6200.0 > 5000.0` -> Estado `OBSERVADO` (no va a la BD de aprobados).
* **ENV-006:** `peso_kg = 750.0 > 500.0` -> Estado `RECHAZADO`.
* **ENV-007:** `latitud = 112.5 > 90.0` -> Coordenada fuera de rango -> Estado `RECHAZADO`.
* **ENV-008:** Válido (`ESTANDAR`), sin recargo -> Costo final: $210.00$ USD.
* **ENV-009:** `peso_kg = -10.0` -> Error de datos corruptos capturado por `try-except` (Fila descartada).
* **ENV-010:** Válido (`REFRIGERADO`), recargo +35% -> Costo final: $280 \times 1.35 = 378.00$ USD.

**Total Aprobados esperados:** 5 envíos (`ENV-001`, `ENV-002`, `ENV-003`, `ENV-008`, `ENV-010`).

---

## 🖥️ Ejemplo de Ejecución y Salida Esperada

### 1. Ingesta y Auditoría (Opción 1):
```text
>>> Procesando archivo: datos_envios.csv ...
[AVISO] Fila descartada por datos inválidos: ENV-009 (El peso no puede ser negativo: -10.0)
[AVISO] Registro duplicado omitido: ENV-004
[API] Tasa de cambio obtenida exitosamente: 1 USD = 6.96 BOB

✓ Resumen de Auditoría:
  - Filas procesadas:        10
  - Registros únicos:         8
  - Registros con error:      1
  - Envíos APROBADOS:         5
  - Envíos OBSERVADOS:        1
  - Envíos RECHAZADOS:        2
```

### 2. Reporte Tabular (Opción 2):
```text
========================================================================================
                          REPORTE DE ENVÍOS APROBADOS (LOGIFLOW)                        
========================================================================================
ID ENVÍO   CLIENTE                TIPO            PESO (KG)      COSTO (USD)     COSTO (BOB)
----------------------------------------------------------------------------------------
ENV-001    Farmacia Central       REFRIGERADO         12.50       $   202.50     Bs. 1,409.40
ENV-002    Distribuidora Norte    ESTANDAR            45.00       $   320.00     Bs. 2,227.20
ENV-003    Supermercado Fidalga   EXPRESS            120.00       $ 1,020.00     Bs. 7,099.20
ENV-008    Importadora Los Andes  ESTANDAR            25.00       $   210.00     Bs. 1,461.60
ENV-010    Clinica Copacabana     REFRIGERADO         18.30       $   378.00     Bs. 2,630.88
----------------------------------------------------------------------------------------
TOTALES:   5 Envíos Aprobados                        220.80 kg    $ 2,130.50    Bs. 14,828.28
========================================================================================
• Distribución por Tipo de Envío:
  - REFRIGERADO: $ 580.50 (2 envíos)
  - ESTANDAR:    $ 530.00 (2 envíos)
  - EXPRESS:     $ 1,020.00 (1 envío)
========================================================================================
```

### 3. Persistencia en SQLite (Opción 3):
```text
>>> Guardando en base de datos auditoria_envios.db ...
✓ Tabla 'envios_aprobados' verificada.
✓ 5 registros insertados/actualizados exitosamente en SQLite.
```

### 4. Exportación GeoJSON (Opción 4):
```text
>>> Exportando puntos de entrega a GeoJSON ...
✓ Archivo generado exitosamente en: envios_aprobados.geojson
✓ Contiene 5 características geográficas (FeatureCollection).
```

---

## 🏆 Criterios de Evaluación y Buenas Prácticas
1. **Claridad del Código:** Nombres descriptivos de variables y funciones en español o inglés técnico, respetando PEP 8.
2. **Uso de Type Hints:** Declaración de tipos en argumentos y retornos de funciones (ej. `def auditar(envio: Envio) -> EstadoAuditoria:`).
3. **Manejo Defensivo:** El programa nunca debe romperse con un traceback en pantalla ante entradas del usuario fuera de rango o errores de red.
4. **Comentarios Explicativos:** Incluye comentarios en las secciones clave explicando **por qué** utilizas cada estructura (ej. por qué un `set` para duplicados, por qué un `match-case`, por qué `executemany`).
