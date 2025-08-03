# Arbeitsblatt 4: Einführung in Pydantic

## Theorie-Teil: Was ist Pydantic und warum nutzen wir es?
- Pydantic ermöglicht einfache Validierung, Serialisierung und Verwaltung von Datenstrukturen in Python.
- Es garantiert, dass die von einer API erhaltenen Daten einem definierten Schema entsprechen.

## Aufgabe 4: Praxisaufgaben zu Pydantic

### Teilaufgabe A:
1. Installiere Pydantic (`pip install pydantic`) und definiere ein einfaches Datenmodell:

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=50)
    age: int | None
```

2. Teste dein Modell mit korrekten und inkorrekten Daten.

### Teilaufgabe B:
- Integriere Pydantic mit einem LLM-API-Aufruf und parse den Output der OpenAI-API in dein Datenmodell.
