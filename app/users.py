import functools
from flask import Blueprint, g, request, render_template, jsonify
from app.db import get_db


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/get_user_info', methods=['GET'])
def get_user_info():
    if request.method != 'GET':
        jsonify(({"error": "Did not get user info. Not a GET request."}))
        return

    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id value not specified'})

    try:
        limit = int(request.args.get('limit'))
    except:
        limit = 1

    cursor = get_db().cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
    columns = [col[0] for col in cursor.description]
    head_rows = [dict(zip(columns, row)) for row in cursor.fetchmany(size=limit)]

    return jsonify({"success": head_rows})


@bp.after_request
def apply_allow_origin(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response