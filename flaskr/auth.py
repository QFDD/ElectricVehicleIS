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

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        content = request.form
        username = content['name']
        password = content['password']
        phone = content['phone']
        email = content['email']
        role = content['role']
        db = get_db()
        error = None
        try:
            db.execute(
                 "INSERT INTO Users (username,role,email,phone,password) VALUES (?, ?, ?, ?, ?)",
                    (username,role,email,phone,generate_password_hash(password)),
            )
            db.commit()
        except db.IntegrityError:
            error = f"User {username} is already registered."
        else:
            return redirect(url_for("auth.login"))
        if error is None:
            response = make_response({'status':'success'})
    
    return response 

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
            response = {'status': "success", 'user_type': user_type}
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