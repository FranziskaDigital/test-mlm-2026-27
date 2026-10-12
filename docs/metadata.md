# Gemeinsames Metadatenmodell

## Ebenen

### Objektbezogene Metadaten
Titel, Beschreibung, Typ, räumlicher und zeitlicher Bezug.

### Technische Metadaten
Medienspezifische Dateieigenschaften.

### Administrative Metadaten
Rechte, Verantwortlichkeiten, Speicherort.

### Preservation-Metadaten
Fixity, Events, Agenten, Format- und Erhaltungsinformationen.

## Gemeinsamer Kern

| Feld | Bedeutung | Pflicht |
|---|---|---|
| id | Projekt-Identifier | ja |
| title | Titel | ja |
| type | Medientyp | ja |
| description | Beschreibung | ja |
| location | räumlicher Bezug | ja |
| representations | Access-Repräsentationen | ja |
| rights | Rechteinformation | ja |
| keywords | Schlagwörter | nein |
| technical | medienspezifische technische Metadaten | nein |

Die medienspezifischen Felder werden im Semester weiterentwickelt.
