from flask import Flask, request, jsonify
import os
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from src.database.models import db





load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_URI')





with app.app_context():
    db.create_all()
