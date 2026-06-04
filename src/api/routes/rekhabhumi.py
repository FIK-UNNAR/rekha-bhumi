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

@rekhabhumi_bp.route('/list', methods=['GET'], strict_slashes=False)
def error_list():
    #mengembalikan semua list provinsi di Indonesia
    return jsonify({'status': 'SUCCESS', 'message': f'List semua provinsi di Indonesia'}), 200

@rekhabhumi_bp.route('/list/<req_id:request_id>', methods=['GET'], strict_slashes=False)
def get_list(request_id):
    match len(str(request_id.strip())):
        case 2:
            #mengembalikan semua list kota/kabupaten di provinsi di Indonesia
            return jsonify({'status': 'SUCCESS', 'message': f'List kota/kabupaten di provinsi {request_id}'}), 200
        case 5:
            # Handle kabupaten
            return jsonify({'status': 'SUCCESS', 'message': f'List Kecamatan di {request_id}'}), 200
        case 8:
            # Handle kecamatan
            return jsonify({'status': 'SUCCESS', 'message': f'List Desa/Kelurahan di {request_id}'}), 200
        case _:
            return jsonify({'status': 'ERROR', 'message': f'Format request_id tidak valid. Perhatikan format end-point. Lihat contoh di {Config.APP_URL}'}), 400