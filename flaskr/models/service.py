import sqlite3
from flask import current_app
from flaskr.db import get_db

def get_pending_service_records(limit=10, offset=0):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT VehicleID, Date, Description, RecordID FROM PendingServiceRecords LIMIT ? OFFSET ?", (limit, offset))
    records = cursor.fetchall()
    return records

