# Rekha Bhumi Nusantara

**Rheka Bhumi Nusantara** (bahasa Sansekerta, **Rekha** yang berarti garis/coretan, **Bhumi** yang berarti tanah/wilayah, dan **Nusantara** atau Nusa Antara yang berarti Indonesia) adalah _Application Programming Interface_ (API) yang akan memberikan kode wilayah resmi Republik Indonesia berdasarkan Keputusan Menteri Dalam Negeri (KEPMENDAGRI) yang berlaku saat ini. Sistematika kode wilayah ini dibuat berdasarkan hirarki wilayah dari provinsi, kota/kabupaten, kecamatan, hingga desa/kelurahan, sehingga dapat langsung diakses dan digunakan dalam aplikasi dengan pilihan berbentuk SELECT.
<div align="center"><img src="rekha-bhumi-logo.png" alt="Logo Rekha Bhumi" width="200" />
</div>

## Deskripsi

Kode Wilayah adalah identitas resmi berupa serangkaian angka (numerik) yang merepresentasikan setiap tingkatan wilayah administrasi pemerintahan di Indonesia. Kode Wilayah ini secara resmi dikelola oleh **Kementerian Dalam Negeri** (Kemendagri), dan berfungsi sebagai standar nasional untuk pendataan penduduk, perencanaan pembangunan, dan pelayanan publik agar seragam di seluruh instansi.

Bagi pengembang aplikasi, kode wilayah bukan sekadar angka formalitas, melainkan standar data **(Single Source of Truth)** yang sangat krusial untuk mengelola database lokasi pengguna.

Berikut adalah fungsi utamanya dalam pengembangan aplikasi:

1. **Standarisasi dan Validasi Data (Data Integrity).**
Tanpa kode wilayah, pengguna mungkin menulis alamat dengan cara berbeda-beda (misal: "Jaksel", "Jakarta Selatan", atau "DKI Jakarta"). Dengan kode wilayah (seperti 31.74), aplikasi akan memastikan input lokasi seragam sesuai standar Kemendagri/BPS dan mempermudah proses filter dan pencarian (pencarian berbasis angka jauh lebih cepat dan akurat daripada pencarian berbasis teks/string).
2. **Fitur "Cascading Dropdown" (Alamat Bertingkat).**
Pada formulir pendaftaran, kode wilayah digunakan untuk logika relasional. Sebagai contoh, saat pengguna memilih Provinsi (misal: 32 - Jawa Barat), aplikasi dapat secara otomatis hanya akan memunculkan daftar Kabupaten/Kota yang kode awalnya 32.XX. Hal ini mencegah kesalahan input, seperti pengguna memilih Provinsi Jawa Barat tapi memilih Kota Surabaya.
3. **Pemetaan Layanan dan Distribusi (Geofencing Logis).**
Pada aplikasi yang memiliki fitur layanan fisik (seperti e-commerce atau pesan antar), maka dengan sangat mudah bisa mengatur ongkir atau ketersediaan stok berdasarkan kode wilayah tertentu. Selain itu dapat sebagai analisa pengguna dengan memetakan di wilayah mana (kode wilayah mana) akun paling aktif tanpa harus memproses koordinat GPS yang rumit.
4. **Keamanan dan Verifikasi Akun.**
Beberapa aplikasi finansial atau legal menggunakan kode wilayah untuk *cross-check* NIK. Misalkan memvalidasi apakah 6 digit pertama NIK yang diinput pengguna sesuai dengan data lokasi (Provinsi/Kota/Kecamatan) yang mereka klaim di profil. Selain itu, dapat juga sebagai pendeteksi anomali. Yaitu jika sebuah akun terdaftar dengan kode wilayah Papua tetapi melakukan transaksi yang tidak biasa di wilayah lain, sistem akan dengan mudah bisa memberikan peringatan keamanan.

**Rekha Bhumi** ini dibuat agar masyarakat, pengembang, dan pihak lain dapat dengan mudah mengakses informasi kode wilayah administratif Indonesia. Data yang digunakan disusun menurut format kode wilayah resmi dan akan terus dirawat ketika ada pembaruan dari keputusan Mendagri.

## Struktur Kode Wilayah Kemendagri

Kode ini memiliki hierarki tertentu yang biasanya berjumlah hingga 10 digit untuk tingkat desa:
- Provinsi (2 digit pertama): Menunjukkan identitas provinsi (misal: 35 untuk Jawa Timur).
- Kabupaten/Kota (2 digit berikutnya): Menunjukkan identitas daerah tingkat II. Awalan angka 0 sampai dengan 6 (01 - 69) menunjukkan statusnya sebagai kabupaten dan angka 7 sampai dengan 9 (71 - 99) menunjukkan statusnya sebagai kota (misal: 78 untuk Kota Surabaya).
- Kecamatan (2 digit ketiga): Menunjukkan identitas wilayah kecamatan
- Desa/Kelurahan (4 digit terakhir): Menunjukkan unit terkecil. Angka pertama dari 4 digit ini membedakan status, dimulai dengan angka 1 untuk Kelurahan dan dimulai dengan angka 2 untuk Desa (misal 1004 untuk kelurahan Ketintang di kecamatan Gayungan kota Surabaya).

Sebagai contoh, 35.78.22.1004 adalah kode untuk kelurahan Ketintang, kecamatan Gayungan, Kota Surabaya, provinsi Jawa Timur.

## 🚀 Layanan API

API ini dirancang untuk memberikan data berjenjang, dalam arti memiliki fasilitas pencarian data dimulai dari provinsi se-Indonesia. Jika kode provinsi telah diketahui, maka terdapat fasilitas yang menyediakan data seluruh kota/kabupaten di dalam provinsi tersebut. Selanjutya, jika kode provinsi dan kota/kabupaten didapatkan, maka dapat diberikan fasilitas data seluruh kecamatan dalam kota/kabupaten tersebut. Demikian seterusnya sehingga sampai ke level desa/kelurahan.

API juga akan menyediakan pencarian berupa regex baik dari kode wilayah maupun dari nama wilayah untuk pencarian yang lebih fleksibel -yang mungkin diperlukan oleh jenis-jenis aplikasi tertentu atau untuk tujuan tertentu.

## Tujuan

- Memudahkan masyarakat menemukan kode wilayah resmi Indonesia.
- Menyediakan layanan yang siap dipakai oleh aplikasi lain.
- Menjaga akurasi kode wilayah dengan pembaruan dari Keputusan Mendagri.

## Struktur Proyek

- `src/api/` : tempat kode sumber API berada.
- `src/tokenize/` : tempat kode sumber pendaftaran API untuk mendapatkan *API key* berupa token yang harus disertakan dalam 
- `README.md` : dokumentasi proyek.

## Pemeliharaan

Pengembang akan terus memperbarui data wilayah ketika ada keputusan baru dari Menteri Dalam Negeri, sehingga aplikasi tetap sinkron dengan kode wilayah NKRI terbaru.

## 🙏 Terima Kasih
Proyek ini pertama kali berjalan sebagai data yang digunakan dalam proyek magang di [PT Radnet Digital Indonesia](https://radnet-digital.id) mencari kemungkinan **Potensi Konflik Kepemilikan Nama Domain Desa.ID** dari [UPN Veteran Jawa Timur](https://upnjatim.ac.id/) (Billy Thierry Maulana A.F., Adhen Chandra Gilang R., Salsabila Farida Firdaus, dan pembimbing Ardhon Rakhmadi, S.Tr.T., M.Kom.).

Saat ini format dan cara penggunaan data diteruskan oleh Mochammad Dicky -mahasiswa [Universitas Narotama](https://narotama.ac.id) untuk diubah menjadi layanan API yang dapat digunakan oleh umum.

## 🤝 Kontribusi
Kami sangat menyambut kontribusi dari komunitas! Silakan buka issue atau kirim pull request untuk perbaikan, penambahan fitur, atau dokumentasi.

## 📜 Lisensi
Proyek ini dilisensikan di bawah lisensi MIT.
