import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
INSTANCE_PATH = BASE_DIR / "instance"

# Создаем папку instance, если ее нет
INSTANCE_PATH.mkdir(exist_ok=True)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{INSTANCE_PATH / "site.db"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False