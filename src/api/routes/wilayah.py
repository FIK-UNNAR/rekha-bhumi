from flask import Blueprint, jsonify, request
from models import get_db, parse_kode

wilayah_bp = Blueprint('wilayah', __name__)

@wilayah_bp.route('/', methods=['GET'])
def do_list():
    kode = request.args.get('kd', default="", type=str)
    token = request.args.get('tk', default=None, type=str)
    #### CHECK TOKEN DULU DI SINI ####
    match len(str(kode.strip())):
        case 0:
            level = 'list seluruh provinsi'
            query = f"SELECT kode, nama FROM wilayah WHERE kode REGEXP '^[0-9]{{2}}$' ORDER BY kode"
        case 2:
            level = 'list kabupaten/kota'
            query = f"SELECT kode, nama FROM wilayah WHERE kode REGEXP '^{kode.strip()}.[0-9]{{2}}$' ORDER BY kode"
        case 5:
            level = 'list kecamatan'
            query = f"SELECT kode, nama FROM wilayah WHERE kode REGEXP '^{kode.strip()}.[0-9]{{2}}$' ORDER BY kode"
        case 8:
            level = 'list desa/kelurahan'
            query = f"SELECT kode, nama FROM wilayah WHERE kode REGEXP '^{kode.strip()}.[0-9]{{4}}$' ORDER BY kode"
        case 13:
            level = 'spesifik nama wilayah atau cek nomor kepmendagri'
            query = f"SELECT kode, nama FROM wilayah WHERE kode LIKE '{kode.strip()}' ORDER BY kode"
        case _:
            return jsonify({'status': 'error', 'message': 'kode tidak valid'}), 400
    db = get_db()
    print(query)
    try:
        with db.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
        if len(rows) == 0:
            return jsonify({'status': 'not_found', 'total': 0, 'message': 'Data tidak ditemukan'}), 404
        return jsonify({'status': 'OK', 'total': len(rows), 'data': rows})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        db.close()

@wilayah_bp.route('/provinsi', methods=['GET'])
def get_provinsi():
    """
    List semua provinsi (kode 2 digit)
    GET /api/wilayah/provinsi
    """
    db = get_db()
    try:
        with db.cursor() as cur:
            cur.execute("""
                SELECT kode, nama FROM wilayah
                WHERE kode REGEXP '^[0-9]{2}$'
                ORDER BY kode
            """)
            rows = cur.fetchall()
        return jsonify({'status': 'ok', 'total': len(rows), 'data': rows})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        db.close()


@wilayah_bp.route('/kabkota/<prov_kode>', methods=['GET'])
def get_kabkota(prov_kode):
    """
    List kabupaten/kota berdasarkan kode provinsi
    GET /api/wilayah/kabkota/11
    """
    try:
        p = parse_kode(prov_kode.strip())
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

    if p['kab'] is not None:
        return jsonify({'status': 'error', 'message': 'Gunakan kode provinsi 2 digit, contoh: 11'}), 400

    db = get_db()
    try:
        with db.cursor() as cur:
            pattern = f'^{p["prov"]}\\.[0-9]{{2}}$'
            cur.execute("""
                SELECT kode, nama FROM wilayah
                WHERE kode REGEXP %s
                ORDER BY kode
            """, (pattern,))
            rows = cur.fetchall()
        return jsonify({'status': 'ok', 'total': len(rows), 'data': rows})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        db.close()


@wilayah_bp.route('/kecamatan/<path:kabkota_kode>', methods=['GET'])
def get_kecamatan(kabkota_kode):
    """
    List kecamatan berdasarkan kode kabupaten/kota
    GET /api/wilayah/kecamatan/11.01
    """
    try:
        p = parse_kode(kabkota_kode.strip())
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

    if p['kab'] is None or p['kec'] is not None:
        return jsonify({'status': 'error', 'message': 'Gunakan kode kab/kota format XX.XX, contoh: 11.01'}), 400

    db = get_db()
    try:
        with db.cursor() as cur:
            pattern = f'^{p["prov"]}\\.{p["kab"]}\\.[0-9]{{2}}$'
            cur.execute("""
                SELECT kode, nama FROM wilayah
                WHERE kode REGEXP %s
                ORDER BY kode
            """, (pattern,))
            rows = cur.fetchall()
        return jsonify({'status': 'ok', 'total': len(rows), 'data': rows})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        db.close()


@wilayah_bp.route('/kelurahan/<path:kec_kode>', methods=['GET'])
def get_kelurahan(kec_kode):
    """
    List kelurahan/desa berdasarkan kode kecamatan
    GET /api/wilayah/kelurahan/11.01.01
    """
    try:
        p = parse_kode(kec_kode.strip())
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

    if p['kec'] is None or p['kel'] is not None:
        return jsonify({'status': 'error', 'message': 'Gunakan kode kecamatan format XX.XX.XX, contoh: 11.01.01'}), 400

    db = get_db()
    try:
        with db.cursor() as cur:
            pattern = f'^{p["prov"]}\\.{p["kab"]}\\.{p["kec"]}\\.[0-9]{{4}}$'
            cur.execute("""
                SELECT kode, nama FROM wilayah
                WHERE kode REGEXP %s
                ORDER BY kode
            """, (pattern,))
            rows = cur.fetchall()
        return jsonify({'status': 'ok', 'total': len(rows), 'data': rows})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        db.close()


@wilayah_bp.route('/cari/kode/<path:kode>', methods=['GET'])
def cari_by_kode(kode):
    """
    Cari wilayah berdasarkan kode eksak
    GET /api/wilayah/cari/kode/11
    GET /api/wilayah/cari/kode/11.01
    GET /api/wilayah/cari/kode/11.01.01
    GET /api/wilayah/cari/kode/11.01.01.2001
    """
    db = get_db()
    try:
        with db.cursor() as cur:
            cur.execute("""
                SELECT kode, nama FROM wilayah
                WHERE kode = %s
            """, (kode.strip(),))
            row = cur.fetchone()
        if row:
            return jsonify({'status': 'ok', 'data': row})
        return jsonify({'status': 'not_found', 'message': f'Kode {kode} tidak ditemukan'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        db.close()


@wilayah_bp.route('/cari/nama', methods=['GET'])
def cari_by_nama():
    """
    Cari wilayah berdasarkan nama (semua level)
    GET /api/wilayah/cari/nama?q=aceh
    GET /api/wilayah/cari/nama?q=aceh&level=provinsi
    GET /api/wilayah/cari/nama?q=aceh&level=kabkota
    GET /api/wilayah/cari/nama?q=aceh&level=kecamatan
    GET /api/wilayah/cari/nama?q=aceh&level=kelurahan
    """
    q = request.args.get('q', '').strip()
    level = request.args.get('level', '').strip()

    if not q:
        return jsonify({'status': 'error', 'message': 'Parameter q tidak boleh kosong'}), 400

    level_filters = {
        'provinsi':  "AND kode REGEXP '^[0-9]{2}$'",
        'kabkota':   "AND kode REGEXP '^[0-9]{2}\\\\.[0-9]{2}$'",
        'kecamatan': "AND kode REGEXP '^[0-9]{2}\\\\.[0-9]{2}\\\\.[0-9]{2}$'",
        'kelurahan': "AND kode REGEXP '^[0-9]{2}\\\\.[0-9]{2}\\\\.[0-9]{2}\\\\.[0-9]{4}$'",
    }
    level_filter = level_filters.get(level, '')

    db = get_db()
    try:
        with db.cursor() as cur:
            sql = f"""
                SELECT kode, nama FROM wilayah
                WHERE nama LIKE %s {level_filter}
                ORDER BY kode
                LIMIT 50
            """
            cur.execute(sql, (f'%{q}%',))
            rows = cur.fetchall()
        return jsonify({'status': 'ok', 'total': len(rows), 'data': rows})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        db.close()