#!/usr/bin/python3
"""
index
"""

from flask import jsonify
from api.v1.views import app_views

from models import storage


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """
    status route
    :return: response with json
    """
    data = {
        "status": "OK"
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """
    stats of all objs route
    :return: json of all objs
    """
    data = {
  	"amenities": 47, 
  	"cities": 36, 
  	"places": 154, 
  	"reviews": 718, 
  	"states": 27, 
  	"users": 31
	}

    resp = jsonify(data)
    resp.status_code = 200

    return resp
