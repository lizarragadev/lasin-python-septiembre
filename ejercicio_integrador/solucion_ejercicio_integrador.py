"""
========================================================================================
LOGIFLOW — SISTEMA DE ENVÍOS LOGÍSTICOS
Solución Oficial del Ejercicio Práctico Integrador (LASIN - Curso Python Básico)
========================================================================================
Integra los conceptos esenciales del curso:
 - Módulo 1: Tipado, operadores y f-strings tabulares.
 - Módulo 2: Lógica condicional (match-case).
 - Módulo 3: Conjuntos (set), comprensiones, funciones y manejo de errores (try-except).
 - Módulo 4: Rutas con pathlib, lectura CSV y consumo de API web con fallback resiliente.
 - Módulo 5: Enums, @dataclass y persistencia relacional con SQLite.
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


# --------------------------------------------------------------------------------------
# 1. MODELADO CON POO (Dataclass y Enum)
# --------------------------------------------------------------------------------------

class TipoEnvio(str, Enum):
    """Categorías permitidas para los envíos."""
    ESTANDAR = "ESTANDAR"
    EXPRESS = "EXPRESS"
    REFRIGERADO = "REFRIGERADO"


@dataclass
class Envio:
    """Entidad que representa un envío logístico individual."""
    id_envio: str
    cliente: str
    peso_kg: float
    costo_base: float
    tipo: TipoEnvio

    def __post_init__(self) -> None:
        """Validación de integridad física de los datos."""
        if self.peso_kg <= 0:
            raise ValueError(f"El peso debe ser mayor a 0 kg (recibido: {self.peso_kg})")
        if self.costo_base < 0:
            raise ValueError(f"El costo base no puede ser negativo (recibido: {self.costo_base})")

    def calcular_costo_final(self) -> float:
        """Aplica recargos comerciales según el tipo de envío."""
        match self.tipo:
            case TipoEnvio.EXPRESS:
                return round(self.costo_base * 1.20, 2)
            case TipoEnvio.REFRIGERADO:
                return round(self.costo_base * 1.35, 2)
            case TipoEnvio.ESTANDAR | _:
                return round(self.costo_base, 2)


# --------------------------------------------------------------------------------------
# 2. ENRIQUECIMIENTO CON API EXTERNA
# --------------------------------------------------------------------------------------

def obtener_tipo_cambio() -> float:
    """Consulta la tasa USD/BOB desde API web con respaldo por defecto ante fallas."""
    url = "https://open.er-api.com/v6/latest/USD"
    tasa_defecto = 6.96

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "LASIN-Python/1.0"})
        with urllib.request.urlopen(req, timeout=3) as resp:
            if resp.status == 200:
                datos = json.loads(resp.read().decode("utf-8"))
                tasa = float(datos.get("rates", {}).get("BOB", tasa_defecto))
                print(f"[API] Tasa obtenida: 1 USD = {tasa:.2f} BOB")
                return tasa
    except (urllib.error.URLError, TimeoutError, Exception):
        print(f"[API] Conexión no disponible. Usando tasa de contingencia: 1 USD = {tasa_defecto:.2f} BOB")

    return tasa_defecto


# --------------------------------------------------------------------------------------
# 3. INGESTA Y LIMPIEZA DE DATOS (CSV, Set, Try-Except)
# --------------------------------------------------------------------------------------

def cargar_envios(ruta_csv: Path) -> list[Envio]:
    """Lee el CSV, deduplica con set y descarta filas con errores usando try-except."""
    if not ruta_csv.exists():
        print(f"[ERROR] No existe el archivo: {ruta_csv}")
        return []

    envios: list[Envio] = []
    ids_vistos: set[str] = set()

    with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            id_envio = fila.get("id_envio", "").strip()

            # Deduplicación con conjunto (set)
            if id_envio in ids_vistos:
                print(f"[AVISO] Omitido por duplicado: {id_envio}")
                continue

            # Validación y captura de datos erróneos con try-except
            try:
                nuevo = Envio(
                    id_envio=id_envio,
                    cliente=fila.get("cliente", "").strip(),
                    peso_kg=float(fila.get("peso_kg", 0)),
                    costo_base=float(fila.get("costo_base", 0)),
                    tipo=TipoEnvio(fila.get("tipo", "ESTANDAR").strip().upper())
                )
                ids_vistos.add(id_envio)
                envios.append(nuevo)
            except (ValueError, KeyError) as err:
                print(f"[AVISO] Fila descartada ({id_envio}): {err}")

    return envios


# --------------------------------------------------------------------------------------
# 4. PERSISTENCIA EN SQLITE
# --------------------------------------------------------------------------------------

def guardar_en_sqlite(envios: list[Envio], tasa: float, ruta_db: Path) -> int:
    """Guarda los envíos válidos en SQLite mediante sentencias parametrizadas seguras."""
    with sqlite3.connect(ruta_db) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS envios (
                id TEXT PRIMARY KEY,
                cliente TEXT NOT NULL,
                tipo TEXT NOT NULL,
                peso_kg REAL NOT NULL,
                costo_usd REAL NOT NULL,
                costo_bob REAL NOT NULL
            )
        """)
        registros = [
            (
                e.id_envio,
                e.cliente,
                e.tipo.value,
                e.peso_kg,
                e.calcular_costo_final(),
                round(e.calcular_costo_final() * tasa, 2)
            )
            for e in envios
        ]
        cursor.executemany("INSERT OR REPLACE INTO envios VALUES (?, ?, ?, ?, ?, ?)", registros)
        conn.commit()
        return len(registros)


# --------------------------------------------------------------------------------------
# 5. REPORTE EN CONSOLA CON F-STRINGS
# --------------------------------------------------------------------------------------

def mostrar_reporte(envios: list[Envio], tasa: float) -> None:
    """Imprime una tabla formateada y los totales del lote."""
    ancho = 70
    print("\n" + "-" * ancho)
    print(f"{'ID':<10} {'CLIENTE':<21} {'TIPO':<15} {'USD':>10} {'BOB':>18}")
    print("-" * ancho)

    total_usd = sum(e.calcular_costo_final() for e in envios)
    total_bob = total_usd * tasa

    for e in envios:
        c_usd = e.calcular_costo_final()
        c_bob = c_usd * tasa
        txt_usd = f"$ {c_usd:>8,.2f}"
        txt_bob = f"Bs. {c_bob:>10,.2f}"
        print(f"{e.id_envio:<10} {e.cliente:<21} {e.tipo.value:<15} {txt_usd}  {txt_bob}")

    print("-" * ancho)
    print(f"TOTAL: {len(envios)} envíos válidos | $ {total_usd:,.2f} USD | Bs. {total_bob:,.2f} BOB")


# --------------------------------------------------------------------------------------
# FUNCIÓN PRINCIPAL
# --------------------------------------------------------------------------------------

def main() -> None:
    directorio = Path(__file__).resolve().parent
    ruta_csv = directorio / "datos_envios.csv"
    ruta_db = directorio / "envios.db"

    print("=== SISTEMA DE ENVÍOS LOGIFLOW ===")
    tasa = obtener_tipo_cambio()
    envios = cargar_envios(ruta_csv)

    if envios:
        mostrar_reporte(envios, tasa)
        guardados = guardar_en_sqlite(envios, tasa, ruta_db)
        print(f"✓ {guardados} registros guardados exitosamente en SQLite ({ruta_db.name}).\n")


if __name__ == "__main__":
    main()
