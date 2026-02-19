class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.status = "Tersedia"

    def tampilkan_info(self):
        print(f"Judul  : {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun  : {self.tahun}")
        print(f"Status : {self.status}")
        print("-" * 30)

    def ubah_status(self, status_baru):
        self.status = status_baru

