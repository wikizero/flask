from flask import Flask
from server.db import init_db, get_db


def create_app():
    """
    Create and configure an instance of the Flask application.
    """

    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return 'Hello, flask!'

    @app.errorhandler(404)
    def page_not_found(e):
        return 'Are you lost?', 404

    @app.errorhandler(500)
    def server_error(e):
        return "We're sorry. Something went wrong. Please try again later. The backend responded with an error!", 500

    # register the database commands
    # init_db()

    # apply the blueprints to the app
    # from flaskr import auth, blog
    # app.register_blueprint(auth.bp)
    # app.register_blueprint(blog.bp)

    return app
