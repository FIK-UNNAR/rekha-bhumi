# kode-wilayah

Aplikasi API Python untuk menyediakan layanan kode wilayah Republik Indonesia berdasarkan Keputusan Menteri Dalam Negeri (Kepmendagri).

## Deskripsi

Aplikasi ini dibuat agar masyarakat, pengembang, dan pihak lain dapat dengan mudah mengakses informasi kode wilayah administratif Indonesia. Data yang digunakan disusun menurut format kode wilayah resmi dan terus dirawat ketika ada pembaruan dari keputusan Mendagri.

## Format Kode Wilayah

Kode wilayah memiliki 4 bagian utama, dipisahkan dengan titik:

- `aa` : kode provinsi
- `bb` : kode kota/kabupaten di dalam provinsi `aa`
- `cc` : kode kecamatan di dalam kota/kabupaten `bb`
- `dddd` : kode kelurahan/desa di dalam kecamatan `cc`

Contoh struktur:

- `11.01.02.0001`
- `33.12.05.1234`

## Layanan API

API ini menyediakan akses kode wilayah berdasarkan format kode tersebut. Pengguna dapat menggunakan endpoint layanan untuk mencari dan menampilkan informasi wilayah sesuai struktur kode.

> Versi Kepmendagri yang tersimpan di database aplikasi ini dapat dilihat dengan mengakses kode wilayah `00.00.00.0000`.

## Tujuan

- Memudahkan masyarakat menemukan kode wilayah resmi Indonesia.
- Menyediakan layanan yang siap dipakai oleh aplikasi lain.
- Menjaga akurasi kode wilayah dengan pembaruan dari Keputusan Mendagri.

## Struktur Proyek

- `src/api/` : tempat kode sumber API berada.
- `README.md` : dokumentasi proyek.

## Pemeliharaan

Pengembang akan terus memperbarui data wilayah ketika ada keputusan baru dari Menteri Dalam Negeri, sehingga aplikasi tetap sinkron dengan kode wilayah NKRI terbaru.
