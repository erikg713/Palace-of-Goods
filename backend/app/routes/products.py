from flask import request, jsonify
from services.product_service import ProductService
from routes import products_bp

@products_bp.route('/products', methods=['GET'])
def get_products():
    products = ProductService.get_all_products()
    return jsonify({'success': True, 'products': products}), 200

@products_bp.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = ProductService.create_product(data)
    return jsonify({'success': True, 'product': product}), 201

