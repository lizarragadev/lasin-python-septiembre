"""
========================================================================================
LOGIFLOW — SISTEMA DE AUDITORÍA Y PROCESAMIENTO LOGÍSTICO
Solución Oficial del Ejercicio Práctico Integrador (LASIN - Curso Python Básico)
========================================================================================
Este script integra los conceptos fundamentales de los 5 módulos del curso:
 - Módulo 1: Tipado, f-strings formateadas, operadores y conversiones numéricas.
 - Módulo 2: Bucle interactivo while, condicionales y control con match-case.
 - Módulo 3: Conjuntos (set), comprensiones de listas/dicts, funciones y try-except-else-finally.
 - Módulo 4: Manipulación de rutas con pathlib, lectura/escritura CSV/JSON y consumo de APIs HTTP.
 - Módulo 5: Enums, @dataclass, encapsulamiento, persistencia SQLite y formato GeoJSON.
========================================================================================
"""

from __future__ import annotations
import csv
import json
import sqlite3
import urllib.request
import urllib.error
from dataclasses import dataclass
from enum import Enum
from pathlib import Path


# ======================================================================================
# 1. MODELADO DEL DOMINIO CON POO (Módulos 1 y 5: Enum y Dataclasses)
# ======================================================================================

class TipoEnvio(str, Enum):
    """
    Enum para representar los tipos de envío admitidos.
    Heredar de (str, Enum) facilita la serialización directa a JSON y texto legible.
    """
    ESTANDAR = "ESTANDAR"
    EXPRESS = "EXPRESS"
    REFRIGERADO = "REFRIGERADO"


class EstadoAuditoria(str, Enum):
    """
    Enum para tipificar el resultado de la auditoría de cada registro logístico.
    """
    APROBADO = "APROBADO"
    OBSERVADO = "OBSERVADO"
    RECHAZADO = "RECHAZADO"


@dataclass
class Envio:
    """
    Representa una orden de despacho logístico individual.
    @dataclass genera automáticamente __init__, __repr__ y métodos de comparación.
    """
    id_envio: str
    cliente: str
    peso_kg: float
    costo_base: float
    tipo: TipoEnvio
    latitud: float
    longitud: float

    def __post_init__(self) -> None:
        """
        Validación defensiva inmediata tras la inicialización del objeto.
        Garantiza que ningún objeto Envio pueda crearse con magnitudes físicas inválidas.
        """
        if self.peso_kg <= 0:
            raise ValueError(f"El peso debe ser mayor a 0 kg (recibido: {self.peso_kg})")
        if self.costo_base < 0:
            raise ValueError(f"El costo base no puede ser negativo (recibido: {self.costo_base})")

    def calcular_costo_final(self) -> float:
        """
        Calcula el costo final aplicando los recargos comerciales según el TipoEnvio.
         - ESTANDAR: sin recargo (+0%)
         - EXPRESS: recargo por prioridad comercial (+20%)
         - REFRIGERADO: recargo por mantenimiento de cadena de frío (+35%)
        """
        match self.tipo:
            case TipoEnvio.EXPRESS:
                return round(self.costo_base * 1.20, 2)
            case TipoEnvio.REFRIGERADO:
                return round(self.costo_base * 1.35, 2)
            case TipoEnvio.ESTANDAR | _:
                return round(self.costo_base, 2)

    def auditar(self) -> EstadoAuditoria:
        """
        Aplica las reglas de negocio y seguridad física de la empresa:
         1. RECHAZADO: si el peso excede la capacidad máxima por paquete (500 kg) o
            si las coordenadas geográficas son matemáticamente imposibles.
         2. OBSERVADO: si el costo supera los $5,000.00 USD (requiere revisión contable).
         3. APROBADO: envío normal apto para despacho inmediato.
        """
        # Validación de rango geográfico terrestre: lat [-90, 90], lon [-180, 180]
        coordenadas_validas = (-90.0 <= self.latitud <= 90.0) and (-180.0 <= self.longitud <= 180.0)
        
        if self.peso_kg > 500.0 or not coordenadas_validas:
            return EstadoAuditoria.RECHAZADO
        
        if self.costo_base > 5000.0:
            return EstadoAuditoria.OBSERVADO
            
        return EstadoAuditoria.APROBADO


# ======================================================================================
# 2. ENRIQUECIMIENTO EXTERNO CON API REST (Módulo 4: urllib.request y resiliencia)
# ======================================================================================

def obtener_tipo_cambio_usd_a_bob() -> float:
    """
    Consulta un servicio web REST público para obtener la tasa de cambio USD -> BOB.
    Aplica el principio de resiliencia: si no hay internet o falla el DNS,
    atrapa la excepción y retorna una tasa de contingencia por defecto (6.96).
    """
    url_api = "https://open.er-api.com/v6/latest/USD"
    tasa_fallback = 6.96

    try:
        # Petición HTTP GET con tiempo de espera máximo de 3 segundos para no congelar la UI
        peticion = urllib.request.Request(
            url_api, 
            headers={"User-Agent": "LASIN-Python-LogiFlow/1.0"}
        )
        with urllib.request.urlopen(peticion, timeout=3) as respuesta:
            if respuesta.status == 200:
                datos = json.loads(respuesta.read().decode("utf-8"))
                tasa = datos.get("rates", {}).get("BOB", tasa_fallback)
                print(f"[API] Tasa de cambio obtenida exitosamente en línea: 1 USD = {tasa:.2f} BOB")
                return float(tasa)
    except (urllib.error.URLError, TimeoutError, Exception) as error:
        print(f"[AVISO API] No se pudo consultar la API externa ({error}). Usando tasa de contingencia: {tasa_fallback} BOB")

    return tasa_fallback


# ======================================================================================
# 3. INGESTA Y LIMPIEZA DE DATOS (Módulos 3 y 4: csv, pathlib, set y try-except)
# ======================================================================================

def cargar_y_auditar_csv(ruta_archivo: Path) -> tuple[list[Envio], dict[str, int]]:
    """
    Lee un archivo CSV con transacciones logísticas, aplica deduplicación mediante
    conjuntos (set) y maneja excepciones fila por fila para evitar caídas de ejecución.
    
    Retorna:
     - Lista de objetos Envio válidos y deduplicados.
     - Diccionario de métricas del proceso de ingesta.
    """
    if not ruta_archivo.exists():
        raise FileNotFoundError(f"No se encontró el archivo de datos en: {ruta_archivo}")

    envios_procesados: list[Envio] = []
    ids_vistos: set[str] = set()  # Colección set para deduplicación O(1)
    
    metricas = {
        "total_filas": 0,
        "duplicados": 0,
        "con_error": 0,
        "aprobados": 0,
        "observados": 0,
        "rechazados": 0
    }

    with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        
        for num_fila, fila in enumerate(lector, start=2):
            metricas["total_filas"] += 1
            id_envio = fila.get("id_envio", "").strip()

            # 1. Detección y filtrado de duplicados usando conjunto (set)
            if id_envio in ids_vistos:
                metricas["duplicados"] += 1
                print(f"[AVISO] Registro duplicado omitido: {id_envio} (fila {num_fila})")
                continue

            # 2. Bloque try-except defensivo para atrapar datos corruptos
            try:
                cliente_limpio = fila.get("cliente", "").strip()
                peso = float(fila.get("peso_kg", 0))
                costo = float(fila.get("costo_base", 0))
                
                # Normalización y validación del tipo de envío con Enum
                str_tipo = fila.get("tipo", "ESTANDAR").strip().upper()
                tipo_enum = TipoEnvio(str_tipo)
                
                lat = float(fila.get("latitud", 0))
                lon = float(fila.get("longitud", 0))

                # Instanciación de la Dataclass (dispara __post_init__)
                nuevo_envio = Envio(
                    id_envio=id_envio,
                    cliente=cliente_limpio,
                    peso_kg=peso,
                    costo_base=costo,
                    tipo=tipo_enum,
                    latitud=lat,
                    longitud=lon
                )

                # Clasificación de auditoría
                estado = nuevo_envio.auditar()
                match estado:
                    case EstadoAuditoria.APROBADO:
                        metricas["aprobados"] += 1
                    case EstadoAuditoria.OBSERVADO:
                        metricas["observados"] += 1
                    case EstadoAuditoria.RECHAZADO:
                        metricas["rechazados"] += 1

                ids_vistos.add(id_envio)
                envios_procesados.append(nuevo_envio)

            except (ValueError, KeyError) as error:
                metricas["con_error"] += 1
                print(f"[AVISO] Fila {num_fila} descartada por datos inválidos ({id_envio}): {error}")

    return envios_procesados, metricas


# ======================================================================================
# 4. PERSISTENCIA EN BASE DE DATOS RELACIONAL (Módulo 5: sqlite3)
# ======================================================================================

def guardar_en_sqlite(envios_aprobados: list[Envio], tasa_cambio: float, ruta_db: Path) -> int:
    """
    Crea la tabla 'envios_aprobados' en SQLite y almacena los envíos validados
    usando sentencias parametrizadas seguras para evitar inyección SQL.
    """
    # Context manager 'with' asegura el commit y cierre de la conexión
    with sqlite3.connect(ruta_db) as conexion:
        cursor = conexion.cursor()
        
        # Creación de tabla DDL
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS envios_aprobados (
                id TEXT PRIMARY KEY,
                cliente TEXT NOT NULL,
                tipo TEXT NOT NULL,
                peso_kg REAL NOT NULL,
                costo_usd REAL NOT NULL,
                costo_bob REAL NOT NULL,
                latitud REAL NOT NULL,
                longitud REAL NOT NULL
            )
        """)

        # Preparación de datos mediante tuplas
        registros_a_insertar = [
            (
                e.id_envio,
                e.cliente,
                e.tipo.value,
                e.peso_kg,
                e.calcular_costo_final(),
                round(e.calcular_costo_final() * tasa_cambio, 2),
                e.latitud,
                e.longitud
            )
            for e in envios_aprobados
        ]

        # Inserción masiva segura y atómica
        cursor.executemany("""
            INSERT OR REPLACE INTO envios_aprobados 
            (id, cliente, tipo, peso_kg, costo_usd, costo_bob, latitud, longitud)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, registros_a_insertar)

        conexion.commit()
        return cursor.rowcount


# ======================================================================================
# 5. GENERACIÓN DE FORMATOS GEOESPACIALES (Módulo 5: GeoJSON)
# ======================================================================================

def exportar_geojson(envios_aprobados: list[Envio], ruta_salida: Path) -> None:
    """
    Genera un archivo GeoJSON estándar (RFC 7946) con los puntos de entrega
    para visualización directa en visores geográficos (geojson.io, QGIS).
    """
    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [e.longitud, e.latitud]  # Estándar GeoJSON: [X: Lon, Y: Lat]
            },
            "properties": {
                "id_envio": e.id_envio,
                "cliente": e.cliente,
                "tipo": e.tipo.value,
                "peso_kg": e.peso_kg,
                "costo_usd": e.calcular_costo_final()
            }
        }
        for e in envios_aprobados
    ]

    coleccion_geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(ruta_salida, mode="w", encoding="utf-8") as archivo:
        json.dump(coleccion_geojson, archivo, indent=2, ensure_ascii=False)


# ======================================================================================
# 6. REPORTES Y SALIDAS TABULARES (Módulo 1 y 3: f-strings y comprensiones)
# ======================================================================================

def mostrar_reporte_tabular(envios_aprobados: list[Envio], tasa_cambio: float) -> None:
    """
    Imprime un informe financiero y logístico con columnas tabulares alineadas con f-strings.
    Calcula además distribuciones agrupadas por tipo usando comprensiones de diccionarios.
    """
    if not envios_aprobados:
        print("\n[!] No existen envíos aprobados para mostrar. Ingiere el lote primero.")
        return

    ancho_linea = 88
    print("\n" + "=" * ancho_linea)
    print("REPORTE DE ENVÍOS APROBADOS (LOGIFLOW)".center(ancho_linea))
    print("=" * ancho_linea)
    print(f"{'ID ENVÍO':<10} {'CLIENTE':<22} {'TIPO':<15} {'PESO (KG)':>10} {'COSTO (USD)':>14} {'COSTO (BOB)':>14}")
    print("-" * ancho_linea)

    total_peso = 0.0
    total_usd = 0.0
    total_bob = 0.0

    for e in envios_aprobados:
        costo_usd = e.calcular_costo_final()
        costo_bob = costo_usd * tasa_cambio

        total_peso += e.peso_kg
        total_usd += costo_usd
        total_bob += costo_bob

        txt_usd = f"$ {costo_usd:,.2f}"
        txt_bob = f"Bs. {costo_bob:,.2f}"

        print(
            f"{e.id_envio:<10} "
            f"{e.cliente:<22} "
            f"{e.tipo.value:<15} "
            f"{e.peso_kg:>10.2f} "
            f"{txt_usd:>14} "
            f"{txt_bob:>14}"
        )

    print("-" * ancho_linea)
    tot_usd_txt = f"$ {total_usd:,.2f}"
    tot_bob_txt = f"Bs. {total_bob:,.2f}"
    print(
        f"{'TOTALES:':<10} "
        f"{f'{len(envios_aprobados)} Envíos':<22} "
        f"{'':<15} "
        f"{f'{total_peso:.2f} kg':>10} "
        f"{tot_usd_txt:>14} "
        f"{tot_bob_txt:>14}"
    )
    print("=" * ancho_linea)

    # 4. Comprensión de diccionarios (dict comprehension) para totales por categoría
    tipos_presentes = {e.tipo for e in envios_aprobados}
    distribucion_montos = {
        tipo.value: sum(e.calcular_costo_final() for e in envios_aprobados if e.tipo == tipo)
        for tipo in tipos_presentes
    }
    conteo_por_tipo = {
        tipo.value: sum(1 for e in envios_aprobados if e.tipo == tipo)
        for tipo in tipos_presentes
    }

    print("• Distribución por Tipo de Envío:")
    for tipo_str, subtotal in distribucion_montos.items():
        cantidad = conteo_por_tipo[tipo_str]
        print(f"  - {tipo_str:<12}: ${subtotal:>8.2f} USD ({cantidad} envíos)")
    print("=" * ancho_linea)


# ======================================================================================
# 7. MENÚ INTERACTIVO PRINCIPAL (Módulo 2: while, match-case e input)
# ======================================================================================

def main() -> None:
    directorio_actual = Path(__file__).resolve().parent
    ruta_csv = directorio_actual / "datos_envios.csv"
    ruta_db = directorio_actual / "auditoria_envios.db"
    ruta_geojson = directorio_actual / "envios_aprobados.geojson"

    # Estado en memoria de la sesión de trabajo
    todos_los_envios: list[Envio] = []
    envios_aprobados: list[Envio] = []
    tasa_cambio_actual = 6.96

    print("\nInicializando sistema LogiFlow...")
    tasa_cambio_actual = obtener_tipo_cambio_usd_a_bob()

    while True:
        print("\n" + "=" * 60)
        print("     LOGIFLOW — SISTEMA DE AUDITORÍA Y CONTROL (LASIN)")
        print("=" * 60)
        print("[1] Ingerir y Auditar Lote de Envíos (CSV)")
        print("[2] Mostrar Reporte Tabular de Envíos Aprobados")
        print("[3] Guardar Envíos Aprobados en Base de Datos (SQLite)")
        print("[4] Exportar Coordenadas a GeoJSON (Mapa)")
        print("[5] Salir del Sistema")
        print("-" * 60)
        
        opcion = input("Seleccione una opción (1-5): ").strip()

        match opcion:
            case "1":
                print(f"\n>>> Procesando archivo: {ruta_csv.name} ...")
                try:
                    todos_los_envios, metricas = cargar_y_auditar_csv(ruta_csv)
                    
                    # Comprensión de listas (list comprehension) para filtrar los APROBADOS
                    envios_aprobados = [
                        e for e in todos_los_envios 
                        if e.auditar() == EstadoAuditoria.APROBADO
                    ]

                    print("\n✓ Resumen de Auditoría:")
                    print(f"  - Filas procesadas:        {metricas['total_filas']:>4}")
                    print(f"  - Registros únicos:        {len(todos_los_envios):>4}")
                    print(f"  - Registros con error:     {metricas['con_error']:>4}")
                    print(f"  - Registros duplicados:    {metricas['duplicados']:>4}")
                    print(f"  - Envíos APROBADOS:        {metricas['aprobados']:>4}")
                    print(f"  - Envíos OBSERVADOS:       {metricas['observados']:>4}")
                    print(f"  - Envíos RECHAZADOS:       {metricas['rechazados']:>4}")

                except FileNotFoundError as err:
                    print(f"[ERROR] {err}")

            case "2":
                mostrar_reporte_tabular(envios_aprobados, tasa_cambio_actual)

            case "3":
                if not envios_aprobados:
                    print("\n[!] Debe primero procesar un lote con la Opción 1.")
                    continue
                print(f"\n>>> Guardando en base de datos: {ruta_db.name} ...")
                guardados = guardar_en_sqlite(envios_aprobados, tasa_cambio_actual, ruta_db)
                print(f"✓ {guardados} registros almacenados/actualizados correctamente en SQLite.")

            case "4":
                if not envios_aprobados:
                    print("\n[!] Debe primero procesar un lote con la Opción 1.")
                    continue
                print(f"\n>>> Exportando puntos de entrega a GeoJSON ...")
                exportar_geojson(envios_aprobados, ruta_geojson)
                print(f"✓ Archivo generado exitosamente en: {ruta_geojson.name}")
                print(f"✓ Contiene {len(envios_aprobados)} características espaciales (Point).")

            case "5":
                print("\nCerrando sesión en LogiFlow. ¡Hasta pronto!\n")
                break

            case _:
                print(f"\n[!] Opción inválida ('{opcion}'). Por favor elija un número del 1 al 5.")


if __name__ == "__main__":
    main()
