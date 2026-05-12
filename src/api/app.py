from flask import Flask
from flask_cors import CORS
from config import Config
from routes.wilayah import wilayah_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(wilayah_bp, url_prefix='/api/wilayah')

@app.route('/api/health')
def health():
    return {'status': 'ok', 'service': 'Sistem Wilayah API v2'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)