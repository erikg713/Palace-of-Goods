from flask import Blueprint, jsonify

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/transactions', methods=['GET'])
def get_transactions():
    # Logic for fetching transactions
    return jsonify({"transactions": []})
