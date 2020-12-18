from geometry.bangun_ruang import BangunRuang
from geometry.persegipanjang import PersegiPanjang
from geometry.segitiga import Segitiga

print('Menggunakan OOP')
p1 = PersegiPanjang(10, 30)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(10, 30)
print(s1.info())
print(s1.hitung_luas())

print('\nMencoba membuat object class dari BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

"""
Polymorphism adalah kemampuan object untuk merespons berbeda 
terhadap pemanggilan method yang sama
"""
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\nPolymorphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())