# what_to_watch_ref/settings.py
import os

from dotenv import load_dotenv

load_dotenv()  # ← обязательно, иначе .env не подхватится


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
