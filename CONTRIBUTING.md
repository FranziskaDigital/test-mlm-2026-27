# Mitarbeit

## Branches

Gruppen arbeiten zunächst in eigenen Branches, z. B.:

```text
group/image
group/audio
group/video
group/3d
group/geo
```

Feature-Branches sind ebenfalls möglich:

```text
feature/audio-pipeline
feature/metadata-schema
feature/geo-viewer
```

## Commits

Gute Commit-Nachrichten:

```text
Add metadata for LDM-0007
Create MP3 access derivative
Document image transformation
Fix coordinates for LDM-0013
```

Ungünstig:

```text
update
stuff
changes
final
```

## Gemeinsame Dateien

Änderungen an diesen Dateien müssen abgestimmt werden:

- `data/media.schema.json`
- `web/app.js`
- `web/index.html`
- `docs/metadata.md`

## Vor einem Merge

```bash
python scripts/validate_metadata.py
python scripts/build_web.py
```

## Große Dateien

Große Master- und Quelldateien nicht in Git committen. Der externe Speicherort wird in
`docs/storage.md` und im `inventory.csv` dokumentiert.
