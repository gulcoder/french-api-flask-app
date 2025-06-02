# 🧘‍♀️ Mindfulness Quotes Flask App

En vacker mindfulness-applikation byggd med **Flask**, **PostgreSQL (via Docker)**, **SQLAlchemy**. Appen hämtar citat från ett API och visar dem på en stilren, interaktiv webbsida.

---

## 🌸 Funktioner

- ✅ Hämtar mindfulness-citat via [ZenQuotes API](https://zenquotes.io/)
- ✅ Sparar citaten i en PostgreSQL-databas
- ✅ Flask + SQLAlchemy backend
- ✅ Docker-stöd för databasen
- ✅ Responsiv & transparent UI med vacker blå ton

---

## 🖼️ Arkitekturöversikt

```mermaid
graph TD
    User[🧘‍♀️ Användare] -->|Klickar på nytt citat| Frontend
    Frontend[🌐 JavaScript/CSS/HTML] -->|Fetch API| FlaskApp
    FlaskApp[🐍 Flask Backend] -->|Hämtar citat| ZenQuotesAPI[(ZenQuotes API)]
    FlaskApp -->|Sparar/Läser| Database[(PostgreSQL via Docker)]

