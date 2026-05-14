import pymysql
import pymysql.cursors
from config import Config


def get_db():
    print("============ DEBUG ============")
    print("Connecting to DB with config:")
    print(f"Host: {Config.DB_HOST}")
    print(f"Port: {Config.DB_PORT}")
    print(f"User: {Config.DB_USER}")
    print(f"Password: {'*' * len(Config.DB_PASSWORD)}")  # Don't print the actual password
    print(f"Database: {Config.DB_NAME}")
    print("===============================")
    
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


def parse_kode(kode: str) -> dict:
    """
    Format baru:
      11            → provinsi
      11.01         → kabkota
      11.01.01      → kecamatan
      11.01.01.2001 → kelurahan
    """
    parts = kode.strip().split('.')
    if not (1 <= len(parts) <= 4):
        raise ValueError(f"Format kode tidak valid: '{kode}'")
    return {
        'prov': parts[0] if len(parts) >= 1 else None,
        'kab':  parts[1] if len(parts) >= 2 else None,
        'kec':  parts[2] if len(parts) >= 3 else None,
        'kel':  parts[3] if len(parts) == 4 else None,
    }


def get_level(kode: str) -> str:
    parts = kode.strip().split('.')
    level_map = {1: 'provinsi', 2: 'kabkota', 3: 'kecamatan', 4: 'kelurahan'}
    level = level_map.get(len(parts))
    if level is None:
        raise ValueError(f"Format kode tidak valid: '{kode}'")
    return level