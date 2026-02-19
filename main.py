from buku import Buku
from anggota import Anggota
from perpustakaan import Perpustakaan

# Buat objek Buku dulu
buku1 = Buku("Buku 1", "Albert Einstein", 2023)
buku2 = Buku("Buku 2", "Vincent van Gogh", 2022)

# lalu objek anggota
anggota1 = Anggota("Anggota_1", "001")
anggota2 = Anggota("Anggota_2", "002")

# terakhir objek perpustakaan
perpus = Perpustakaan("Perpustakaan Teknik Informatika")

# tambahkan buku ke perpustakaan
perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)

# daftarkan anggota baru
perpus.daftar_anggota_baru(anggota1)
perpus.daftar_anggota_baru(anggota2)


print("Percobaan Peminjaman")
anggota1.pinjam_buku(buku1)


print("Informasi Buku")

buku1.tampilkan_info()
buku2.tampilkan_info()
