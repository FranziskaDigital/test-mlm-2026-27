import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "media.json"
SCHEMA_FILE = ROOT / "data" / "media.schema.json"

data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
schema = json.loads(SCHEMA_FILE.read_text(encoding="utf-8"))

validator = Draft202012Validator(schema)
errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))

if errors:
    print("Metadaten sind NICHT valide.\n")
    for error in errors:
        location = " → ".join(str(item) for item in error.path) or "(root)"
        print(f"{location}: {error.message}")
    sys.exit(1)

ids = [obj["id"] for obj in data]
duplicates = sorted({x for x in ids if ids.count(x) > 1})
if duplicates:
    print("Doppelte Objekt-Identifier:", ", ".join(duplicates))
    sys.exit(1)

print(f"✓ {len(data)} Medienobjekt(e) valide.")
