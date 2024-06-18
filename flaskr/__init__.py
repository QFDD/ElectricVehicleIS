import os
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from flaskr.db import init_db, list_tables
socketio = SocketIO()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'cars_database.db'),
    )
    print(app.instance_path)
    socketio.init_app(app)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        
    # ensure the instance folder existsinstance
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import db
    from . import auth
    from . import blog
    from . import chat
    from .api.routes import api_bp
    from . import user
    from . import sales
    db.init_app(app)
    
     # 获取数据库文件路径
    with app.app_context():
        db.list_tables(app.config['DATABASE'])
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(chat.bp)
    app.register_blueprint(api_bp,url_prefix='/api')
    app.register_blueprint(user.bp)
    app.register_blueprint(sales.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app