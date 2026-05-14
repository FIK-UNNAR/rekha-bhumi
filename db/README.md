CREATE USER 'kode_wilayah'@'localhost' IDENTIFIED BY 'K6FNYQ42%ry1Ym';
GRANT ALL PRIVILEGES ON kode_wilayah.* TO 'kode_wilayah'@'localhost';
FLUSH PRIVILEGES;

$ mysql -u kode_wilayah -p -D kode_wilayah < kode_wilayah.sql