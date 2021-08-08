import functools
from flask import Blueprint, g, request, render_template, jsonify
from app.db import get_db

bp = Blueprint('vehicles', __name__, url_prefix='/vehicles')


@bp.route('/get_vehicle', methods=['GET'])
def get_vehicle():
    if request.method == 'GET':
        vehicle_id = request.args.get('vehicle_id')
        if not vehicle_id:
            return jsonify({'error': 'vehicle_id value not specified'})
        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM vehicles where vehicle_id = %s", (vehicle_id,))
        columns = [col[0] for col in cursor.description]
        head_rows = [dict(zip(columns, row)) for row in cursor.fetchmany(size=50)]

        return jsonify({"success": head_rows})


@bp.route('/get_user_vehicles', methods=['GET'])
def get_user_vehicles():
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        if not user_id:
            return jsonify({'error': 'user_id value not specified'})
        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM vehicles where user_id = %s", (user_id,))
        columns = [col[0] for col in cursor.description]
        head_rows = [dict(zip(columns, row)) for row in cursor.fetchmany(size=50)]

        return jsonify({"success": head_rows})


@bp.route('/delete_user_vehicles', methods=['GET'])
def delete_user_vehicle():
    vehicle_id = request.args.get('vehicle_id')
    if not vehicle_id:
        return jsonify({'error': 'vehicle_id value not specified'})
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE from vehicles where vehicle_id = %s', (vehicle_id,))
    db.commit()
    return jsonify({"success": "vehicle(s) successfully removed"})
    


@bp.route('/create_user_vehicles', methods=['POST'])
def create_user_vehicle():
    vehicle_request = request.args
    print("vehicle_request: ", vehicle_request)
    query_string = ""
    if "vehicle_id" in vehicle_request:
        vehicle_id = vehicle_request["vehicle_id"]
    else:
        return jsonify(({"error": "vehicle_id is NULL"}))
    if "user_id" in vehicle_request:
        user_id = vehicle_request["user_id"]
    else:
        return jsonify(({"error": "user_id is NULL"}))
    if "manufacturer" in vehicle_request:
        manufacturer = vehicle_request["manufacturer"]
    else:
        manufacturer = None
    if "model" in vehicle_request:
        model = vehicle_request["model"]
    else:
        model = None
    if "year" in vehicle_request:
        year = int(vehicle_request["year"])
    else:
        year = None
    if "type" in vehicle_request:
        vehicle_type = vehicle_request["type"]
    else:
        vehicle_type = None
    if "vehicle_condition" in vehicle_request:
        vehicle_condition = vehicle_request["vehicle_condition"]
    else:
        vehicle_condition = None
    if "odometer" in vehicle_request:
        odometer = int(vehicle_request["odometer"])
    else:
        odometer = None
    if "paint_color" in vehicle_request:
        paint_color = vehicle_request["paint_color"]
    else:
        paint_color = None
    if "image_url" in vehicle_request:
        image_url = vehicle_request["image_url"]
    else:
        image_url = None
    if "description" in vehicle_request:
        description = vehicle_request["description"]
    else:
        description = None
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
        return jsonify(({"error": "Could not insert vehicle"}))


@bp.route('/update_user_vehicles', methods=['PUT'])
def update_user_vehicle():
    vehicle_request = request.form
    vehicle_id = vehicle_request["vehicle_id"]
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM vehicles where vehicle_id = %s", (vehicle_id,))
    columns = [col[0] for col in cursor.description]
    head_rows = [dict(zip(columns, row)) for row in cursor.fetchmany(size=50)]
    if "manufacturer" in vehicle_request:
        manufacturer = vehicle_request["manufacturer"]
    else:
        manufacturer = head_rows[0]["manufacturer"]
    if "model" in vehicle_request:
        model = vehicle_request["model"]
    else:
        model = head_rows[0]["model"]
    if "year" in vehicle_request:
        year = int(vehicle_request["year"])
    else:
        year = head_rows[0]["year"]
    if "type" in vehicle_request:
        vehicle_type = vehicle_request["type"]
    else:
        vehicle_type = head_rows[0]["year"]
    if "vehicle_condition" in vehicle_request:
        vehicle_condition = vehicle_request["vehicle_condition"]
    else:
        vehicle_condition = head_rows[0]["vehicle_condition"]
    if "odometer" in vehicle_request:
        odometer = int(vehicle_request["odometer"])
    else:
        odometer = head_rows[0]["odometer"]
    if "paint_color" in vehicle_request:
        paint_color = vehicle_request["paint_color"]
    else:
        paint_color = head_rows[0]["paint_color"]
    if "image_url" in vehicle_request:
        image_url = vehicle_request["image_url"]
    else:
        image_url = head_rows[0]["image_url"]
    if "description" in vehicle_request:
        description = vehicle_request["description"]
    else:
        description = head_rows[0]["description"]

    cursor = get_db().cursor()
    rows = cursor.execute("UPDATE vehicles set manufacturer = %s, model = %s,year=%s, type = %s, vehicle_condition= %s,"
                          "odometer = %s, paint_color = %s, image_url= %s, description = %s where "
                          "vehicle_id = %s", (manufacturer, model,year, vehicle_type,
                    vehicle_condition,odometer, paint_color, image_url, description,vehicle_id,))
    get_db().commit()
    cursor.close()
    return jsonify({"Success": "vehicle successfully updated"})


@bp.route('/user_posts', methods=['GET', 'POST', 'DELETE'])
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

    try:        
        limit = int(request.args.get('limit'))
    except:
        limit = 50

        # Returns result as a list of dicts
    columns = [col[0] for col in cursor.description]
    head_rows = [dict(zip(columns, row)) for row in cursor.fetchmany(size=limit)]

    return render_template('shop/buy.html', head_rows=head_rows)


@bp.route('/recent_vehicles', methods=['GET'])
def recent_vehicles():
    if request.method != 'GET':
        return jsonify(({"error": "Did not get vehicles. Not a GET request."}))
    
    try:
        start_index = int(request.args.get('start_index'))
    except:
        start_index = 1

    try:
        end_index = int(request.args.get('end_index'))
    except:
        end_index = 50

    cursor = get_db().cursor()
    cursor.execute(("SELECT * FROM vehicles ORDER BY vehicle_id DESC LIMIT %s,%s"), 
        (start_index-1, end_index-start_index+1,))
    columns = [col[0] for col in cursor.description]
    head_rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return jsonify({"success": head_rows})


@bp.after_request
def apply_allow_origin(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response