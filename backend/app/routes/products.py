from flask import Blueprint, request, jsonify
from app.models import Product, db

products = Blueprint('products', __name__)

@products.route('/api/products', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in all_products]), 200

@products.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created"}), 201
