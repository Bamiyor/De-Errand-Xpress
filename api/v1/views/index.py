#!/usr/bin/python3
from errand_models.errand_models import Cart, User, Product, Errand
from errand_models import storage
from flask import jsonify
from flask_apispec import doc
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

@app_views.route('/status', methods=['GET'], strict_slashes=False)
@doc(description='Status of API', tags=['Misc'])
def status():
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
@doc(description='Retrieves the number of each objects by type', tags=['Misc'])
def number_objects():
    classes = [Product, Cart, Errand, User]
    names = ["Product", "Cart", "Errand", "User"]
    
    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])
    
    return jsonify(num_objs)





"""
from errand_models.errand_models import Cart, User, Product, Errand
from errand_models import storage
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    Status of API
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    Retrieves the number of each objects by type
    classes = [Product, Cart, Errand, User]
    names = ["Product", "Cart", "Errand", "User"]
    
    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])
    
    return jsonify(num_objs)
"""