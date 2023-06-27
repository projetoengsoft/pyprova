import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_cors import CORS


basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)
    
    from .routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})
    
    return app