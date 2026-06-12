import pymysql
import pymysql.cursors
from config import Config


def get_db():
    if Config.FLASK_ENV == 'development':
        print("============ DEBUG DB SETTINGS ============")
        print("Connecting to DB with config:")
        print(f"Host: {Config.DB_HOST}")
        print(f"Port: {Config.DB_PORT}")
        print(f"User: {Config.DB_USER}")
        print(f"Password: {'*' * len(Config.DB_PASSWORD)}")  # Don't print the actual password
        print(f"Database: {Config.DB_NAME}")
        print("============ END of DEBUG ============")
    
    return pymysql.connect(
        host=Config.DB_HOST,
        port=int(Config.DB_PORT),
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False
    )

def get_versi():
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT nama FROM wilayah WHERE kode='00.00.00.0000'")
        row = cur.fetchone()
        db.close()
    except Exception as e:
        return None

    if row == None :
        return None
    else:
        return row['nama']