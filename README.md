# 🇫🇷 French Words Web App (Flask + SQLite + API)

Ett enkelt Python-projekt som hämtar franska meningar från ett API, sparar till SQLite med SQLAlchemy, och visar datan i en webbsida via Flask.

## 🚀 Funktioner

- Hämtar franska meningar från [LibreTranslate](https://libretranslate.com/)
- Sparar meningar till SQLite-databas
- Webbsida med Flask som visar innehållet
- Kod uppdelad i moduler (`api.py`, `models.py`, `views.py`)
- Valfritt: använd Docker för att köra databasen
```mermaid
flowchart TD
    A[Start: Flask App startas] --> B[Läs data från API]
    B --> C[Spara data i SQLite med SQLAlchemy]
    C --> D1[Visa data på webbsida med Flask]
    C --> D2[Exportera till Excel med Pandas]
    D1 --> E1[Användare ser franska ord i webbläsaren]
    D2 --> E2[Excel-fil sparas som french_words.xlsx]
```

## 🧰 Installation

```bash
git clone https://github.com/gulcoder/french-api-flask-app.git
cd french-api-flask-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Användning
```bash
python main.py
```
Besök http://127.0.0.1:5000 i webbläsaren.

## 🧪 Exempel Data

| ID | French Word       | English Translation | Part of Speech |
|----|-------------------|---------------------|----------------|
| 1  | bonjour           | hello               | interjection   |
| 2  | chat              | cat                 | noun           |
| 3  | merci             | thank you           | expression     |
| 4  | apprendre         | to learn            | verb           |
| 5  | fromage           | cheese              | noun           |

