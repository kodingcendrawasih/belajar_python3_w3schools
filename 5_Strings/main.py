# 🔰🔰 STRING

'''
string adalah kumpulan karakter huruf. python de tra pu 
tipe data char. string di kelilingi oleh tanda kutip tunggal (' ') atau 
kutip ganda (" ")
'''

# ⚡ Menampilkan Literal String
print('python')
print("python")

# ⚡ Tanda Kutip Dalam Tanda Kutip
'''
kitong dapat menggunkan tanda kutip didalam sebuah string 
asalah de tanda kutip tra sama seperti tanda kutip pembungkus
'''
print('I"m KodingCen')
print("hari jum'at")
# print('jum'at') -> error

# ⚡ String Multibaris (pake 3 tanda kutip)
print('--------------------------------')
multiBaris = '''Ini adalah string,
multi baris.
ini juga bisa
ini juga
ini juga bagian dari string
'''
print(multiBaris)
print('--------------------------------')

# ⚡ String Adalah Array

str1 = 'Python3'

print('karakter pertama dari string str1:', str1[0])
print('karakter terkakhir dari string str1:', str1[-1])

#- Karena string adalah array, kitong bisa menggunakan
#  perulangan 'for'

for kar in str1:
    print('kar :', kar)

# ⚡ Mendapatkan Panjang Sebuah String
#- untuk mendapatkan panjang dari string gunakan funsi len()
print('panjang string dari str1 :', len(str1))

# ⚡ Memeriksa Kata Di Dalam String
# 🔖 kata kunci 'in' untuk memeriksa apakah kata tertentu 
#   ada di dalam string

print('kata "Py" di dalam str1 :', 'Py' in str1)
print('kata "Py" di dalam str1 :', 'py' in str1)

# 🔖 kata kunci 'not dan in' untuk memeriksa apakah kata tertentu 
#   trada di dalam string

print('kata "Py" trda di dalam str1 :', 'Py' not in str1)
print('kata "Py" trda di dalam str1 :', 'py' not in str1)

# ⚡ Memotong String

# 🔖 slice(str[0:2]) : digunakan untuk mengambil potongan dari string
potongan1 = str1[0:2] # mengambil karakter dari index ke 0 hingga 
#                       index sebelum 2
print('Potongan 1:', potongan1)

# 🔖 slice(str[:2]) : memotong string dari awal sampe index sebelum 2
print('Potongan 2:', str1[:2])

# 🔖 slice(str[2:]) : memotong dari index ke 2 sampe akhir
print('Potongan 3:', str1[2:])

# 🔖 index negatif untuk memulai potongan dari akhir string
print('Potongan 4:', str1[-5:-1])

# ⚡ Memodifikasi String

# 🔖 Mengubah huruf menjadi huruf besar
var1 = 'PYTHON3'
print('ubah ke huruf kecil :', var1.lower())

# 🔖 Mengubah huruf menjadi huruf kecil
var2 = 'python3'
print('ubah ke huruf besar :', var2.upper())

# 🔖 Mengubah huruf menjadi huruf kecil
print('ubah ke huruf ')

# 🔖 Mengubah huruf setiap huruf menjadi huruf kapital
var3 = 'belajar bahasa pemrogram python'
print('Mengubah setiap kalimat awal menjadi huruf besar :', var3.title())

# 🔖 Mengubah huruf pertama string menjadi huruf kapital
print('Mengubah kalimat pertama menjadi huruf besar :', var3.capitalize())

# 🔖 Hapus spasi kosong
#- menghapus spasi kosong sebelum dan/atau sesudah teks 
var4 = ' Python3 '
print('menghapus ruang kosong (spasi) :', var4.strip())

# 🔖 Mengganti kata atau karater di dalam string
print('menganti huruf "P" didalam var4 :', var4.replace('P', 'J'))
print('menganti huruf "P" didalam var4 :', var4.replace('Py', 'J'))

# 🔖 Memisahkan string (akan mengembalikan list)
var5 = 'Python, JavaScript, C, C++, C#, Java'
pisahkanVar5 = var5.split(',') # sesuaikan deng pemisah atau delimiter
print(pisahkanVar5)

# ⚡ Penggabungan String

str1 = 'Koding'
str2 ='Cendrawasih'
gabung = str1 + str2

print(gabung)

# kalo mu ada spasi tinggal tambahkan spasi diantara tanda petik
gabung = str1 + ' ' + str2
print(gabung)

# ⚡ Format String
'''
seperti yang kitorang su tau, jika menggabungkan string deng angka
angka akan menghasilkan error. untuk menanganinya kitong bisa pake
tanda koma(,). sekarang kitong pake cara yang sedikit lebih elegan
deng format string. Format string ini diperkenalkan di python 3.6.
sintaks :
f'{placeholder}'

placeholder bisa tong kas masuk variabel atau ekspresi.
hasil yang dikembalikan selalu string
'''

nama = 'Koding Cendrawasih'
usia = 25

# print(nama + usia) -> error
print(f'Nama : {nama} | Usia : {usia}')

harga = 25000
ongkir = 5000
# print('harga : ' + harga + ongkir) -> error
print(f'Harga : {harga + ongkir}')

var6 = f'{23}'
print(type(var6))

