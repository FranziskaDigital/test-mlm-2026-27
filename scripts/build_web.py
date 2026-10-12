from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "web"
PUBLIC = ROOT / "public"

if PUBLIC.exists():
    shutil.rmtree(PUBLIC)

shutil.copytree(WEB, PUBLIC)

(PUBLIC / "data").mkdir(parents=True, exist_ok=True)
shutil.copy2(ROOT / "data" / "media.json", PUBLIC / "data" / "media.json")
shutil.copy2(ROOT / "data" / "media.schema.json", PUBLIC / "data" / "media.schema.json")

print(f"✓ Website gebaut: {PUBLIC}")
print("  Lokal starten mit:")
print("  python -m http.server 8000 --directory public")
