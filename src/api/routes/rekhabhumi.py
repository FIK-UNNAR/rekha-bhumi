from flask import Blueprint, jsonify, request
from models.db import get_db, parse_kode
from config import Config

rekhabhumi_bp = Blueprint('rekhabhumi', __name__, url_prefix='/rekhabhumi')

@rekhabhumi_bp.before_request
def log_request_info():
    if Config.FLASK_ENV == 'development':
        print('====== DEBUG (Rekha Bhumi) ======', flush=True)
        print(f"Request method: {request.method}", flush=True)
        print(f"Request URL: {request.url}", flush=True)
        print('=================================', flush=True)

# @rekhabhumi_bp.route(...) diletakkan di bawah sini

@rekhabhumi_bp.route('/ver', methods=['GET'], strict_slashes=False)
def versi():
    return jsonify({'status': 'OK', 'version': '1.0.0', 'app': Config.APP_NAME, 'data': 'Kemendagri 2024'})