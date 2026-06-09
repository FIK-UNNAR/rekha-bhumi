from flask import Flask, request, render_template
from werkzeug.routing import BaseConverter
from flask_cors import CORS
from config import Config
import subprocess
from pathlib import Path
import shutil
from routes.rekhabhumi_wilayah import rekhabhumi_wilayah_bp
from routes.rekhabhumi_list import rekhabhumi_list_bp

app = Flask(__name__)
app.config.from_object(Config)
if Config.FLASK_ENV not in ['development', 'production']:
    print(f"FATAL ERROR: Unrecognized FLASK_ENV value '{Config.FLASK_ENV}'.", flush=True)
    sys.exit(1)

if Config.FLASK_ENV == 'development': #jika development, jangan cache file statis.
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

class RequestIdConverter(BaseConverter):
    regex = r'^(?:\d{2}|\d{2}\.\d{2}|\d{2}\.\d{2}\.\d{2}|\d{2}\.\d{2}\.\d{2}\.\d{4})$'

app.url_map.converters['req_id'] = RequestIdConverter
app.register_blueprint(rekhabhumi_wilayah_bp, url_prefix='/rekhabhumi/wilayah')
app.register_blueprint(rekhabhumi_list_bp, url_prefix='/rekhabhumi/list')

#root endpoint untuk informasi dan dokumentasi API -statif file di templates/index.html
@app.route('/rekhabhumi/', methods=['GET'], strict_slashes=False)
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
@app.route('/rekhabhumi/privasi', methods=['GET'], strict_slashes=False)
def privasi():
    return render_template(
        'privacy.html', 
        title="Kebijakan Privasi API", 
        nama_aplikasi=Config.APP_NAME,
    )
@app.route('/rekhabhumi/layanan', methods=['GET'], strict_slashes=False)
def layanan():
    return render_template(
        'layanan.html', 
        title="Ketentuan Layanan API", 
        nama_aplikasi=Config.APP_NAME,
    )
@app.route('/rekhabhumi/acknowledgements', methods=['GET'], strict_slashes=False)
def acknowledgements():
    return render_template(
        'acknowledgements.html', 
        title="Acknowledgements Project API", 
        nama_aplikasi=Config.APP_NAME,
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)