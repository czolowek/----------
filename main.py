from flask import Flask, request, jsonify
import os
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from src.database.models import db
from src.data import parse_products
from typing import Optional




load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_URI')
db.init_app(app)
api = Api(app)



# with app.app_context():
#     # db.create_all()
#     parse_products.get_products()


class ProductAPI(Resource):
    def get(self, product_id: Optional[str] = None):
        if product_id:
            product = db_actions.get_product(product_id)
            return jsonify(product)
        else:
            products = db_actions.get_products()
            response = jsonify(products)

        response.status_code = 200
        return response
            
        
        