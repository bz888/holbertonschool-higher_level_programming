"""Flask application that renders a JSON-backed items list."""

import json
from pathlib import Path

from flask import Flask, render_template


app = Flask(__name__)
DATA_FILE = Path(__file__).with_name("items.json")


@app.route('/items')
def items():
    """Render the list of items stored in ``items.json``."""
    with DATA_FILE.open(encoding='utf-8') as file:
        data = json.load(file)

    return render_template('items.html', items=data.get('items', []))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
