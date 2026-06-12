from flask import Blueprint, render_template, jsonify
from config import Config
from models.db_wilayah import get_db, get_versi

rekhabhumi_bp = Blueprint('rekhabhumi', __name__, url_prefix='/rekhabhumi', static_folder='static', static_url_path='/static')

@rekhabhumi_bp.before_request
def log_request_info():
    if Config.FLASK_ENV == 'development':
        print('====== DEBUG (Rekha Bhumi) ======', flush=True)
        print(f"APP_NAME: {Config.APP_NAME}", flush=True)
        print(f"APP_VERSION: {Config.APP_VERSION}", flush=True)
        print(f"FLASK_ENV: {Config.FLASK_ENV}", flush=True)
        print(f"APP_URL: {Config.APP_URL}", flush=True)
        print('=================================', flush=True)

@rekhabhumi_bp.route('/', methods=['GET'], strict_slashes=False)
def root():
    data_endpoint = [
        {"path": "/rekhabhumi/health/", "deskripsi": "Cek status server API"},
        {"path": "/rekhabhumi/ver/", "deskripsi": "Mendapatkan versi API"},
        {"path": "/rekhabhumi/provinsi/", "deskripsi": "Mendapatkan daftar provinsi"},
        {"path": "/rekhabhumi/kabupaten/", "deskripsi": "Mendapatkan daftar kabupaten berdasarkan provinsi"}
    ]
    return render_template(
        'index.html', 
        title="Dokumentasi API", 
        nama_aplikasi=Config.APP_NAME,
        url_aplikasi=Config.APP_URL,
        versi_aplikasi=Config.APP_VERSION,
        versi_database=get_versi(),
        daftar_endpoint=data_endpoint,
    )

@rekhabhumi_bp.route('/dokumentasi', methods=['GET'], strict_slashes=False)
def dokumentasi():
    return render_template(
        'documentation.html', 
        title="Dokumentasi Rekha Bhumi Nusantara", 
        nama_aplikasi=Config.APP_NAME,
        url_aplikasi=Config.APP_URL,
        version=Config.APP_VERSION,
    )

@rekhabhumi_bp.route('/release_note', methods=['GET'], strict_slashes=False)
def release_note():
    return render_template(
        'release_note.html', 
        title="Dokumentasi Rekha Bhumi Nusantara", 
        nama_aplikasi=Config.APP_NAME,
        url_aplikasi=Config.APP_URL,
        version=Config.APP_VERSION,
    )

@rekhabhumi_bp.route('/privasi', methods=['GET'], strict_slashes=False)
def privasi():
    return render_template(
        'privacy.html', 
        title="Kebijakan Privasi API", 
        nama_aplikasi=Config.APP_NAME,
    )

@rekhabhumi_bp.route('/layanan', methods=['GET'], strict_slashes=False)
def layanan():
    return render_template(
        'layanan.html', 
        title="Ketentuan Layanan API", 
        nama_aplikasi=Config.APP_NAME,
    )

@rekhabhumi_bp.route('/acknowledgements', methods=['GET'], strict_slashes=False)
def acknowledgements():
    return render_template(
        'acknowledgements.html', 
        title="Acknowledgements Project API", 
        nama_aplikasi=Config.APP_NAME,
    )

@rekhabhumi_bp.route('/ver', methods=['GET'], strict_slashes=False)
def version():
    versi = {}
    versi["aplikasi"] = Config.APP_VERSION
    versi["database"] = get_versi()
    return jsonify({
        'status': 'SUCCESS',
        'code': '200',
        'request': '/ver',
        'total': len(versi),
        'message': versi
        }), 200