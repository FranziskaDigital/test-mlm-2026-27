from pathlib import Path
import hashlib
import sys

def sha256(file_path):
    digest = hashlib.sha256()
    with open(file_path, "rb") as file:
        while chunk := file.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()

if len(sys.argv) != 2:
    print("Verwendung: python scripts/make_checksums.py <ordner>")
    sys.exit(1)

root = Path(sys.argv[1])
if not root.exists() or not root.is_dir():
    print(f"Ordner nicht gefunden: {root}")
    sys.exit(1)

output = root / "checksums.sha256"
files = sorted(
    file for file in root.rglob("*")
    if file.is_file() and file != output
)

with open(output, "w", encoding="utf-8") as checksum_file:
    for file in files:
        checksum = sha256(file)
        relative = file.relative_to(root)
        checksum_file.write(f"{checksum}  {relative.as_posix()}\n")

print(f"✓ Checksums für {len(files)} Datei(en) erzeugt: {output}")
