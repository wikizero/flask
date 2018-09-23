from flask import Flask, jsonify
# from blog.db import init_db, get_db


def create_app():
    """
    Create and configure an instance of the Flask application.
    """

    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return 'Hello, flask!'
        # db = get_db()
        # return jsonify({'msg': list(db.db.test.find({}))})

    @app.errorhandler(404)
    def hello():
        return 'Are you lost?'

    @app.errorhandler(500)
    def hello():
        return "We're sorry. Something went wrong. Please try again later. The backend responded with an error!"

    # register the database commands
    # init_db()

    # apply the blueprints to the app
    # from flaskr import auth, blog
    # app.register_blueprint(auth.bp)
    # app.register_blueprint(blog.bp)

    return app
