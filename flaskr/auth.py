import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask, make_response
)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import BadRequest
from flaskr.db import get_db
from flask import session
from flask_cors import CORS, cross_origin
from flask.json import jsonify

bp = Blueprint('auth', __name__, url_prefix='/auth')

bp.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db()
    cursor = conn.cursor()
    user = cursor.execute('SELECT * FROM Users WHERE id = ?', (user_id,)).fetchone()
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({
        'name': user[1],
        'contact': user[4]
    })

@bp.route('/user/<int:user_id>/update_contact', methods=['POST'])
def update_contact(user_id):
    new_contact = request.json.get('contact')
    if not new_contact:
        return jsonify({'error': 'Invalid input'}), 400
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Users SET contact = ? WHERE id = ?', (new_contact, user_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Contact updated successfully'})

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')
    phone = data.get('phone')

    if not name or not email or not password or not role or not phone:
        return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400

    conn = get_db()
    conn.cursor().execute('INSERT INTO Users (name, email, password, role, phone) VALUES (?, ?, ?, ?, ?)',
                 (name, email, password, role, phone))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success', 'message': 'User registered successfully'}), 201

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        data = request.get_json()
        email=data['email']
        password = data['password']
        con = get_db()
        cur = con.cursor()
        error = None
        user = cur.execute(
            'SELECT * FROM Users WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Incorrect email.'
        elif user[5] != password:
            error = 'Incorrect password.'
        
        if error is None:
            user_type = user[2]
            user_id = user[0]
            response = {'status': "success", 'user_type': user_type, 'user_id':user_id}
            return jsonify(response)  

        return jsonify({'status': 'failed', 'error': error})

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
    
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view