from src.database.base import db
from src.database.models import Product, Review
from src.data import parse_products
import uuid



def get_products():
    return db.session.query(Product).all()



def get_product(product_id: str):
    return db.first_or_404(Product.query.filter_by(id=product_id))




def add_product(name: str, description: str, price: float, img_url: str):
    Product = Product(
        id=uuid.uuid4().hex,
        name=name,
        description=description,
        price=price,
        img_url=img_url
    )
    

    db.session.add(Product)
    db.session.commit()



def delete_product(product_id: str):
    product = product.query.filter_by(id=product_id).one_or_404()
    db.session.delete(product)
    db.session.commit()
    
    