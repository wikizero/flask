# coding:utf-8
from flask import Blueprint

cat_bp = Blueprint('cat', __name__, template_folder='templates/cat')


@cat_bp.route('/')
def index():
    return 'cat index page'


@cat_bp.route('/detail')
@cat_bp.route('/detail/<int:cat_id>')
def detail(cat_id=None):
    return 'cat detail {cat_id}'.format(cat_id=cat_id)

