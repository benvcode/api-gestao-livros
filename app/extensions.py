# app/extensions.py

from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_extensions(app):
    db.init_app(app)