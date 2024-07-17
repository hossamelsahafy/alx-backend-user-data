#!/usr/bin/env python3
"""
    Basic Flask app
"""
from flask import Flask, url_for, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def basic():
    """Basic Flask App Function"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
