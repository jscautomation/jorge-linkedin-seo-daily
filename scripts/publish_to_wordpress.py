# -*- coding: utf-8 -*-
"""
Sube el articulo-blog.html de una carpeta de contenido diario a WordPress
como BORRADOR (nunca lo publica directamente — eso lo decide Jorge desde
el editor de WordPress).

Uso:
    python3 scripts/publish_to_wordpress.py content/2026-08-18-martes-mito

Requiere en el .env local: WP_URL, WP_USERNAME, WP_APP_PASSWORD
(contraseña de aplicación de WordPress, nunca la contraseña de acceso).
Esta clave NUNCA debe subirse al repo ni pasarse a la rutina en la nube
— se ejecuta siempre en local, igual que sync_klaviyo_segments.py con
Klaviyo (ver AUTOMATION_BRIEF.md).
"""
import os
import re
import sys
from pathlib import Path

import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent


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


def extract_title_and_body(html: str):
    # Quita el bloque de comentario HTML de instrucciones del principio, si existe.
    html = re.sub(r"^\s*<!--.*?-->\s*", "", html, count=1, flags=re.DOTALL)

    match = re.search(r"<h1[^>]*>(.*?)</h1>", html, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        print("ERROR: no se encontró un <h1> en el artículo para usar como título.")
        sys.exit(1)
    title = re.sub(r"<[^>]+>", "", match.group(1)).strip()

    body = html[: match.start()] + html[match.end():]
    return title, body.strip()


def publish_draft(content_dir: Path):
    load_env()
    wp_url = os.environ.get("WP_URL")
    wp_user = os.environ.get("WP_USERNAME")
    wp_pass = os.environ.get("WP_APP_PASSWORD")
    if not all([wp_url, wp_user, wp_pass]):
        print("ERROR: faltan WP_URL / WP_USERNAME / WP_APP_PASSWORD en .env")
        sys.exit(1)

    article_path = content_dir / "articulo-blog.html"
    if not article_path.exists():
        print(f"ERROR: no existe {article_path}")
        sys.exit(1)

    html = article_path.read_text(encoding="utf-8")
    title, body = extract_title_and_body(html)

    # Envuelto en un bloque nativo "wp:html" de Gutenberg: así WordPress
    # respeta el HTML tal cual y NO le aplica wpautop (que si no, mete <p>
    # dentro del <script> del formulario y rompe el JavaScript).
    block_content = f"<!-- wp:html -->\n{body}\n<!-- /wp:html -->"

    resp = requests.post(
        f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts",
        auth=(wp_user, wp_pass),
        json={
            "title": title,
            "content": block_content,
            "status": "draft",
        },
    )

    if resp.status_code == 201:
        data = resp.json()
        edit_link = f"{wp_url.rstrip('/')}/wp-admin/post.php?post={data['id']}&action=edit"
        print(f"OK: borrador creado — \"{title}\"")
        print(f"    Editar en: {edit_link}")
    else:
        print(f"FAIL ({resp.status_code}): {resp.text[:500]}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 scripts/publish_to_wordpress.py content/<carpeta-del-dia>")
        sys.exit(1)
    publish_draft(REPO_ROOT / sys.argv[1])
