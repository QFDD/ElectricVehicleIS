from flask import Blueprint, jsonify, request
from flaskr.models.service import get_pending_service_records
from flaskr.db import get_db
api_bp = Blueprint('api', __name__)

@api_bp.route('/get_pending_services', methods=['POST'])
def get_pending_services():
    data = request.json
    user_id = data.get('userID')

    if user_id is None:
        return jsonify({"error": "UserID is required"}), 400

    conn = get_db()
    
    # 查找VehicleID
    vehicle = conn.execute('SELECT VehicleID FROM Cars WHERE OwnerID = ?', (user_id,)).fetchone()
    
    if vehicle is None:
        conn.close()
        return jsonify({"error": "UserID not found"}), 404

    vehicle_id = vehicle[0]
    
    # 查找PendingServiceRecords
    records = conn.execute('SELECT * FROM PendingServiceRecords WHERE VehicleID = ?', (vehicle_id,)).fetchall()
    conn.close()
    
    result = []
    for record in records:
        result.append({'serviceType':record[2],'date':record[3],'description':record[4]})

    return jsonify(result), 200

@api_bp.route('submit_processed_records', methods=['POST'])
def create_processed_record():
    data = request.json
    print("Received data:", data) 
    vehicle_license = data['vehicleLicense'] 
    service_type = data['serviceType']
    cost = data['cost']
    description = data['description']
    repair_staff_id = data['repairStaffId']
    date = data['date']

    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT VehicleID FROM Cars WHERE LicensePlate = ? OR VIN = ?', (vehicle_license, vehicle_license))
        vehicle = cursor.fetchone()
        if vehicle is None:
            return jsonify({'status': 'error', 'message': 'Vehicle not found'}), 404
        vehicle_id = vehicle[0]
        
        cursor.execute('''
            INSERT INTO ProcessedServiceRecords (VehicleID, ServiceStaffID, ServiceType, Date, Description, Cost)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (vehicle_id, repair_staff_id, service_type, date, description, cost))
        
        # 删除未处理记录表中的记录
        cursor.execute('DELETE FROM PendingServiceRecords WHERE VehicleID = ?', (vehicle_id,))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success', 'message': 'Processed record created successfully!'}), 201
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'status': 'error', 'message': 'Failed to create processed record.'}), 500
    
@api_bp.route('/parts', methods=['GET'])
def get_parts():
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)
    offset = (page - 1) * limit
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Parts LIMIT ? OFFSET ?", (limit, offset))
    parts = cursor.fetchall()
    conn.close()
    result = []
    for part in parts:
        result.append({
            'PartID':part[0],
            'Name':part[1], 
            'VehicleModel':part[2], 
            'StockQuantity':part[3]
        })
    return jsonify(result)

@api_bp.route('/pending_services', methods=['GET'])
def pending_services():
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)
    offset = (page - 1) * limit
    print(page)
    records = get_pending_service_records(limit, offset)
    result = []
    for record in records:
        result.append({
            'RecordID': record[3],
            'VehicleID': record[0],
            'Date': record[1],
            'Description': record[2]
        })
    return jsonify(result)

@api_bp.route('/processed_services', methods=['GET'])
def processed_services():
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)
    offset = (page - 1) * limit
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT VehicleID, Date, Description, ID FROM ProcessedServiceRecords LIMIT ? OFFSET ?", (limit, offset))
    records = cursor.fetchall()
    result = []
    for record in records:
        result.append({
            'RecordID': record[3],
            'VehicleID': record[0],
            'Date': record[1],
            'Description': record[2]
        })
    return jsonify(result)

@api_bp.route('/total_records', methods=['GET'])
def total_records():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM PendingServiceRecords")
    total_records = cursor.fetchone()[0]
    return jsonify({'total_records': total_records})

@api_bp.route('/processed_total_records', methods=['GET'])
def processed_total_records():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM ProcessedServiceRecords")
    total_records = cursor.fetchone()[0]
    return jsonify({'total_records': total_records})

@api_bp.route('/pending_service_records/<int:record_id>', methods=['GET'])
def get_pending_service_record(record_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT 
            PendingServiceRecords.RecordID, PendingServiceRecords.ServiceType, PendingServiceRecords.Date, PendingServiceRecords.Description,
            Cars.Model, Cars.LicensePlate, Cars.VIN, Cars.PurchaseDate,
            Users.Name, Users.Role, Users.Email, Users.Phone
        FROM PendingServiceRecords
        JOIN Cars ON PendingServiceRecords.VehicleID = Cars.VehicleID
        JOIN Users ON Cars.OwnerID = Users.ID
        WHERE PendingServiceRecords.RecordID = ?
    ''', (record_id,))
    record = cursor.fetchone()
    if record:
        result = {
            'record': {
                'RecordID': record[0],
                'ServiceType': record[1],
                'Date': record[2],
                'Description': record[3]
            },
            'vehicle': {
                'Model': record[4],
                'LicensePlate': record[5],
                'VIN': record[6],
                'PurchaseDate': record[7]
            },
            'user': {
                'Name': record[8],
                'Role': record[9],
                'Email': record[10],
                'Phone': record[11]
            }
        }
        
        return jsonify(result)
    else:
        return jsonify({'error': 'Record not found'}), 404