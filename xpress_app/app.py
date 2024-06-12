#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from errand_models.engine.db_store import DBStorage
from errand_models.engine.errand_file_store import FileStorage
from errand_models.errand_models import Cart, Product, User
from errand_models.errand_models import Errand
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.static_folder = 'static'
app.template_folder = 'templates'  # Ensure correct folder name

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize the database storage
storage_type = os.getenv('EXPRESS_TYPE_STORAGE', 'file')
if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product')
def product():
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
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, subtotal=subtotal)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        new_user = User(username=username, password=password, email=email)
        storage.new(new_user)
        storage.save()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = storage.get_user_by_credentials(username, password)
        if user:
            return redirect(url_for('index'))
        else:
            return "Login Failed"
    return render_template('login.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        card_number = request.form['card_number']
        expiration_date = request.form['expiration_date']
        cvv = request.form['cvv']
        # Process payment logic here
        return redirect(url_for('index'))
    return render_template('payment.html')

if __name__ == '__main__':
    app.run(debug=True)
