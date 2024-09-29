from models import Product, db

class ProductService:
    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def create_product(data):
        product = Product(name=data['name'], price=data['price'], description=data.get('description'), seller_id=data['seller_id'])
        db.session.add(product)
        db.session.commit()
        return product
