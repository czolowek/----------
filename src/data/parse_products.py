from src.database.base import db
from src.database.models import Product
from uuid import uuid4
from requests_html import HTMLSession


URL = "https://rozetka.com.ua/ua/igrovie-mishi/c4673278/producer=logitech/"



def get_products(url: str=URL):
    session = HTMLSession()
    response = session.get(url)
    print(response)
    products = response.html.xpath('//rz-indexed-link[@class="product-link goods-tile__heading"]/a[@_ngcontent-rz-client-c4240794426 and @data-test="filter-link"]/@href')
    for product in products:
        print(product)
        save_product(product)
    db.session.commit()

def save_product(product_url: str):
    session = HTMLSession()
    response = session.get(product_url)


    name = response.html.xpath('//p[@_ngcontent-rz-client-c4240794426 and  @class="title_font"/text()]')[0]
    price = response.html.xpath('//p[contains(@class, "product-price__big")]/text')[0]
    img_url = response.html.xpath('//img[_ngcontent-rz-client-c2880331661]/@src')[0]
    description = response.html.xpath('//div[@id="description" or contains(@class, "product-about")]//text()')[0]
    description =  ''.join(description)


    product = Product(
    id=uuid4().hex,
    name=name,
    price=price,
    img_url=img_url,
    description=description

    )
    db.session.add(product)
