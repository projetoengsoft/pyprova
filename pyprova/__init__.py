import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from flask_cors import CORS


basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .models.user import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from .routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    migrate = Migrate(app, db)
    
    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    
    return app