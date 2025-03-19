#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)
    
def csv_file(filepath):
    products = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
        return products

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data  = json.load(file)
    list = data.get('items', [])
    return render_template('items.html', list=list)

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id', type=int)
    
    if source == 'json':
        products = json_file('products.json')
    elif source == 'csv':
        products = csv_file('products.csv')
    else:
        return render_template('product_display.html', message="Wrong source")
    
    if id:
        products = [product for product in products if product['id'] == id]
        if not products:
            return render_template('product_display.html', message="Product not found")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)