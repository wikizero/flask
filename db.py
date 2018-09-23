from flask import g, current_app
from flask_pymongo import PyMongo


def get_db():
    if not hasattr(g, 'db'):
        current_app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/test'
        g.db = PyMongo(current_app)

    return g.db


def init_db():
    get_db()
    pass
