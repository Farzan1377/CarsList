import functools
from flask import Blueprint, g, request, render_template, jsonify
from app.db import get_db

bp = Blueprint('profile', __name__, url_prefix='/profile')


@bp.route('/get_user_vehicles', methods=['GET'])
def get_user_vehicles():
    if request.method == 'GET':
        vehicle_request = request.form
        if 'user_id' not in vehicle_request:
            return jsonify({'error': 'user_id key not specified'})
        user_id = vehicle_request['user_id']
        if not user_id:
            return jsonify({'error': 'user_id value not specified'})
        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM vehicles where user_id = %s", (user_id,))
        columns = [col[0] for col in cursor.description]
        print(columns)
        head_rows = [dict(zip(columns, row)) for row in cursor.fetchmany(size=50)]

        return jsonify({"success": head_rows})


@bp.route('/delete_user_vehicles', methods=['DELETE'])
def delete_user_vehicle():
    vehicle_request = request.form
    if 'vehicle_id' not in vehicle_request:
        return jsonify({'error': 'vehicle_id key not specified'})

    vehicle_id = vehicle_request['vehicle_id']
    if not vehicle_id:
        return jsonify({'error': 'vehicle_id value not specified'})

    cursor = get_db().cursor()
    rows = cursor.execute('DELETE from vehicles where vehicle_id = %s', (vehicle_id,))

    if not rows:
        return jsonify({'error': 'vehicle_id not found'})
    return jsonify({"success": "vehicle successfully removed"})


@bp.route('/create_user_vehicles', methods=['POST'])
def create_user_vehicle():
    vehicle_request = request.form
    query_string = ""
    if "vehicle_id" in vehicle_request:
        vehicle_id = vehicle_request["vehicle_id"]
    else:
        vehicle_id = ""
    if "user_id" in vehicle_request:
        user_id = vehicle_request["user_id"]
    else:
        user_id = ""
    if "manufacturer" in vehicle_request:
        manufacturer = vehicle_request["manufacturer"]
    else:
        manufacturer =""
    if "model" in vehicle_request:
        model = vehicle_request["model"]
    else:
        model =""
    if "year" in vehicle_request:
        year = int(vehicle_request["year"])
    else:
        year =""
    if "type" in vehicle_request:
        vehicle_type = vehicle_request["type"]
    else:
        vehicle_type =""
    if "vehicle_condition" in vehicle_request:
        vehicle_condition = vehicle_request["vehicle_condition"]
    else:
        vehicle_condition =""
    if "odometer" in vehicle_request:
        odometer = int(vehicle_request["odometer"])
    else:
        odometer =""
    if "paint_color" in vehicle_request:
        paint_color = vehicle_request["paint_color"]
    else:
        paint_color =""
    if "image_url" in vehicle_request:
        image_url = vehicle_request["image_url"]
    else:
        image_url =""
    if "description" in vehicle_request:
        description = vehicle_request["description"]
    else:
        description =""
    print((vehicle_id,user_id,manufacturer, model,year, vehicle_type,
                    vehicle_condition,odometer, paint_color, image_url, description,))
    cursor = get_db().cursor()
    before_row_count = cursor.rowcount
    rows = cursor.execute("""INSERT into vehicles values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                   (vehicle_id,user_id,manufacturer, model,year, vehicle_type,
                    vehicle_condition,odometer, paint_color, image_url, description,))
    after_row_count = cursor.rowcount
    get_db().commit()
    cursor.close()
    if after_row_count > before_row_count:
        return jsonify({"Success": "vehicle successfully created"})
    else:
        return jsonify(({"error": "Did not insert vehicle"}))


@bp.route('/user_posts', methods=('GET', 'POST', 'DELETE'))
def post():
    print(request)
    if request.method == 'GET':
        # user_id = request.form['user_id']
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
