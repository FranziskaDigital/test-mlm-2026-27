# Media Lifecycle Management – Leipzig als digitaler Medienraum

Starter-Repository für das Modul **Media Lifecycle Management**.

## Ziel

Das Semesterprojekt bildet einen vollständigen Lebenszyklus medialer Daten ab:

**PLAN → INGEST → CHARACTERIZE → PROCESS → ORGANIZE → DESCRIBE → INTEROPERATE → AUTOMATE → QUALITY → PRESERVE → PUBLISH → HANDOVER**

Bearbeitet werden unterschiedliche Medientypen:

- Bild
- Audio
- Video
- 3D
- Geodaten

## Grundprinzip

Das Git-Repository ist **kein Preservation Storage**.

In Git gehören insbesondere:

- Metadaten
- Inventare
- Dokumentation
- Skripte
- Provenienzinformationen
- kleine Access-Derivate
- die Webanwendung

Nicht in Git gehören insbesondere:

- große Rohdaten
- TIFF-/WAV-/Video-Preservation-Master
- große Punktwolken
- sensible oder nicht publizierbare Quelldaten

## Schnellstart

### 1. Repository klonen

```bash
git clone <GITLAB-URL>
cd mlm-leipzig-gitlab
```

### 2. Python-Abhängigkeiten installieren

```bash
python -m pip install -r requirements.txt
```

### 3. System prüfen

```bash
python scripts/check_environment.py
```

### 4. Metadaten validieren

```bash
python scripts/validate_metadata.py
```

### 5. Website bauen

```bash
python scripts/build_web.py
```

### 6. Website lokal starten

```bash
python -m http.server 8000 --directory public
```

Dann öffnen:

`http://localhost:8000`

## Zentrale Datenebenen

- `data/media.json` beschreibt **Medienobjekte**
- `data/inventory.csv` beschreibt **Dateien/Repräsentationen**
- `data/provenance.json` beschreibt **Lifecycle-Ereignisse**
- `projects/` dokumentiert die gruppenspezifischen Workflows
- `web/` enthält die Weboberfläche und kleine Access-Derivate
- `public/` wird automatisch erzeugt und nicht versioniert

## Releases

- **R0 PLAN** – Projekt und Medienprofil definiert
- **R1 INGEST** – Daten übernommen, inventarisiert, charakterisiert
- **R2 PROCESS & DESCRIBE** – Repräsentationen, Metadaten, Schema
- **R3 PRESERVE** – Qualität, Provenienz, Preservation Plan, Manifest
- **R4 ACCESS & REUSE** – Webpublikation und Handover
