import functools
from flask import Blueprint, g, request, render_template, jsonify, flash
from app.db import get_db

bp = Blueprint('search', __name__, url_prefix='/search')

SELECT_VEHICLE_BASE_QUERY = "SELECT posts.vehicle_id, posts.user_id, post_id, manufacturer, model, year, type, " \
                            "vehicle_condition, odometer, paint_color, image_url, description, price, date_created, " \
                            "date_expires, name, location, email, phone, picture " \
                            "FROM vehicles INNER JOIN posts ON posts.vehicle_id = vehicles.vehicle_id " \
                            "INNER JOIN users ON posts.user_id = users.user_id"


# Calling this endpoint requires form data (a dictionary) in the request body
# The manufacturer, price_low, and price_high keys must exist regardless of whether they have values or not
# Returns a JSON dictionary with key "data" set to a list of vehicle information made my "manufacturer" and having
# price <= "price_high" and >= "price_low"
@bp.route('/select_vehicles', methods=['GET'])
def select_vehicles():
    if request.method == 'GET':
        select_request = request.form
        cursor = get_db().cursor()
        manufacturer = select_request['manufacturer']
        price_low = select_request['price_low']
        price_high = select_request['price_high']
        if manufacturer and price_low and price_high:
            cursor.execute(SELECT_VEHICLE_BASE_QUERY + " WHERE manufacturer = '%s' AND price <= %d AND price >= %d" %
                           (manufacturer, int(price_high), int(price_low)))
        elif manufacturer:
            cursor.execute(SELECT_VEHICLE_BASE_QUERY + " WHERE manufacturer = '%s'" % manufacturer)
        elif price_low and price_high:
            cursor.execute(SELECT_VEHICLE_BASE_QUERY + " WHERE price <= %d AND price >= %d" % (int(price_high),
                                                                                               int(price_low)))
        else:
            cursor.execute(SELECT_VEHICLE_BASE_QUERY)

        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return jsonify({"data": data})


# Calling this endpoint requires form data (a dictionary) in the request body
# "manufacturer" must be present as a key in the request body, set to the manufacturer name
# Returns a JSON dictionary with key "average_price" set to the average price of the given manufacturer
# If there was an error, will return a dictionary with key "error" set to the error message
@bp.route('/get_manufacturer_average_price', methods=['GET'])
def get_manufacturer_average_price():
    if request.method == 'GET':
        get_request = request.form
        cursor = get_db().cursor()
        if 'manufacturer' not in get_request:
            return jsonify({'error': 'manufacturer not specified'})
        manufacturer = get_request['manufacturer']
        if not manufacturer:
            return jsonify({'error': 'manufacturer not specified'})
        cursor.execute("SELECT AVG(price) "
                       "FROM posts INNER JOIN vehicles ON posts.vehicle_id = vehicles.vehicle_id "
                       "GROUP BY manufacturer "
                       "HAVING manufacturer = '%s'" % manufacturer)
        rows = cursor.fetchall()
        if not rows:
            return jsonify({'error': 'manufacturer not found'})
        average_price = rows[0][0]
        return jsonify({"average_price": str(average_price)})
