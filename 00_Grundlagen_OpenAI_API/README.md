# Arbeitsblatt 1: Grundlagen OpenAI API erkunden (Praxis)

## Teilaufgabe A:
1. Erstelle einen Account bei [platform.openai.com](https://platform.openai.com).
2. Generiere deinen ersten API-Key.

## Teilaufgabe B:
1. Nutze Python mit der openai Bibliothek:
   - Installiere die Bibliothek mit `pip install openai`.
   - Erstelle ein kurzes Python-Skript, das über die API ein einfaches „Hello World“ mit GPT-3.5-turbo erzeugt.

```python
import openai

openai.api_key = "dein_api_key"

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Sag Hallo Welt!"}
  ]
)

print(response.choices[0].message.content)
```
