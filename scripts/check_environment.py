import shutil
import sys

tools = {
    "Git": "git",
    "FFmpeg": "ffmpeg",
    "FFprobe": "ffprobe",
    "ExifTool": "exiftool",
    "ImageMagick": "magick",
}

print("Media Lifecycle Management – Systemcheck")
print("-" * 48)
print(f"✓ Python {sys.version.split()[0]}")

missing = []
for name, command in tools.items():
    path = shutil.which(command)
    if path:
        print(f"✓ {name}: {path}")
    else:
        print(f"○ {name}: nicht gefunden")
        missing.append(name)

print("-" * 48)
if missing:
    print("Hinweis: Einige optionale Medienwerkzeuge fehlen:")
    print(", ".join(missing))
    print("Das Repo kann trotzdem genutzt werden; installieren Sie die Werkzeuge vor der jeweiligen Übung.")
else:
    print("Alle geprüften Werkzeuge wurden gefunden.")
