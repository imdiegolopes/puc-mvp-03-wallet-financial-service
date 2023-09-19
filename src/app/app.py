from handlers.healthcheck_handler import HealthcheckHandler
from flask import (
    Flask
)
from flask_cors import CORS

from handlers.assets_handler import AssetsHandler

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule('/', 'index', HealthcheckHandler.handle, methods=['GET'])

app.add_url_rule('/v1/assets', 'get_assets', AssetsHandler.handle_get_assets, methods=['GET'])
app.add_url_rule('/v1/assets/<string:asset_id>', 'get_asset', AssetsHandler.handle_get_assets_by_id, methods=['GET'])
app.add_url_rule('/v1/assets', 'create_assets', AssetsHandler.handle_create_assets, methods=['POST'])
app.add_url_rule('/v1/assets/<string:asset_id>', 'update_assets', AssetsHandler.handle_update_assets, methods=['PUT'])
app.add_url_rule('/v1/assets/<string:asset_id>', 'delete_assets', AssetsHandler.handle_delete_assets, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=8083, host="0.0.0.0")
