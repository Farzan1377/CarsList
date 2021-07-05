import functools
from flask import Blueprint, g, request, render_template, jsonify
from app.db import get_db


bp = Blueprint('posts', __name__, url_prefix='/posts')


@bp.route('/create_post', methods=['POST'])
def create_post():
    print(request)
    if request.method != 'POST':
        jsonify(({"error": "Did not create post. Not a POST request."}))
        return
    
    print('Attempting to create post...')
    post_request = request.form
    post_id = post_request["post_id"] if "post_id" in post_request else ""
    user_id = post_request["user_id"] if "user_id" in post_request else ""
    vehicle_id = post_request["vehicle_id"] if "vehicle_id" in post_request else ""
    price = post_request["price"] if "price" in post_request else ""
    date_created = post_request["date_created"] if "date_created" in post_request else ""
    date_expires = post_request["date_expires"] if "date_expires" in post_request else ""

    cursor = get_db().cursor()
    before_row_count = cursor.rowcount
    rows = cursor.execute("""INSERT into posts values (%s,%s,%s,%s,%s,%s)""",
                (post_id, user_id, vehicle_id, price, date_created, date_expires,))
    after_row_count = cursor.rowcount
    get_db().commit()
    cursor.close()
    if after_row_count > before_row_count:
        return jsonify({"Success": "post successfully created"})
    else:
        return jsonify(({"error": "Did not insert post"}))


@bp.route('/delete_post', methods=['DELETE'])
def delete_post():
    print(request)
    if request.method != 'DELETE':
        jsonify(({"error": "Did not delete post. Not a DELETE request."}))
        return

    post_request = request.form
    if 'post_id' not in post_request:
        return jsonify({'error': 'post_id key not specified'})

    post_id = post_request['post_id']
    if not post_id:
        return jsonify({'error': 'post_id value not specified'})

    cursor = get_db().cursor()
    rows = cursor.execute('DELETE from posts where post_id = %s', (post_id,))

    if not rows:
        return jsonify({'error': 'post_id not found'})
    return jsonify({"success": "post successfully removed"})


@bp.route('/update_post', methods=['PUT'])
def update_post():
    print(request)
    if request.method != 'PUT':
        jsonify(({"error": "Did not update post. Not a PUT request."}))
        return

    post_request = request.form
    if 'post_id' not in post_request:
        return jsonify({'error': 'post_id key not specified'})

    post_id = post_request['post_id']
    if not post_id:
        return jsonify({'error': 'post_id value not specified'})

    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM posts where post_id = %s", (post_id,))

    columns = [col[0] for col in cursor.description]
    head_rows = [dict(zip(columns, row)) for row in cursor.fetchmany(size=50)]

    price = post_request["price"] if "price" in post_request else head_rows[0]["price"]
    date_expires = post_request["date_expires"] if "date_expires" in post_request else head_rows[0]["date_expires"]

    cursor = get_db().cursor()
    rows = cursor.execute("UPDATE posts set price = %s, date_expires = %s", (price, date_expires,))
    get_db().commit()
    cursor.close()
    return jsonify({"Success": "post successfully created"})


@bp.route('/show_post', methods=['GET'])
def show_post():
    print(request)
    if request.method != 'GET':
        jsonify(({"error": "Did not show post. Not a GET request."}))
        return

    post_request = request.form
    if 'post_id' not in post_request:
        return jsonify({'error': 'post_id key not specified'})
        
    post_id = post_request['post_id']
    if not post_id:
        return jsonify({'error': 'post_id value not specified'})

    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM posts where post_id = %s", (post_id,))
    columns = [col[0] for col in cursor.description]
    head_rows = [dict(zip(columns, row)) for row in cursor.fetchmany(size=50)]

    return jsonify({"success": head_rows})