from flask import Flask
import os
from init import db, ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"]="postgresql+psycopg2://trello_dev:123456@localhost:5432/trello_mvc_db"
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    return app