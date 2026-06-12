# Cara Instalasi Data

**Rekha Bhumi Nusantara** menggunakan *Data Base Management System* (DBMS) MySQL atau MariaDB. Pada README.md ini dijelaskan instalasi data dengan menggunakan perintah *Command Line Interface* (CLI) *mysql client*.

1. Instal DBMS MySQL atau MariaDB sesuai dengan versi sistem operasi yang digunakan.
2. Masuk menggunakan CLI dengan akun *root* atau yang setara: `mysql -u root -p` atau `sudo mysql`.
3. Buat database dengan nama yang diinginkan: `CREATE DATABASE 'rekhabhumi';`
4. Buat user untuk keperluan aplikasi ini: `CREATE USER 'rekha_bhumi'@'localhost' IDENTIFIED BY 'p@ssw0rd';`
5. Beri hak semua *privileges* pada database tadi: `GRANT ALL PRIVILEGES ON rekhabhumi.* TO 'rekha_bhumi'@'localhost';`
6. Perbarui hak akses yang telah diberikan: `FLUSH PRIVILEGES;`

Setelah database dan user dibuat serta hak akses diberikan, maka sudah dapat memindah data yang ada ke dalam DBMS tersebut: `$ mysql -u rekha_bhumi -p -D rekhabhumi < kode_wilayah.sql`