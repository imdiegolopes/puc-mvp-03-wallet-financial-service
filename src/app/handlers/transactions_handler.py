from flask import jsonify, request

from src.infra.db.repositories.transactions_repository import TransactionsRepository

class TransactionsHandler:
    def __init__(self, request):
        self.request = request

    def handle_get_transactions():
        user_id = request.args.get('user_id')
        repository = TransactionsRepository()

        if user_id:
            transactions = repository.get_transactions_by_user_id(user_id)
        else:
            transactions = repository.get_transactions()

        return jsonify(transactions)

    def handle_get_transaction_by_id(transaction_id):
        if transaction_id is None:
            return jsonify({'error': 'transaction_id is required'}), 400

        repository = TransactionsRepository()
        transaction = repository.get_transaction_by_id(transaction_id)

        if transaction is None:
            return jsonify({'error': 'transaction not found'}), 404

        return jsonify(transaction), 200

    def handle_create_transaction():
        body = request.get_json()

        if body is None:
            return jsonify({'error': 'body is required'}), 400

        if body['user_id'] is None:
            return jsonify({'error': 'user_id is required'}), 400

        if body['asset_id'] is None:
            return jsonify({'error': 'asset_id is required'}), 400

        if body['type'] is None:
            return jsonify({'error': 'type is required'}), 400

        if body['quantity'] is None:
            return jsonify({'error': 'quantity is required'}), 400

        if body['created_on'] is None:
            return jsonify({'error': 'created_on is required'}), 400

        if body['updated_on'] is None:
            return jsonify({'error': 'updated_on is required'}), 400

        if body['price'] is None:
            return jsonify({'error': 'price is required'}), 400

        repository = TransactionsRepository()

        transaction = {
            'user_id': body['user_id'],
            'asset_id': body['asset_id'],
            'type': body['type'],
            'quantity': body['quantity'],
            'created_on': body['created_on'],
            'updated_on': body['updated_on'],
            'price': body['price']
        }

        result = repository.create_transaction(transaction)

        if result is None:
            return jsonify({'error': 'error on create transaction'}), 500

        transaction['ID'] = result

        return jsonify(transaction), 201

    def handle_update_transaction(transaction_id):
        if transaction_id is None:
            return jsonify({'error': 'transaction_id is required'}), 400

        body = request.get_json()

        if body is None:
            return jsonify({'error': 'body is required'}), 400

        if body['user_id'] is None:
            return jsonify({'error': 'user_id is required'}), 400

        if body['asset_id'] is None:
            return jsonify({'error': 'asset_id is required'}), 400

        if body['type'] is None:
            return jsonify({'error': 'type is required'}), 400

        if body['quantity'] is None:
            return jsonify({'error': 'quantity is required'}), 400

        if body['created_on'] is None:
            return jsonify({'error': 'created_on is required'}), 400

        if body['updated_on'] is None:
            return jsonify({'error': 'updated_on is required'}), 400

        if body['price'] is None:
            return jsonify({'error': 'price is required'}), 400

        repository = TransactionsRepository()

        transaction = {
            'ID': transaction_id,
            'user_id': body['user_id'],
            'asset_id': body['asset_id'],
            'type': body['type'],
            'quantity': body['quantity'],
            'created_on': body['created_on'],
            'updated_on': body['updated_on'],
            'price': body['price']
        }

        result = repository.update_transaction(transaction)

        if result is None:
            return jsonify({'error': 'error on update transaction'}), 500

        return jsonify(transaction), 200

    def handle_delete_transaction(transaction_id):
        if transaction_id is None:
            return jsonify({'error': 'transaction_id is required'}), 400

        repository = TransactionsRepository()
        transaction = repository.get_transaction_by_id(transaction_id)

        if transaction is None:
            return jsonify({'error': 'transaction not found'}), 404

        delete = repository.delete_transaction(transaction_id)

        if delete is None:
            return jsonify({'error': 'error on delete transaction'}), 500

        return jsonify({'message': 'transaction deleted'}), 200

    def handle_get_balance(user_id):
        repository = TransactionsRepository()

        # Get all transactions for the user
        transactions = repository.get_transactions_by_user_id(user_id)

        # Calculate balance
        balance = 0
        for transaction in transactions:
            quantity = float(transaction[4])
            price = float(transaction[7])
            ttype = transaction[3]

            if ttype == 'buy':
                balance += quantity * price 
            elif ttype == 'sell':
                balance -= quantity * price 

        return jsonify({'balance': balance}), 200
