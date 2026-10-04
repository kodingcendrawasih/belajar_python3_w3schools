# 🔰🔰 MODULES (MODUL)

# ⚡ Import Modul

import modul1


modul1.sayhai("KodingCen")

print(modul1.sobat1["nama"])
print(modul1.sobat1["umur"])
print(modul1.sobat1["hobi"])

# ⚡ Memberi Nama Alias pada Modul

import rumus_mtk_dasar as rumus

print(rumus.penjumlahan(2, 3))
print(rumus.pengurangan(5, 2))
print(rumus.perkalian(3, 4))
print(rumus.pembagian(10, 2))
print(rumus.pangkat(2, 3))

# ⚡ Modul Bawaan Python

import platform

print(platform.system())

# ⚡ Menggunakan dir() untuk Melihat Semua Fungsi
#    dan Variabel dalam Modul

print(dir(platform))

# ⚡ from Modul Mengimpor Fungsi Tertentu
from modul2 import double

print(double(5))


