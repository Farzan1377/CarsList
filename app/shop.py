import functools
from flask import Blueprint, g, request, render_template
from app.db import get_db

bp = Blueprint('shop', __name__, url_prefix='/shop')


@bp.route('/buy', methods=('GET', 'POST'))
def buy():
    if request.method == 'GET':
        cursor = get_db().cursor()
        cursor.execute(("SELECT * FROM SData")) 
    elif request.method == 'POST':
        cursor = get_db().cursor()
        price = request.form['price']
        cursor.execute(("SELECT * FROM SData WHERE price <= {}".format(price))) 

    # Returns result as a list of dicts
    columns = [col[0] for col in cursor.description]
    head_rows = [dict(zip(columns, row)) for row in cursor.fetchmany(size=50)]

    return render_template('shop/buy.html', head_rows=head_rows)


@bp.after_request
def apply_allow_origin(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response