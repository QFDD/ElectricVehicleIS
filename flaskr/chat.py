from flaskr.auth import login_required
from flaskr.db import get_db
from flask import (
    Blueprint, jsonify, g, redirect, render_template, request, session, url_for, Flask, make_response
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/get_message', methods=['GET'])
def get_messages():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM messages ORDER BY timestamp DESC")
    messages = cursor.fetchall()
    return jsonify(messages)

@bp.route('/post_message', methods=['POST'])
def post_message():
    db = get_db()
    user = request.json['user']
    content = request.json['content']
    cursor = db.cursor()
    cursor.execute("INSERT INTO messages (user, content) VALUES (?, ?)", (user, content))
    db.commit()
    return jsonify({'id': cursor.lastrowid, 'user': user, 'content': content, 'timestamp': 'Now'})