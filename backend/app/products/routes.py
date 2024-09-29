from flask import Blueprint, jsonify, request
from app.models import Product, db
from flask_jwt_extended import jwt_required
from app.utils import process_pi_payment

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

@products_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict()), 200

@products_bp.route('/', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@products_bp.route('/buy/<int:id>', methods=['POST'])
@jwt_required()
def buy_product(id):
    product = Product.query.get_or_404(id)
    # Assume user authentication via JWT is already done
    user = get_current_user()
    payment_success = process_pi_payment(user, product.price)
    if payment_success:
        # Update product ownership, record transaction, etc.
        return jsonify({"message": "Transaction successful"}), 200
    else:
        return jsonify({"message": "Transaction failed"}), 400
