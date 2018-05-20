# coding:utf-8
from flask import Flask, render_template
from cat import cat_bp
from movie import movie_bp

app = Flask(__name__)

app.register_blueprint(cat_bp, url_prefix='/cat')
app.register_blueprint(movie_bp, url_prefix='/movie')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', error='error code : 404'), 404


if __name__ == '__main__':
    app.run()
