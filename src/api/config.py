import os

class Config:
    APP_NAME    = os.getenv('APP_NAME', 'Rekha Bhumi Nusantara')
    FLASK_ENV   = os.getenv('FLASK_ENV', 'development')
    APP_URL     = os.getenv('APP_URL', 'http://api.testing.id/rekhabhumi')
    DB_HOST     = os.getenv('DB_HOST', '127.0.0.1')
    DB_PORT     = int(os.getenv('DB_PORT', 3306))   # ← wajib int, bukan string
    DB_USER     = os.getenv('DB_USER', 'rekha_bhumi')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'p@ssw0rd')
    DB_NAME     = os.getenv('DB_NAME', 'rekhabhumi')
    SECRET_KEY  = os.getenv('SECRET_KEY', 'kunci-rahasia-anda-disini')
    STAGE_RUNNING = os.getenv('STAGE_RUNNING', 'development')  # default ke development jika tidak diset