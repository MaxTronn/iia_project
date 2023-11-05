from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/items/electrical')
def get_electrical_item():
    item_category = request.args.get('item_category')
    item_type = request.args.get('item_type')
    item_size = request.args.get('item_size')
    item_name = request.args.get('item_name')
    item_brand = request.args.get('item_brand')
    item_max_price = request.args.get('item_max_price')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    max_dist = request.args.get('max_dist')

    search_attributes = {}

    if item_category is not None:
        search_attributes[item_category] = '1'
    if item_type is not None:
        search_attributes['item_type'] = item_type
    if item_size is not None:
        search_attributes['item_size'] = item_size
    if item_name is not None:
        search_attributes['item_name'] = item_name
    if item_max_price is not None:
        search_attributes['item_max_price'] = item_max_price
    if item_brand is not None:
        search_attributes['item_brand'] = item_brand

    base_query = 'SELECT * FROM electrical_items WHERE '
    query = 'SELECT * FROM electrical_items WHERE '

    for key, value in search_attributes.items():
        query += key + " =?" + " AND "

    if query == base_query:
        return "No search parameters provided"

    query = query[:-5] + ";"

    # query the materialized view and get the db_names of the items
    # using db names, query global db to get store details
    conn = sqlite3.connect(
        './materialised_items_database/materialised_items.db')
    cursor = conn.execute(query, tuple(search_attributes.values()))
    result = cursor.fetchall()

    shop_details = []
    # take the store name, store id lat and long
    for item in result:
        item_category = ''

        if item[11] == 1:
            item_category += 'TVs'
        elif item[12] == 1:
            item_category += 'Laptops'
        elif item[13] == 1:
            item_category = 'Home_Appliances'
        else:
            item_category = 'Smartphones'

        shop_details.append({
            "store_name": item[1],
            "store_id": item[2],
            "store_lat": item[3],
            "store_long": item[4],
            "item_name": item[15],
            "item_category": item_category,
            "item_id": item[10],
            "item_size": item[8],
            "item_price": item[7],
            "item_brand": item[6],
            "item_type": item[5],
        })

    return shop_details


@app.route('/items/furniture')
def get_furniture_item():
    item_category = request.args.get('item_category')
    item_id = request.args.get('item_id')
    item_type = request.args.get('item_type')
    item_brand = request.args.get('item_brand')
    item_size = request.args.get('item_size')
    item_shape = request.args.get('item_shape')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    max_dist = request.args.get('max_dist')

    search_attributes = {}

    if item_category is not None:
        search_attributes['item_category'] = item_category
    if item_id is not None:
        search_attributes['item_id'] = item_id
    if item_type is not None:
        search_attributes['item_type'] = item_type
    if item_size is not None:
        search_attributes['item_size'] = item_size
    if item_brand is not None:
        search_attributes['item_name'] = item_brand
    if item_shape is not None:
        search_attributes['item_shape'] = item_shape

    base_query = 'SELECT * FROM furniture_items WHERE '
    query = 'SELECT * FROM furniture_items WHERE '

    for key, value in search_attributes.items():
        query += key + " = " + value + " AND "

    if query == base_query:
        return "No search parameters provided"

    query = query[:-5] + ";"
    # query the materialized view and get the db_names of the items
    # using db names, query global db to get store details

    # Connect to the Service_provider_global.db
    conn = sqlite3.connect('materiailization/materialized.db')
    cursor = conn.execute(query)
    cols = cursor.fetchone()


if __name__ == '__main__':
    app.run()
