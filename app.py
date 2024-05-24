#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy
from models.engine.db_storage import DBStorage
from flask import Flask, render_template, request, redirect, url_for
from errand_models.user import User
from errand_models.product import Product
from errand_models.cart import Cart
from models import storage
from errand_models.errand import Errand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://<user>:<pwd>@<host>/<db>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Initialize the database storage
storage = DBStorage()
storage.reload()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    products = storage.all(Errand)
    return render_template('products.html', products=products)

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
from flask import Flask
from flask import render_template, redirect, url_for, request
# from errand_models import product, cart, user
# from  errand_models  import Errand
from flask_sqlalchemy import SQLAlchemy
from errand_models.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Import models after creating the db instance
from errand_models import Product, Cart, User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        # Handle adding items to the cart
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        # Save the cart item to the database
        # ...
        return redirect(url_for('cart'))
    # Retrieve the cart items from the database and render the cart.html template
    cart_items = Cart.query.all()
    return render_template('cart.html', cart_items=cart_items)

if __name__ == '__main__':
    app.run(debug=True)
"""

