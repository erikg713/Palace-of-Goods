from flask import request, jsonify
from services.transaction_service import TransactionService
from routes import transactions

@transactions.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.json
    transaction = TransactionService.create_transaction(data)
    return jsonify({'success': True, 'transaction': transaction}), 201

@transactions.route('/transactions', methods=['GET'])
def get_transactions():
    user_id = request.args.get('user_id')
    transactions = TransactionService.get_user_transactions(user_id)
    return jsonify({'success': True, 'transactions': transactions}), 200


