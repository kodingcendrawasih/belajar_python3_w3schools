#🧶🎫🚀🔰🔰⚡🏷🔖📖❗🚩✔❌ 
# 🔰🔰 VARIABEL
'''
variabel adalah tempat atau wadah bernama yang berguna untuk 
menyimpan data di memori komputer.
'''


# ⚡ Membuat Variabel
'''
Dipython kitong tra kenal yang namanya deklarasi variabel.
variabel nhi de ada saat tong memberikan nilai kedalam variabel
'''
#- membuat variabel nama 
nama = 'Koding Cendrawasih'

# ⚡ Menampilkan Variabel
print(nama)

# 🚩 Aturan Penamaan Variabel
# - nama variabel harus diawali deng huruf atau karakter garis bawah.
# - nama variabel tra boleh diawali deng angka
# - nama variabel hanya boleh berisi karakter alfanum (A-z, 0-9) dan garis bawah (_)
# - nama variabel case sensitive (artinya huruf besar deng huruf kecil berbeda)
# - nama variabel tra boleh pake kata kunci python

# ✔ Penamaan yang benar
nama = "KodingCen"
nama_depan = "Koding"
namaBelakang = "Cendrawasih"
nama1 = "kodingcen"
_namaPrivat = 'ozo'
NAMALENGKAP = 'KODING CENDRAWASIH'

# ❌ Penamaan yang salah
# 2nama = 'error'
# nama-depan = 'error'
# nama panggilan = 'error'
# $nama belakang = 'error'

# 🔖 Nama Variabel Case Sensitive
usia = 25
Usia = 26
USIA = 27

#// ketiga variabel diatas berbeda
print('usia :', usia)
print('Usia :', Usia)
print('USIA :', USIA)

# ⚡ Menimpa nilai variabel
name = 'KodingCen'
print('Nama sebelum dapa timpa :', name)

name = 'Koding Cendrawasih'
print('Nama sesudah ditimpa :', name)

# ⚡ Menetapkan nilai ke beberpa variabel
n, o, i = 'str1', 'str2', 'str3'
print('n :', n)
print('o :', o)
print('i :', i)

#- jumlah variabel harus sama deng nilai, kalo trda python de kas kembali error
# a, b = 'a', 'c', 'd' -> error

# ⚡ Menetapkan satu nilai untuk beberapa variabel
n = o = i = 'KodingCen'
print('n :', n)
print('o :', o)
print('i :', i)

# ⚡ Output Variabel
'''
seperti yang sudah kitong lakukan diatas, untuk menampilakn sebuah
niali dari variabel kitong bisa pake fungsi print(). fungsi ini juga
bisa kitong pake untuk menampilkan hasil dari sebuah ekpresi
'''

#- menampilkan beberpa variabel deng tanda koma (,)
print(n, o, i)

#- atau bisa juga deng operator plus (+)
print(n + o + i)

#- deng operator plus string akan digabungkan tapi tanpa menggunakan spasi
#- kalau mau ya tinggal tambah spasi kosong di dalam fungsi print
print(n + ' ' + o + ' ' + ' ' + i)

'''
operator (+) juga tra bisa berfungsi kalo tong menggabungkan atau menambahkan 
string dengan angka, python akan kas kembali error. kalo tra mu error ya
tinggal pake tanda koma (,)
'''
str = 'string'
num = 12

# print(str + num) -> error
print(str, num)

# ⚡ Variabel Global dan Variabel Lokal

'''
variabel global adalah variabel yang kitorang buat di luar fungsi. sedangkan
variabel lokal adalah variabel yang kitorang buat di dalam fungsi.
de pu perbedaan :
    - variabel global dapat dipakai dimana saja (contohnya variabel-variabel diatas)
    - variabel lokal trada (hanya didalam lingkungan fungsi tempat dia ditetapkan)
jika kitong memaksa untuk memanggil variabel lokal diluar scope atau lingkungannya,
python akan mengembalikan error. supaya tra error kitong butuh kata kunci "global"
'''

#- variabel global 
varGlobal = 'variabel global'

#- variabel lokal
def f1():
    varLokal = 'variabel lokal'
    print('----------------')
    print('var lokal :', varLokal)
    print('var global :', varGlobal)
    print('----------------')


print('var global :', varGlobal)
f1()
# print('var lokal :', varLokal) -> error

# jika kitorang buat nama variabel lokal deng variabel global sama, nilainya
# trakan terpengaruh. niali global tetap, lokal juga tetap

namaSobat = 'Python'

def NamaSobat():
    namaSobat = 'Python3'
    print('nama sobat lokal :', namaSobat)

print('nama sobat global :', namaSobat)
NamaSobat()

#- kata kunci "global"

# "global" untuk membuat variabel global di dalam fungsi
def f2():
    global sobatCode
    sobatCode = 'Helena'

f2()
print('Sobat Code :', sobatCode) # akan error jika tong tra jalankan fungsi f2()

# "global" untuk mengubah variabel global di dalam fungsi
myCrush = 'python'

def f3():
    global myCrush
    myCrush = 'python3'


f3()
print('my crush :', myCrush) # nilainya tetap kalo tong tra panggil fungsi f3()