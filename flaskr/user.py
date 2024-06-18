from flaskr import db
from flask import (
    Blueprint, jsonify, g, redirect, render_template, request, session, url_for, Flask, make_response
)
bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    service_type = data['serviceType']
    appointment_date = data['appointmentDate']
    vehicle_info = data['vehicleInfo']
    description = data['description']
    
    try:
        conn = db.get_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO PendingServiceRecords (ServiceType, Date, Description, VehicleID)
            VALUES (?, ?, ?, ?)
        ''', (service_type, appointment_date, description, vehicle_info))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success', 'message': 'Appointment created successfully!'}), 201
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Failed to create appointment.'}), 500
    
@bp.route('/change_password', methods=['POST'])
def change_password():
    data = request.json
    current_password = data['currentPassword']
    new_password = data['newPassword']
    user_id = data['user_id']

    conn = db.get_db()
    user = conn.cursor().execute('SELECT * FROM Users WHERE ID = ?', (user_id,)).fetchone()

    if user is None:
        return jsonify({'message': '用户不存在'}), 404

    if user[5] != current_password:
        return jsonify({'message': '当前密码不正确'}), 400

    conn.execute('UPDATE Users SET password = ? WHERE ID = ?', (new_password, user_id))
    conn.commit()
    conn.close()

    return jsonify({'message': '密码已成功更新'}), 200