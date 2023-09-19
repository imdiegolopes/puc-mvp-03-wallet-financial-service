
from flask import jsonify, request

from src.infra.db.repositories.assets_repository import AssetsRepository


class AssetsHandler:
    def __init__(self, request):
        self.request = request

    def handle_get_assets():
        user_id = request.args.get('user_id');

        repository = AssetsRepository()

        if user_id:
            assets = repository.get_assets_by_user_id(user_id)
        else:
            assets = repository.get_assets()

        return jsonify(assets)

    def handle_get_assets_by_id(asset_id):
        if asset_id is None:
            return jsonify({'error': 'asset_id is required'}), 400

        repository = AssetsRepository()

        asset = repository.get_asset_by_id(asset_id)

        if asset is None:
            return jsonify({'error': 'asset not found'}), 404

        return jsonify(asset), 200


    def handle_create_assets():

        body = request.get_json()

        if body is None:
            return jsonify({'error': 'body is required'}), 400

        if body['name'] is None:
            return jsonify({'error': 'name is required'}), 400

        if body['type'] is None:
            return jsonify({'error': 'type is required'}), 400

        if body['quantity'] is None:
            return jsonify({'error': 'quantity is required'}), 400

        if body['value'] is None:
            return jsonify({'error': 'value is required'}), 400

        if body['purchase_on'] is None:
            return jsonify({'error': 'purchase_on is required'}), 400

        repository = AssetsRepository()

        asset = {
            'user_id': body['user_id'],
            'name': body['name'],
            'type': body['type'],
            'quantity': body['quantity'],
            'value': body['value'],
            'purchase_on': body['purchase_on']
        }

        result = repository.create_asset(asset)

        if result is None:
            return jsonify({'error': 'error on create asset'}), 500

        asset['id'] = result

        return jsonify(asset), 201


    def handle_update_assets(asset_id):
        if asset_id is None:
            return jsonify({'error': 'asset_id is required'}), 400


        body = request.get_json()

        if body is None:
            return jsonify({'error': 'body is required'}), 400

        if body['name'] is None:
            return jsonify({'error': 'name is required'}), 400

        if body['type'] is None:
            return jsonify({'error': 'type is required'}), 400

        if body['quantity'] is None:
            return jsonify({'error': 'quantity is required'}), 400

        if body['value'] is None:
            return jsonify({'error': 'value is required'}), 400

        if body['purchase_on'] is None:
            return jsonify({'error': 'purchase_on is required'}), 400

        repository = AssetsRepository()

        asset = {
            'id': asset_id,
            'user_id': body['user_id'],
            'name': body['name'],
            'type': body['type'],
            'quantity': body['quantity'],
            'value': body['value'],
            'purchase_on': body['purchase_on']
        }

        result = repository.update_asset(asset)

        if result is None:
            return jsonify({'error': 'error on update asset'}), 500

        return jsonify(asset), 200


    def handle_delete_assets(asset_id):
        if asset_id is None:
            return jsonify({'error': 'asset_id is required'}), 400

        repository = AssetsRepository()

        asset = repository.get_asset_by_id(asset_id)

        if asset is None:
            return jsonify({'error': 'asset not found'}), 404

        delete = repository.delete_asset(asset_id)        

        if delete is None:
            return jsonify({'error': 'error on delete asset'}), 500

        return jsonify({'message': 'asset deleted'}), 200
