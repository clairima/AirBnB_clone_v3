#!/usr/bin/python3
"""
API for our application
"""
from flask import (Flask, jsonify, make_response)
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import environ
app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_conn(self):
    """
    close the current connection
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """json 404 page"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = environ.get('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
