from geometry.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):  #diawali huruf kapital
    def __init__(self, p, l):
        #fungsi yangdipanggil pertama kali saat object diciptakan
        self.p = p
        self.l = l

    def info(self):
        return f'Ini adalah object dari Persegi Panjang dengan panjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l