from flask import Blueprint, jsonify, request
from models.db import get_db, parse_kode
from config import Config

rekhabhumi_2_bp = Blueprint('rekhabhumi_2', __name__, url_prefix='/rekhabhumi/wilayah')

@rekhabhumi_2_bp.before_request
def log_request_info():
    if Config.FLASK_ENV == 'development':
        print('====== DEBUG (Rekha Bhumi) ======', flush=True)
        print(f"Request method: {request.method}", flush=True)
        print(f"Request URL: {request.url}", flush=True)
        print('=================================', flush=True)

@rekhabhumi_2_bp.route('/', methods=['GET'], strict_slashes=False)
def error_wilayah():
    return jsonify({
        "status": "ERROR",
        "invalid_input": request_id,
        "message": "Format ID salah. Gunakan format xx, xx.xx, xx.xx.xx, atau xx.xx.xx.xxxx"
    }), 400

@rekhabhumi_2_bp.route('/<req_id:request_id>', methods=['GET'], strict_slashes=False)
def get_wilayah(request_id):
    query = f"SELECT kode, nama FROM wilayah WHERE kode LIKE '{request_id.strip()}' ORDER BY kode"  
    db = get_db()
    try:
        with db.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
        if len(rows) == 0:
            return jsonify({'status': 'NOT_FOUND', 'total': 0, 'message': 'Data tidak ditemukan'}), 404
        return jsonify({'status': 'SUCCESS', 'total': len(rows), 'data': rows})
    except Exception as e:
        return jsonify({'status': 'ERROR', 'message': str(e)}), 500
    finally:
        db.close()
 
@rekhabhumi_2_bp.route('/<string:request_id>', methods=['GET'], strict_slashes=False)
def get_wilayah_sink_home(request_id):
    return jsonify({
        "status": "ERROR",
        "invalid_input": request_id,
        "message": "Format ID salah. Gunakan format xx, xx.xx, xx.xx.xx, atau xx.xx.xx.xxxx"
    }), 400

