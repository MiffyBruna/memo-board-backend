from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    
    # Import models here
    from app.models.memo import Memo
    from app.models.board import Board
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register Blueprints here
    from .routes import hello_world_bp
    from .routes import board_bp
    from .routes import memo_bp
    
    app.register_blueprint(hello_world_bp)
    app.register_blueprint(board_bp)
    app.register_blueprint(memo_bp)

    return app