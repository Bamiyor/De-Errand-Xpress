#!/usr/bin/python3

from flask import Flask
from flask_restful import Api
from flask_apispec import FlaskApiSpec
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config.update({
    'APISPEC_SPEC': 'apispec.ext.marshmallow',
    'APISPEC_SWAGGER_URL': '/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/',
})

CORS(app)
api = Api(app)
docs = FlaskApiSpec(app)

from api.v1.views.user import UserResource, UserListResource
from api.v1.views.product import ProductResource, ProductListResource
from api.v1.views.cart import CartResource, CartListResource
from api.v1.views.index import status, number_objects

# Register resources
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserListResource, '/users')
api.add_resource(ProductResource, '/products/<int:product_id>')
api.add_resource(ProductListResource, '/products')
api.add_resource(CartResource, '/carts/<int:cart_id>')
api.add_resource(CartListResource, '/carts')

# Register docs
docs.register(UserResource)
docs.register(UserListResource)
docs.register(ProductResource)
docs.register(ProductListResource)
docs.register(CartResource)
docs.register(CartListResource)
docs.register(status)
docs.register(number_objects)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)




"""
from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from flask_cors import CORS
from errand_models.engine.errand_file_store import FileStorage
from api.v1.views.user import UserResource, UserListResource
from api.v1.views.product import ProductResource, ProductListResource
from api.v1.views.cart import CartResource, CartListResource
from errand_models.errand_models import User, Product, Cart
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
swagger = Swagger(app)
CORS(app)
api = Api(app)

storage = FileStorage()
storage.reload()

# Register resources
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserListResource, '/users')
api.add_resource(ProductResource, '/products/<int:product_id>')
api.add_resource(ProductListResource, '/products')
api.add_resource(CartResource, '/carts/<cart_id>')
api.add_resource(CartListResource, '/carts')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
"""
