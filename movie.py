# coding:utf-8
from flask import Blueprint, render_template

movie_bp = Blueprint('movie', __name__, template_folder='templates/movie')


@movie_bp.route('/')
def index():
    return 'movie index page'


@movie_bp.route('/detail')
@movie_bp.route('/detail/<int:movie_id>')
def detail(movie_id=None):
    return render_template('blog.html')

