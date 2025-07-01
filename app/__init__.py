from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config  # Добавьте этот импорт

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Загружаем конфиг из класса
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from . import models
    
    from .routes import bp
    app.register_blueprint(bp, url_prefix='/')
    
    return app