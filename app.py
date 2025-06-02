from flask import Flask, render_template, jsonify
import requests
from database import session, Quote

app = Flask(__name__)

ZEN_QUOTES_URL = "https://zenquotes.io/api/random"

def fetch_quote():
    response = requests.get(ZEN_QUOTES_URL)
    if response.status_code == 200:
        data = response.json()
        if data:
            q = data[0]
            return q['q'], q['a']
    return None, None

@app.route('/')
def index():
    quote = session.query(Quote).order_by(Quote.id.desc()).first()
    return render_template('index.html', quote=quote)

@app.route('/new-quote')
def new_quote():
    text, author = fetch_quote()
    if text:
        # Spara i DB
        new_q = Quote(text=text, author=author)
        session.add(new_q)
        session.commit()
        return jsonify({'text': text, 'author': author})
    return jsonify({'error': 'Kunde inte hämta citat'}), 500

if __name__ == "__main__":
    app.run(debug=True)
