import functools
from flask import Blueprint, g, request, render_template, jsonify
from app.db import get_db

bp = Blueprint('profile', __name__, url_prefix='/profile')


@bp.route('/get_user_vehicles', methods=['GET'])
def get_user_vehicles():
    if request.method == 'GET':
        vehicle_request = request.form
        user_id = vehicle_request['user_id']
        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM vehicles where user_id = %s",(user_id,))
        columns = [col[0] for col in cursor.description]
        print(columns)
        head_rows = [dict(zip(columns, row)) for row in cursor.fetchmany(size=50)]

        return jsonify({"vehicles": head_rows})


@bp.route('/delete_user_vehicles', methods=['DELETE'])
def delete_user_vehicle():
    vehicle_request = request.form
    vehicle_id = vehicle_request['vehicle_id']
    print(vehicle_id)
    cursor = get_db().cursor()
    cursor.execute('DELETE from vehicles where vehicle_id = %s', (vehicle_id,))
    print(cursor.rowcount)
    return jsonify({"vehicles": "done"})

@bp.route('/create_user_vehicles', methods=['POST'])
def create_user_vehicle():
    vehicle_request = request.form
    vehicle_id = vehicle_request['vehicle_id']


@bp.route('/user_posts', methods=('GET', 'POST', 'DELETE'))
def post():
    print(request)
    if request.method == 'GET':
        #user_id = request.form['user_id']
        print('Hi')
        print(request)
        cursor = get_db().cursor()
        cursor.execute(("SELECT * FROM posts"))
    elif request.method == 'POST':
        cursor = get_db().cursor()
        price = request.form['price']
        cursor.execute(("SELECT * FROM SData WHERE price <= {}".format(price)))
    elif request.method == 'DELETE':
        cursor = get_db().cursor()
        vehicle_id = request.form['vehicle_id']
        cursor.execute(('DELETE from vehicles where id =vehicle_id'))

        # Returns result as a list of dicts
    columns = [col[0] for col in cursor.description]
    head_rows = [dict(zip(columns, row)) for row in cursor.fetchmany(size=50)]

    return render_template('shop/buy.html', head_rows=head_rows)