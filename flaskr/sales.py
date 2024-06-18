from flaskr import db
from flask import (
    Blueprint, jsonify, g, redirect, render_template, request, session, url_for, Flask, make_response
)
from datetime import datetime, timedelta
bp = Blueprint('sales', __name__, url_prefix='/sales')


@bp.route('sales_records', methods=['GET'])
def get_sales_records():
    
    period = request.args.get('period', 'all')
    conn = db.get_db()
    cursor = conn.cursor()
    if period == '1year':
        start_date = datetime.now() - timedelta(days=365)
    elif period == '3years':
        start_date = datetime.now() - timedelta(days=3*365)
    elif period == '5years':
        start_date = datetime.now() - timedelta(days=5*365)
    else:
        start_date = None
    
    if start_date:
        sales_records = cursor.execute('SELECT * FROM SalesRecords WHERE SaleDate >= ?', (start_date,)).fetchall()
    else:
        sales_records = cursor.execute('SELECT * FROM SalesRecords').fetchall()    
   
    result = []
    for record in sales_records:
        result.append({
            'SaleDate':record[4],
            'SalePrice':record[5], 
        })
    conn.close()
    return result

@bp.route('/users', methods=['GET'])
def get_users():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit

    conn = db.get_db()
    users = conn.cursor().execute('SELECT ID, Name, Role, Email, Phone FROM users LIMIT ? OFFSET ?', (limit, offset)).fetchall()
    users_data = []

    for user in users:
        cars = conn.cursor().execute('SELECT Model, LicensePlate FROM Cars WHERE OwnerID = ?', (user[0],)).fetchall()
        cars_data = [{'Model': car[0], 'LicensePlate': car[1]} for car in cars]
        print(cars_data)
        users_data.append({
            'UserID': user[0],
            'Name': user[1],
            'Role': user[2],
            'Email': user[3],
            'Phone': user[4],
            'Cars': cars_data
        })
    
    total_users = conn.cursor().execute('SELECT COUNT(*) FROM users').fetchone()[0]
    conn.close()

    has_more_users = (page * limit) < total_users

    response = {
        'users': users_data,
        'hasMoreUsers': has_more_users
    }

    return jsonify(response)

@bp.route('/opportunities', methods=['GET'])
def get_opportunities():
    conn = db.get_db()
    cursor = conn.cursor()
    opportunities = cursor.execute('SELECT * FROM opportunities').fetchall()
    conn.close()
    return jsonify([{'id':opportunity[0], 'name':opportunity[1], 'description':opportunity[2], 'status':opportunity[3]}for opportunity in opportunities])

@bp.route('/opportunities', methods=['POST'])
def add_opportunity():
    new_opportunity = request.json
    conn = db.get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO opportunities (name, description, status) VALUES (?, ?, ?)',
                 (new_opportunity['name'], new_opportunity['description'], new_opportunity['status']))
    conn.commit()
    conn.close()
    return jsonify(new_opportunity), 201

@bp.route('/opportunities/<int:id>', methods=['PUT'])
def update_opportunity(id):
    updated_opportunity = request.json
    conn = db.get_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE opportunities SET name = ?, description = ?, status = ? WHERE id = ?',
                 (updated_opportunity['name'], updated_opportunity['description'], updated_opportunity['status'], id))
    conn.commit()
    conn.close()
    return jsonify(updated_opportunity)

@bp.route('/opportunities/<int:id>', methods=['DELETE'])
def delete_opportunity(id):
    conn = db.get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM opportunities WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return '', 204

@bp.route('/marketing_events', methods=['POST'])
def create_marketing_event():
    new_event = request.json
    conn = db.get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO marketing_events (name, description, start_date, end_date, budget) VALUES (?, ?, ?, ?, ?)',
                 (new_event['name'], new_event['description'], new_event['start_date'], new_event['end_date'], new_event['budget']))
    conn.commit()
    conn.close()
    return jsonify(new_event), 201