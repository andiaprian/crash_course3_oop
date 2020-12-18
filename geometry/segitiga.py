from geometry.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):  #diawali huruf kapital
    def __init__(self, a, t): #__init__ konstruktor untuk dipanggil
        #fungsi yangdipanggil pertama kali saat object diciptakan
        self.a = a
        self.t = t

    def info(self):
        return f'Ini adalah object dari Segitiga dengan alas = {self.a} dan tinggi = {self.t}'

    def hitung_luas(self):
        return self.a * self.t / 2