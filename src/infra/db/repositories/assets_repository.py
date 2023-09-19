import os
from src.infra.db.clients.sqlite_client import SqliteClient

class AssetsRepository:
    def __init__(self):
        db_file = os.path.abspath(
            "./src/infra/db/database/database.db")
        self.client = SqliteClient(db_file)       

    def get_assets(self):
        self.client.connect()
        query = "SELECT * FROM assets"
        result = self.client.execute_query(query)
        self.client.disconnect()
        return result


    def get_assets_by_user_id(self, user_id):
        self.client.connect()
        query = "SELECT * FROM assets WHERE user_id = ?"
        result = self.client.execute_query(query, [user_id])
        self.client.disconnect()
        return result

    def get_asset_by_id(self, asset_id):
        self.client.connect()
        query = "SELECT * FROM assets WHERE id = ?"
        result = self.client.execute_query_single(query, [asset_id])
        self.client.disconnect()
        return result

    
    def create_asset(self, asset):
        self.client.connect()
        query = "INSERT INTO assets (user_id, name, type, quantity, value, purchase_on) VALUES (?, ?, ?, ?, ?, ?)"
        result = self.client.execute_insert(query, [asset['user_id'], asset['name'], asset['type'], asset['quantity'], asset['value'], asset['purchase_on']])
        self.client.disconnect()
        return result


    def update_asset(self, asset):
        self.client.connect()
        query = "UPDATE assets SET name = ?, type = ?, quantity = ?, value = ?, purchase_on = ? WHERE id = ?"
        result = self.client.execute_insert(query, [asset['user_id'], asset['name'], asset['type'], asset['quantity'], asset['value'], asset['purchase_on']])
        self.client.disconnect()
        return result

    def delete_asset(self, asset_id):
        self.client.connect()
        query = "DELETE FROM assets WHERE id = ?"
        result = self.client.execute_insert(query, [asset_id])
        self.client.disconnect()
        return result
