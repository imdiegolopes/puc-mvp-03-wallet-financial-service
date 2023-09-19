import os
from src.infra.db.clients.sqlite_client import SqliteClient

class TransactionsRepository:
    def __init__(self):
        db_file = os.path.abspath("./src/infra/db/database/database.db")
        self.client = SqliteClient(db_file)       

    def get_transactions(self):
        self.client.connect()
        query = "SELECT * FROM transactions"
        result = self.client.execute_query(query)
        self.client.disconnect()
        return result

    def get_transactions_by_user_id(self, user_id):
        self.client.connect()
        query = "SELECT * FROM transactions WHERE user_id = ?"
        result = self.client.execute_query(query, [user_id])
        self.client.disconnect()
        return result

    def get_transaction_by_id(self, transaction_id):
        self.client.connect()
        query = "SELECT * FROM transactions WHERE ID = ?"
        result = self.client.execute_query_single(query, [transaction_id])
        self.client.disconnect()
        return result

    def create_transaction(self, transaction):
        self.client.connect()
        query = "INSERT INTO transactions (user_id, asset_id, type, quantity, created_on, updated_on, price) VALUES (?, ?, ?, ?, ?, ?, ?)"
        result = self.client.execute_insert(query, [transaction['user_id'], transaction['asset_id'], transaction['type'], transaction['quantity'], transaction['created_on'], transaction['updated_on'], transaction['price']])
        self.client.disconnect()
        return result

    def update_transaction(self, transaction):
        self.client.connect()
        query = "UPDATE transactions SET user_id = ?, asset_id = ?, type = ?, quantity = ?, created_on = ?, updated_on = ?, price = ? WHERE ID = ?"
        result = self.client.execute_insert(query, [transaction['user_id'], transaction['asset_id'], transaction['type'], transaction['quantity'], transaction['created_on'], transaction['updated_on'], transaction['price'], transaction['ID']])
        self.client.disconnect()
        return result

    def delete_transaction(self, transaction_id):
        self.client.connect()
        query = "DELETE FROM transactions WHERE ID = ?"
        result = self.client.execute_insert(query, [transaction_id])
        self.client.disconnect()
        return result
