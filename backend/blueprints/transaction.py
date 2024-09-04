from flask import Blueprint, request, jsonify
from web3 import Web3
from flask_login import login_required, current_user
from models.product import Product

transaction_bp = Blueprint('transaction', __name__)

pi_web3 = Web3(Web3.HTTPProvider("https://your-pi-network-node"))

@transaction_bp.route('/purchase', methods=['POST'])
@login_required
def purchase_product():
    data = request.json
    product = Product.query.get_or_404(data['product_id'])
    
    try:
        # Example transaction logic
        transaction = {
            'to': product.owner.wallet_address,
            'value': pi_web3.toWei(product.price, 'pi'),
            'gas': 21000,
            'gasPrice': pi_web3.toWei('50', 'gwei')
        }
        signed_tx = pi_web3.eth.account.sign_transaction(transaction, current_user.private_key)
        tx_hash = pi_web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return jsonify({'status': 'Transaction successful', 'tx_hash': tx_hash.hex()}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400
