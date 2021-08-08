import functools
from flask import Blueprint, g, request, render_template, jsonify, flash
from app.db import get_db

bp = Blueprint('search', __name__, url_prefix='/search')

SELECT_VEHICLE_BASE_QUERY = "SELECT posts.vehicle_id, posts.user_id, post_id, manufacturer, model, year, type, " \
                            "vehicle_condition, odometer, paint_color, image_url, description, price, date_created, " \
                            "date_expires, name, location, email, phone, picture " \
                            "FROM vehicles INNER JOIN posts ON posts.vehicle_id = vehicles.vehicle_id " \
                            "INNER JOIN users ON posts.user_id = users.user_id"


@bp.route('/select_vehicles', methods=['GET'])
def select_vehicles():
    if request.method == 'GET':
        cursor = get_db().cursor()
        manufacturer = request.args.get('manufacturer')
        price_low = request.args.get('price_low')
        price_high = request.args.get('price_high')
        if manufacturer and price_low and price_high:
            cursor.execute(SELECT_VEHICLE_BASE_QUERY + " WHERE manufacturer = '%s' AND price <= %d AND price >= %d" % (manufacturer, int(price_high), int(price_low)))
        elif manufacturer:
            cursor.execute(SELECT_VEHICLE_BASE_QUERY + " WHERE manufacturer = '%s'" % manufacturer)
        elif price_low and price_high:
            cursor.execute(SELECT_VEHICLE_BASE_QUERY + " WHERE price <= %d AND price >= %d" % (int(price_high), int(price_low)))
        else:
            cursor.execute(SELECT_VEHICLE_BASE_QUERY)

        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return jsonify({"data": data})


@bp.route('/get_manufacturer_average_price', methods=['GET'])
def get_manufacturer_average_price():
    if request.method == 'GET':
        get_request = request.form
        manufacturer = request.args.get('manufacturer')
        if not manufacturer:
            return jsonify({'error': 'manufacturer not specified'})
        cursor = get_db().cursor()
        cursor.execute("SELECT AVG(price) "
                       "FROM posts INNER JOIN vehicles ON posts.vehicle_id = vehicles.vehicle_id "
                       "GROUP BY manufacturer "
                       "HAVING manufacturer = '%s'" % manufacturer)
        rows = cursor.fetchall()
        if not rows:
            return jsonify({'error': 'manufacturer not found'})
        average_price = rows[0][0]
        return jsonify({"average_price": str(average_price)})


@bp.after_request
def apply_allow_origin(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response