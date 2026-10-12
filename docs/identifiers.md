# Identifier

## Objekt-Identifier

Schema:

```text
LDM-0001
LDM-0002
...
```

Der Objekt-Identifier identifiziert das **Medienobjekt**, nicht eine einzelne Datei.

## Datei-Identifier

Schema:

```text
F0001
F0002
...
```

Eine Objekt-ID kann mit mehreren Datei-IDs verbunden sein:

```text
LDM-0001
 ├── F0001 source
 ├── F0002 master
 ├── F0003 access
 └── F0004 thumbnail
```
