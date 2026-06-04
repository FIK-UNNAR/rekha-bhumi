from flask import Blueprint, jsonify, request
from models.db import get_db, parse_kode
from config import Config

rekhabhumi_2_bp = Blueprint('rekhabhumi_2', __name__, url_prefix='/rekhabhumi')

@rekhabhumi_2_bp.before_request
def log_request_info():
    if Config.FLASK_ENV == 'development':
        print('====== DEBUG (Rekha Bhumi) ======', flush=True)
        print(f"Request method: {request.method}", flush=True)
        print(f"Request URL: {request.url}", flush=True)
        print('=================================', flush=True)

# @rekhabhumi_2_bp.route(...) diletakkan di bawah sini

@rekhabhumi_2_bp.route('/wilayah', methods=['GET'], strict_slashes=False)
def error_wilayah():
    return jsonify({'status': 'ERROR', 'message': f'Perhatikan format end-point. Lihat contoh di {Config.APP_URL}'}), 400
@rekhabhumi_2_bp.route('/wilayah/<req_id:request_id>', methods=['GET'], strict_slashes=False)
def get_wilayah(request_id):
    
    return jsonify({
        "status": "success",
        "message": f"Berhasil diakses dari Blueprint! ID: {request_id}"
    })


