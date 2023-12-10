#!/usr/bin/python3
""" Index view
"""
from flask import *

from api.v1.views import app_views

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return make_response(jsonify({"status": "OK"}), 200)
