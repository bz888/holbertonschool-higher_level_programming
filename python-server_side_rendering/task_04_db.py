"""Flask application for displaying products from JSON, CSV, or SQLite."""

import csv
import json
import sqlite3
from pathlib import Path

from flask import Flask, render_template, request


app = Flask(__name__)
BASE_DIR = Path(__file__).parent
DATABASE = BASE_DIR / 'products.db'


def create_database():
    """Create the products database and populate its initial records."""
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
            '''
        )
        cursor.executemany(
            '''
            INSERT OR IGNORE INTO Products (id, name, category, price)
            VALUES (?, ?, ?, ?)
            ''',
            [
                (1, 'Laptop', 'Electronics', 799.99),
                (2, 'Coffee Mug', 'Home Goods', 15.99),
            ],
        )


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


def read_sql_products():
    """Return products stored in the SQLite database as dictionaries."""
    with sqlite3.connect(DATABASE) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            'SELECT id, name, category, price FROM Products'
        ).fetchall()
    return [dict(row) for row in rows]


@app.route('/products')
def products():
    """Display products from the requested source, optionally filtered by ID."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            product_list = read_json_products()
        elif source == 'csv':
            product_list = read_csv_products()
        elif source == 'sql':
            product_list = read_sql_products()
        else:
            return render_template('product_display.html', error='Wrong source')
    except sqlite3.Error:
        return render_template('product_display.html', error='Database error')

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
    create_database()
    app.run(debug=True, port=8000)
