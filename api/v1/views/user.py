<<<<<<< HEAD
#!/usr/bin/python3
from flask import request, abort, jsonify, make_response
from flask_apispec import doc, use_kwargs, marshal_with
from flask_restful import Resource
from bcrypt import hashpw, gensalt
from errand_models.errand_models import User
from errand_models import storage
from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    # Add other fields as necessary

class UserResource(Resource):
    @doc(description='Get a user by ID', tags=['User'])
    @marshal_with(UserSchema)
    def get(self, user_id):
        user = storage.get(User, user_id)
        if not user:
            abort(404)
        return user

    @doc(description='Delete a user by ID', tags=['User'])
    def delete(self, user_id):
        user = storage.get(User, user_id)
        if not user:
            abort(404)
        storage.delete(user)
        storage.save()
        return make_response(jsonify({}), 200)

    @doc(description='Update a user by ID', tags=['User'])
    @use_kwargs(UserSchema)
    @marshal_with(UserSchema)
    def put(self, user_id):
        user = storage.get(User, user_id)
        if not user:
            abort(404)
        if not request.get_json():
            abort(400, description="Not a JSON")
        ignore = ['id', 'created_at', 'updated_at']
        data = request.get_json()
        for key, value in data.items():
            if key not in ignore:
                setattr(user, key, value)
        storage.save()
        return user

class UserListResource(Resource):
    @doc(description='Get all users', tags=['User'])
    @marshal_with(UserSchema(many=True))
    def get(self):
        all_users = storage.all(User).values()
        return list(all_users)

    @doc(description='Create a new user', tags=['User'])
    @use_kwargs(UserSchema)
    @marshal_with(UserSchema)
    def post(self):
        if not request.get_json():
            abort(400, description="Not a JSON")
        if 'email' not in request.get_json():
            abort(400, description="Missing email")
        if 'password' not in request.get_json():
            abort(400, description="Missing password")
        data = request.get_json()
        data['password'] = hashpw(data['password'].encode('utf-8'), gensalt())
        instance = User(**data)
        storage.new(instance)
        storage.save()
        return instance, 201







"""
from flask import request, abort, jsonify, make_response
from flask_restful import Resource
from bcrypt import hashpw, gensalt
# from api.v1.app import db
=======
!/usr/bin/python3
>>>>>>> refs/remotes/origin/master
from errand_models.errand_models import User
from errand_models import storage
from api.v1.views import app_views
from flasgger.utils import swag_from

class UserResource(Resource):
    @swag_from('documentation/user/get_user.yml')
    def get(self, user_id):
        user = storage.get(User, user_id)
        if not user:
            abort(404)
        return jsonify(user.to_dict())

    @swag_from('documentation/user/delete_user.yml')
    def delete(self, user_id):
        user = storage.get(User, user_id)
        if not user:
            abort(404)
        storage.delete(user)
        storage.save()
        return make_response(jsonify({}), 200)

    @swag_from('documentation/user/put_user.yml')
    def put(self, user_id):
        user = storage.get(User, user_id)
        if not user:
            abort(404)
        if not request.get_json():
            abort(400, description="Not a JSON")
        ignore = ['id', 'created_at', 'updated_at']
        data = request.get_json()
        for key, value in data.items():
            if key not in ignore:
                setattr(user, key, value)
        storage.save()
        return make_response(jsonify(user.to_dict()), 200)

class UserListResource(Resource):
    @swag_from('documentation/user/all_users.yml')
    def get(self):
        all_users = storage.all(User).values()
        list_users = [user.to_dict() for user in all_users]
        return jsonify(list_users)

    @swag_from('documentation/user/post_user.yml')
    def post(self):
        if not request.get_json():
            abort(400, description="Not a JSON")
        if 'email' not in request.get_json():
            abort(400, description="Missing email")
        if 'password' not in request.get_json():
            abort(400, description="Missing password")
        data = request.get_json()
        data['password'] = hashpw(data['password'].encode('utf-8'), gensalt())
        instance = User(**data)
        storage.new(instance)
        storage.save()
        return make_response(jsonify(instance.to_dict()), 201)
"""