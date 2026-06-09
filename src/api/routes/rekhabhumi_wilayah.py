from flask import Blueprint, jsonify, request
from models.db_wilayah import get_db
from config import Config

rekhabhumi_wilayah_bp = Blueprint('rekhabhumi_wilayah', __name__, url_prefix='/rekhabhumi/wilayah')

@rekhabhumi_wilayah_bp.before_request
def log_request_info():
    if Config.FLASK_ENV == 'development':
        print('====== DEBUG (Rekha Bhumi) ======', flush=True)
        print(f"Request Method: {request.method}", flush=True)
        print(f"Request URL: {request.url}", flush=True)
        print(f"Request Origin: {request.headers.get('Origin', 'NO_ORIGIN')}")
        print(f"Request Authorization: {request.headers.get('Authorization', 'NO_AUTH')}")
        print(f"Request Header: {request.headers}", flush=True)
        print('=================================', flush=True)
    else:
        # Nanti dipasang authorization di sini
        pass

    """
    Contoh:
    /rekhabhumi/wilayah/35
    /rekhabhumi/wilayah/35.78
    /rekhabhumi/wilayah/35.78.01
    /rekhabhumi/wilayah/35.78.01.1001
    """

@rekhabhumi_wilayah_bp.route('/', methods=['GET'], strict_slashes=False)
def get_wilayah_root():
    return jsonify({
        'status': 'REQUEST_INVALID',
        'code': '400',
        'request': None,
        'total': 0,
        'message': f'Format request_id tidak valid. Perhatikan format end-point. Lihat contoh di {Config.APP_URL}'
    }), 400

@rekhabhumi_wilayah_bp.route('/<req_id:kode>', methods=['GET'])
def get_wilayah(kode):

    bagian = kode.split('.')

    try:
        db = get_db()
        with db.cursor() as cur:
            hasil = {}
            # Provinsi
            cur.execute("SELECT nama FROM wilayah WHERE kode=%s LIMIT 1",(bagian[0],))
            row = cur.fetchone()

            if not row:
                return jsonify({
                    "status": "error",
                    "message": "Data tidak ditemukan"
                }), 404

            hasil["Provinsi"] = row["nama"]

            # Kabupaten/Kota
            if len(bagian) >= 2:
                kode_kab = ".".join(bagian[:2])

                cur.execute(
                    "SELECT nama FROM wilayah WHERE kode=%s LIMIT 1",
                    (kode_kab,)
                )
                row = cur.fetchone()

                if row:
                    hasil["Kabupaten_Kota"] = row["nama"]

            # Kecamatan
            if len(bagian) >= 3:
                kode_kec = ".".join(bagian[:3])

                cur.execute(
                    "SELECT nama FROM wilayah WHERE kode=%s LIMIT 1",
                    (kode_kec,)
                )
                row = cur.fetchone()

                if row:
                    hasil["Kecamatan"] = row["nama"]

            # Kelurahan
            if len(bagian) >= 4:
                kode_kel = ".".join(bagian[:4])

                cur.execute(
                    "SELECT nama FROM wilayah WHERE kode=%s LIMIT 1",
                    (kode_kel,)
                )
                row = cur.fetchone()

                if row:
                    hasil["Kelurahan"] = row["nama"]

        return jsonify({
            "status": "success",
            "wilayah": hasil
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@rekhabhumi_wilayah_bp.route('/<string:request_id>', methods=['GET'], strict_slashes=False)
def get_wilayah_sink_home(request_id):
    return jsonify({
        'status': 'REQUEST_INVALID',
        'code': '400',
        'request': request_id,
        'total': 0,
        'message': f'Format request_id tidak valid. Perhatikan format end-point. Lihat contoh di {Config.APP_URL}'
    }), 400