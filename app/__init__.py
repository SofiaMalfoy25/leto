from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Явно загружаем конфигурацию
    app.config.from_object('config.Config')
    
    # Проверка загрузки конфигурации
    if not app.config.get('SQLALCHEMY_DATABASE_URI'):
        raise ValueError("Database URI not configured!")
    
    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Импорт и регистрация blueprint
    from .routes import bp
    app.register_blueprint(bp)
    
    return app