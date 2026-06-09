from flask import Blueprint, render_template
from config import Config

rekhabhumi_bp = Blueprint('rekhabhumi', __name__, url_prefix='/rekhabhumi')

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
        version=Config.APP_VERSION,
        daftar_endpoint=data_endpoint,
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