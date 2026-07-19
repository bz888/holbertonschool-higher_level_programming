"""Flask application for displaying products from JSON or CSV files."""

import csv
import json
from pathlib import Path

from flask import Flask, render_template, request


app = Flask(__name__)
BASE_DIR = Path(__file__).parent


def read_json_products():
    """Return the products stored in the JSON data file."""
    with (BASE_DIR / 'products.json').open(encoding='utf-8') as file:
        return json.load(file)


def read_csv_products():
    """Return the products stored in the CSV data file."""
    with (BASE_DIR / 'products.csv').open(newline='', encoding='utf-8') as file:
        return [
            {
                'id': int(product['id']),
                'name': product['name'],
                'category': product['category'],
                'price': float(product['price']),
            }
            for product in csv.DictReader(file)
        ]


@app.route('/products')
def products():
    """Display products from the requested source, optionally filtered by ID."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        product_list = read_json_products()
    elif source == 'csv':
        product_list = read_csv_products()
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        product_list = [
            product for product in product_list
            if str(product['id']) == product_id
        ]
        if not product_list:
            return render_template(
                'product_display.html', error='Product not found'
            )

    return render_template('product_display.html', products=product_list)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
