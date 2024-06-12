#!/usr/bin/python3
from flask import Flask
from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)
CORS(app)
app.register_blueprint(app_views)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
