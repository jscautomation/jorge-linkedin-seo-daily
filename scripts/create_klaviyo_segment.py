# -*- coding: utf-8 -*-
"""
Crea en Klaviyo un segmento "Descargó: <título del PDF>" que agrupa
automáticamente a todos los perfiles que hayan descargado ese PDF exacto
(filtra por la propiedad pdf_titulo del evento "Solicitó Lead Magnet").

Uso:
    python3 scripts/create_klaviyo_segment.py "Título exacto del PDF"

Requiere KLAVIYO_API_KEY en el .env local (esta clave NUNCA debe subirse
al repo ni pasarse a la rutina en la nube — se ejecuta siempre en local).
"""
import os
import sys
from pathlib import Path

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
METRIC_ID = "SJvVTG"  # métrica "Solicitó Lead Magnet", fija


def load_env():
    env_path = REPO_ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


def create_segment(pdf_titulo: str):
    load_env()
    api_key = os.environ.get("KLAVIYO_API_KEY")
    if not api_key:
        print("ERROR: no se encontró KLAVIYO_API_KEY en .env")
        sys.exit(1)

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

    resp = requests.post(
        "https://a.klaviyo.com/api/segments/",
        headers={
            "Authorization": f"Klaviyo-API-Key {api_key}",
            "Content-Type": "application/vnd.api+json",
            "revision": "2024-10-15",
        },
        json=payload,
    )
    if resp.status_code == 201:
        seg_id = resp.json()["data"]["id"]
        print(f"OK: segmento creado '{name}' (id {seg_id})")
    else:
        print(f"FAIL ({resp.status_code}): {resp.text}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Uso: python3 scripts/create_klaviyo_segment.py "Título exacto del PDF"')
        sys.exit(1)
    create_segment(sys.argv[1])
