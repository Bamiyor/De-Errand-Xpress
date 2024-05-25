#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from errand_models.engine.db_store import DBStorage
from errand_models.errand_models import Cart, Product  # Adjusted import path
from errand_models.errand_models import User, Errand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://<user>:<pwd>@<host>/<db>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Initialize the database storage
storage = DBStorage()
storage.reload()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product')
def products():
    products = storage.all(Product)
    return render_template('product.html', products=products)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        # Handle adding items to the cart
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        user_id = request.form['user_id']
        cart_item = Cart(user_id=user_id, product_id=product_id, quantity=quantity)
        storage.new(cart_item)
        storage.save()
        return redirect(url_for('cart'))
    # Retrieve the cart items from the database and render the cart.html template
    cart_items = storage.all(Cart)
    return render_template('cart.html', cart_items=cart_items)

if __name__ == '__main__':
    app.run(debug=True)

"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
from errand_models.engine.db_store import DBStorage
from errand_models import Cart, Product, User, Errand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://<user>:<pwd>@<host>/<db>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Initialize the database storage
storage = DBStorage()
storage.reload()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product')
def products():
    products = storage.all(Product)
    return render_template('product.html', products=products)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        user_id = request.form['user_id']
        cart_item = Cart(user_id=user_id, product_id=product_id, quantity=quantity)
        storage.new(cart_item)
        storage.save()
        return redirect(url_for('cart'))
    cart_items = storage.all(Cart)
    return render_template('cart.html', cart_items=cart_items)

if __name__ == '__main__':
    app.run(debug=True)
"""
