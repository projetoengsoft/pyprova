import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_cors import CORS

from flask_jwt_extended import JWTManager


basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    
    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['JWT_SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    jwt = JWTManager(app)
    
    from .models.user import User
    
    from .controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .controllers.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    migrate = Migrate(app, db)
    
    return app