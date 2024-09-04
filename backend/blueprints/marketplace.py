from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models.product import Product
from models import db

marketplace_bp = Blueprint('marketplace', __name__)

@marketplace_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.serialize() for product in products]), 200

@marketplace_bp.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.serialize()), 200

@marketplace_bp.route('/sell', methods=['POST'])
@login_required
def sell_product():
    data = request.json
    new_product = Product(
        name=data['name'], 
        description=data['description'], 
        price=data['price'], 
        owner_id=current_user.id
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product listed successfully'}), 201
