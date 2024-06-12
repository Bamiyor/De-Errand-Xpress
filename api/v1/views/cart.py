#!/usr/bin/python3
from errand_models.errand_models import Cart
from errand_models import storage
from flask import abort, jsonify, make_response, request
from flask_apispec import doc, use_kwargs, marshal_with
from flask_restful import Resource
from marshmallow import Schema, fields

class CartSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    product_ids = fields.List(fields.Int())
    # Add other fields as necessary

class CartResource(Resource):
    @doc(description='Get a cart by ID', tags=['Cart'])
    @marshal_with(CartSchema)
    def get(self, cart_id):
        cart = storage.get(Cart, cart_id)
        if not cart:
            abort(404)
        return cart.to_dict()

    @doc(description='Delete a cart by ID', tags=['Cart'])
    def delete(self, cart_id):
        cart = storage.get(Cart, cart_id)
        if not cart:
            abort(404)
        storage.delete(cart)
        storage.save()
        return make_response(jsonify({}), 200)

    @doc(description='Update a cart by ID', tags=['Cart'])
    @use_kwargs(CartSchema)
    @marshal_with(CartSchema)
    def put(self, cart_id):
        cart = storage.get(Cart, cart_id)
        if not cart:
            abort(404)
        if not request.get_json():
            abort(400, description="Not a JSON")
        ignore = ['id', 'created_at', 'updated_at']
        data = request.get_json()
        for key, value in data.items():
            if key not in ignore:
                setattr(cart, key, value)
        storage.save()
        return cart.to_dict()

class CartListResource(Resource):
    @doc(description='Get all carts', tags=['Cart'])
    @marshal_with(CartSchema(many=True))
    def get(self):
        all_carts = storage.all(Cart).values()
        list_carts = [cart.to_dict() for cart in all_carts]
        return list_carts

    @doc(description='Create a new cart', tags=['Cart'])
    @use_kwargs(CartSchema)
    @marshal_with(CartSchema)
    def post(self):
        if not request.get_json():
            abort(400, description="Not a JSON")
        data = request.get_json()
        instance = Cart(**data)
        instance.save()
        return instance.to_dict(), 201



"""
from errand_models.errand_models import Cart
from errand_models import storage
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from api.v1.views import app_views

@app_views.route('/carts', methods=['GET'], strict_slashes=False)
@swag_from('documentation/cart/all_carts.yml')
def get_carts():
    all_carts = storage.all(Cart).values()
    list_carts = [cart.to_dict() for cart in all_carts]
    return jsonify(list_carts)

@app_views.route('/carts/<cart_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/cart/get_cart.yml', methods=['GET'])
def get_cart(cart_id):
    cart = storage.get(Cart, cart_id)
    if not cart:
        abort(404)
    return jsonify(cart.to_dict())

@app_views.route('/carts/<cart_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/cart/delete_cart.yml', methods=['DELETE'])
def delete_cart(cart_id):
    cart = storage.get(Cart, cart_id)
    if not cart:
        abort(404)
    storage.delete(cart)
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/carts', methods=['POST'], strict_slashes=False)
@swag_from('documentation/cart/post_cart.yml', methods=['POST'])
def post_cart():
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    instance = Cart(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/carts/<cart_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/cart/put_cart.yml', methods=['PUT'])
def put_cart(cart_id):
    cart = storage.get(Cart, cart_id)
    if not cart:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['id', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(cart, key, value)
    storage.save()
    return make_response(jsonify(cart.to_dict()), 200)
"""