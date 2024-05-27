#!/usr/bin/python3
from errand_models.errand_models import Product
from errand_models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/products', methods=['GET'], strict_slashes=False)
@swag_from('documentation/product/all_products.yml')
def get_products():
    all_products = storage.all(Product).values()
    list_products = [product.to_dict() for product in all_products]
    return jsonify(list_products)


@app_views.route('/products/<product_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/product/get_product.yml', methods=['GET'])
def get_product(product_id):
    product = storage.get(Product, product_id)
    if not product:
        abort(404)
    return jsonify(product.to_dict())


@app_views.route('/products/<product_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/product/delete_product.yml', methods=['DELETE'])
def delete_product(product_id):
    product = storage.get(Product, product_id)
    if not product:
        abort(404)
    storage.delete(product)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/products', methods=['POST'], strict_slashes=False)
@swag_from('documentation/product/post_product.yml', methods=['POST'])
def post_product():
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'price' not in request.get_json():
        abort(400, description="Missing price")
    data = request.get_json()
    instance = Product(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/products/<product_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/product/put_product.yml', methods=['PUT'])
def put_product(product_id):
    product = storage.get(Product, product_id)
    if not product:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(product, key, value)
    storage.save()
    return make_response(jsonify(product.to_dict()), 200)
