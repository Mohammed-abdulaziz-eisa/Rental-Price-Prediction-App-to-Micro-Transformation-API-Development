"""
Flask Application Entry Point.

This module serves as the entry point for the Flask application.

Usage:
-------
    The Flask application is created and intialized here.
    The predication blueprint is (`api.predication.bp`) registered here
    with the application.
"""

from api.predication import bp
from flask import Flask

app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)  # noqa: S201
