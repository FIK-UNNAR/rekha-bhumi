from flask import Flask, request, render_template
from werkzeug.routing import BaseConverter
from flask_cors import CORS
from config import Config
import subprocess
from pathlib import Path
import shutil
from routes.rekhabhumi import rekhabhumi_bp
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
app.register_blueprint(rekhabhumi_bp, url_prefix='/rekhabhumi/')
app.register_blueprint(rekhabhumi_wilayah_bp, url_prefix='/rekhabhumi/wilayah')
app.register_blueprint(rekhabhumi_list_bp, url_prefix='/rekhabhumi/list')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)