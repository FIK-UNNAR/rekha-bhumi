from flask import Flask, request, render_template
from flask_cors import CORS
from config import Config
import subprocess
from pathlib import Path
import shutil
from routes.rekhabhumi import rekhabhumi_bp
#from routes.wilayah import wilayah_bp

app = Flask(__name__)
app.config.from_object(Config)
if Config.FLASK_ENV not in ['development', 'production']:
    print(f"FATAL ERROR: Unrecognized FLASK_ENV value '{Config.FLASK_ENV}'.", flush=True)
    sys.exit(1)
if Config.FLASK_ENV == 'development':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.register_blueprint(rekhabhumi_bp, url_prefix='/rekhabhumi')

@app.route('/rekhabhumi/', methods=['GET'], strict_slashes=False)
def root():
    data_endpoint = [
        {"path": "/rekhabhumi/health/", "deskripsi": "Cek status server API"},
        {"path": "/rekhabhumi/ver/", "deskripsi": "Mendapatkan versi API"},
        {"path": "/rekhabhumi/provinsi/", "deskripsi": "Mendapatkan daftar provinsi"},
        {"path": "/rekhabhumi/kabupaten/", "deskripsi": "Mendapatkan daftar kabupaten berdasarkan provinsi"}
    ]
    
    # 2. Render template dan lempar datanya (Ini adalah konsep MVC!)
    return render_template(
        'index.html', 
        title="Dokumentasi API", 
        nama_aplikasi=Config.APP_NAME,
        daftar_endpoint=data_endpoint,
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)