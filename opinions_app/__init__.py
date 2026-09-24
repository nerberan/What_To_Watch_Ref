# what_to_watch_ref/opinions_app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import Config  # импортируем настройки
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)  # применяем все настройки разом

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models
from . import views, error_handlers, cli_commands
