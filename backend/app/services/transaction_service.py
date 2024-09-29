from models import Transaction, db

class TransactionService:
    @staticmethod
    def create_transaction(data):
        transaction = Transaction(sender_id=data['sender_id'], receiver_id=data['receiver_id'], amount=data['amount'])
        db.session.add(transaction)
        db.session.commit()
        return transaction

    @staticmethod
    def get_user_transactions(user_id):
        return Transaction.query.filter((Transaction.sender_id == user_id) | (Transaction.receiver_id == user_id)).all()
