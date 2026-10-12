"""
Minimaler Starter für technische Charakterisierung.

Im Semester soll dieses Skript erweitert werden, z. B. um:
- ExifTool
- ffprobe
- Dateigröße
- MIME-Type
- medienspezifische technische Eigenschaften
"""
from pathlib import Path
import hashlib
import mimetypes
import json
import sys

if len(sys.argv) != 2:
    print("Verwendung: python scripts/characterize.py <datei>")
    sys.exit(1)

path = Path(sys.argv[1])
if not path.exists():
    print("Datei nicht gefunden.")
    sys.exit(1)

digest = hashlib.sha256(path.read_bytes()).hexdigest()
mime, _ = mimetypes.guess_type(path.name)

result = {
    "filename": path.name,
    "size_bytes": path.stat().st_size,
    "mime_guess": mime,
    "sha256": digest,
}

print(json.dumps(result, indent=2, ensure_ascii=False))
