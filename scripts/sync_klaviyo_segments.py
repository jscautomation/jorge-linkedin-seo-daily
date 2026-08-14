# -*- coding: utf-8 -*-
"""
Revisa el historial de eventos "Solicitó Lead Magnet" en Klaviyo, saca todos
los títulos de PDF distintos que aparecen, y crea el segmento "Descargó: X"
para cualquiera que todavía no lo tenga. Los que ya existen no se duplican.

Uso: python3 scripts/sync_klaviyo_segments.py
Requiere KLAVIYO_API_KEY en el .env local. Se ejecuta siempre en local,
nunca desde la rutina en la nube (ver AUTOMATION_BRIEF.md § 8).
"""
import os
import sys
import time
from pathlib import Path

import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
METRIC_ID = "SJvVTG"  # "Solicitó Lead Magnet"
REVISION = "2024-10-15"


def load_env():
    env_path = REPO_ROOT / ".env"
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


def get_distinct_pdf_titles(session):
    titles = set()
    url = "https://a.klaviyo.com/api/events/"
    params = {
        "filter": f'equals(metric_id,"{METRIC_ID}")',
        "page[size]": 200,
    }
    while url:
        resp = session.get(url, params=params if "?" not in url else None)
        resp.raise_for_status()
        data = resp.json()
        for event in data["data"]:
            title = event["attributes"]["event_properties"].get("pdf_titulo")
            if title:
                titles.add(title)
        url = data["links"].get("next")
        params = None  # 'next' ya trae los params codificados
    return titles


def get_existing_segment_names(session):
    names = set()
    url = "https://a.klaviyo.com/api/segments/"
    params = {"page[size]": 10}
    while url:
        resp = session.get(url, params=params if "?" not in url else None)
        resp.raise_for_status()
        data = resp.json()
        for seg in data["data"]:
            names.add(seg["attributes"]["name"])
        url = data["links"].get("next")
        params = None
    return names


def create_segment(session, pdf_titulo):
    name = f"Descargó: {pdf_titulo[:60]}"
    payload = {
        "data": {
            "type": "segment",
            "attributes": {
                "name": name,
                "definition": {
                    "condition_groups": [
                        {
                            "conditions": [
                                {
                                    "type": "profile-metric",
                                    "metric_id": METRIC_ID,
                                    "measurement": "count",
                                    "measurement_filter": {
                                        "type": "numeric",
                                        "operator": "greater-than-or-equal",
                                        "value": 1,
                                    },
                                    "timeframe_filter": {"type": "date", "operator": "alltime"},
                                    "metric_filters": [
                                        {
                                            "property": "pdf_titulo",
                                            "filter": {
                                                "type": "string",
                                                "operator": "equals",
                                                "value": pdf_titulo,
                                            },
                                        }
                                    ],
                                }
                            ]
                        }
                    ]
                },
            },
        }
    }
    for attempt in range(4):
        resp = session.post("https://a.klaviyo.com/api/segments/", json=payload)
        if resp.status_code == 201:
            print(f"OK creado: {name}")
            return
        if resp.status_code == 429:
            wait = 2 ** attempt
            print(f"  (rate limit, reintentando en {wait}s...)")
            time.sleep(wait)
            continue
        print(f"FAIL '{name}': {resp.status_code} {resp.text[:200]}")
        return
    print(f"FAIL '{name}': se agotaron los reintentos por rate limit")


def main():
    load_env()
    api_key = os.environ.get("KLAVIYO_API_KEY")
    if not api_key:
        print("ERROR: no se encontró KLAVIYO_API_KEY en .env")
        return

    session = requests.Session()
    session.headers.update({
        "Authorization": f"Klaviyo-API-Key {api_key}",
        "Content-Type": "application/vnd.api+json",
        "revision": REVISION,
    })

    titles = get_distinct_pdf_titles(session)
    print(f"Títulos de PDF encontrados en el historial ({len(titles)}):")
    for t in titles:
        print(f"  - {t}")

    existing = get_existing_segment_names(session)
    faltan = [t for t in titles if f"Descargó: {t[:60]}" not in existing]

    if not faltan:
        print("\nTodos los títulos ya tienen su segmento. Nada que hacer.")
        return

    print(f"\nCreando {len(faltan)} segmento(s) nuevo(s)...")
    for i, t in enumerate(faltan):
        if i > 0:
            time.sleep(1.5)
        create_segment(session, t)


if __name__ == "__main__":
    main()
