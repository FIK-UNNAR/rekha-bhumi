from flask import Blueprint, jsonify, request
from models.db import get_db, parse_kode
from config import Config

rekhabhumi_2_bp = Blueprint('rekhabhumi_2', __name__, url_prefix='/rekhabhumi/list')

@rekhabhumi_2_bp.before_request
def log_request_info():
    if Config.FLASK_ENV == 'development':
        print('====== DEBUG (Rekha Bhumi) ======', flush=True)
        print(f"Request method: {request.method}", flush=True)
        print(f"Request URL: {request.url}", flush=True)
        print('=================================', flush=True)

@rekhabhumi_2_bp.route('/', methods=['GET'], strict_slashes=False)
def error_wilayah():
    query = "SELECT kode, nama FROM wilayah WHERE LENGTH(kode) = 2 AND kode BETWEEN '00' AND '99' ORDER BY kode"
    db = get_db()
    try:
        print(f'query : {query}')
        with db.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
        if len(rows) == 0:
            return jsonify({
                'status': 'NOT_FOUND',
                'code': '404',
                'request': '/list/',
                'total': 0,
                'message': 'Data tidak ditemukan. Mohon informasikan ke admin.'
            }), 404
        return jsonify({
            'status': 'SUCCESS',
            'code': '200',
            'request': '/list/',
            'total': len(rows),
            'message': rows}), 200
    except Exception as e:
        return jsonify({
            'status': 'ERROR',
            'code': '500',
            'request': '/list/',
            'total': 0,
            'message': str(e)}), 500
    finally:
        db.close()

@rekhabhumi_2_bp.route('/<req_id:request_id>', methods=['GET'], strict_slashes=False)
def get_wilayah(request_id):
    match len(str(request_id.strip())):
        case 2:
            # list semua kab/kota di propivinsi : xx.xx
            query = f"SELECT kode, nama FROM wilayah WHERE LENGTH(kode) = 5 AND kode LIKE '{request_id.strip()}.%' ORDER BY kode"
        case 5:
            #list semua kecamatan di kab/kota : xx.xx.xx
            query = f"SELECT kode, nama FROM wilayah WHERE LENGTH(kode) = 8 AND kode LIKE '{request_id.strip()}.%' ORDER BY kode"
        case 8:
            #list semua desa/kelurahan di kecamatan: xx.xx.xx.xxxx
            query = f"SELECT kode, nama FROM wilayah WHERE LENGTH(kode) = 13 AND kode LIKE '{request_id.strip()}.%' ORDER BY kode"
        case 13:
            return jsonify({
                'status': 'REQUEST INVALID',
                'code': '400',
                'request': f'/list/{request_id}',
                'total': 0,
                'message': f'Gunakan end-point /wilayah/<kode wilayah> untuk mendapatkan nama wilayah. Lihat contoh di {Config.APP_URL}'
            }), 400
    db = get_db()
    try:
        with db.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
        if len(rows) == 0:
            return jsonify({
                'status': 'NOT_FOUND',
                'code': '404',
                'request': f'/list/{request_id}',
                'total': 0,
                'message': 'Data tidak ditemukan'
            }), 404
        return jsonify({
            'status': 'SUCCESS',
            'code': '200',
            'request': f'/list/{request_id}',
            'total': len(rows),
            'message': rows}), 200
    except Exception as e:
        return jsonify({
            'status': 'ERROR',
            'code': '500',
            'request': f'/list/{request_id}',
            'total': 0,
            'message': str(e)}), 500
    finally:
        db.close()
 
@rekhabhumi_2_bp.route('/<string:request_id>', methods=['GET'], strict_slashes=False)
def get_wilayah_sink_home(request_id):
    return jsonify({
        'status': 'REQUEST_INVALID',
        'code': '400',
        'request': request_id,
        'total': 0,
        'message': f'Format request_id tidak valid. Perhatikan format end-point. Lihat contoh di {Config.APP_URL}'
    }), 400

