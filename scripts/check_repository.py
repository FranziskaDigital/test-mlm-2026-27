from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "data/media.json",
    "data/media.schema.json",
    "data/inventory.csv",
    "data/provenance.json",
    "web/index.html",
    "web/app.js",
    "web/style.css",
    "docs/lifecycle.md",
]

missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("Fehlende Pflichtdateien:")
    for p in missing:
        print(f"- {p}")
    sys.exit(1)

print("✓ Repository-Grundstruktur vollständig.")
