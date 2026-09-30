# #🧶🎫🚀🔰🔰⚡🏷🔖📖🚩❗✔❌ 
# 🔰🔰 Metode String

'''
❗❗ Semua metode string akan mengembalikan nilai baru,
Metode yang digunakan trakan mengubah string asli
'''

# ⚡ capitalize() : 
'''
mengubah karakter pertama menjadi huruf besar
sisanya menjadi huruf kecil
'''
teks = 'BELAJAR PYTHON3'
hasil = teks.capitalize()
print('hasil 1:', hasil)

# ⚡ casefold() :
'''
mirip deng metode lower. tapi de hanya bekerja 
pada karakter bahasa asing
'''
teks1 = 'groß'
teks2 = 'gross'
print('................................')
print('hasil teks1 lower :', teks1.lower())
print('hasil teks1 casefold :', teks1.casefold())

print('hasil teks2 lower :', teks2.lower())
print('hasil teks2 casefold :', teks2.casefold())
print('................................')

# ⚡ center() :
'''
Metode ini digunakan untuk membuat sebuah string berada di
tengah-tengah (center-aligned). Caranya kerjanya, de akan
menambahkan karakter pengisi (secara default adalah spasi)
di sisi kiri dan kanannya.
sintaks : str.center(width, fillchar)
'''
teks = 'Python3'
hasil = teks.center(20)
hasil2 = teks.center(20, '-')
print(hasil)
print(hasil2)

#- jika string lebih panjang dari lebar yang diberi (trakan ada efek)
hasil3 = teks.center(4, '-')
print(hasil3)

#- jika ruang kosong bernilai ganjil, karakter pengisi 
# extra ditaruh di sisi kanan
hasil4 = teks.center(10, '*')
print(hasil4)

# ⚡ count()
'''
metode ini digunkan untuk menghitung berapa kali sebuah substring
atau teks tertentu muncul di dalam sebuah string.
sintak : str.count(substring, start, end)

substring : teks yang akan dicari dan dihitung jumlahnya
start (opsional) : index posisi awal pencarian (secara default 0)
end (opsional) : index posisi akhir perncarian 
                 (default -> sampe akhir string)
'''
teks = '''Sa suka python. kalo ko suka kh trada? 
kam yang lain juga suka kh trada?'''

hasil1 = teks.count('suka')
hasil2 = teks.count('suka', 35)
hasil3 = teks.count('suka', 2, 35)
print('--------------------')
print('hasil 1:', hasil1)
print('hasil 2:', hasil2)
print('hasil 3:', hasil3)
print('--------------------')

# ⚡ encode() :
'''
metode ini digunakan untuk mengubah string biasa (unicode) menjadi
bentuk biner atau susuan bytes menggunakan aturan pengkodean (encoding)
terterntu.
sintaks : str.encode(encoding, errors)

encoding (opsional) : jenis pengokedan (default "utf-8", 
                        -> "ascii", "latin-1", "utf-16" , dll).
errors (opsional) : menentukan cara menangani karakter yang tra
                    didukung oleh jenis pengkodean yang dipilih.
                    defaultnya adalah "strict" yang akan memicu 
                    error UnicodeEncodeError
'''
teks = 'teks'
hasil_bytes = teks.encode()

print('hasil bytes :', hasil_bytes)
print('tipe hasil bytes :', type(hasil_bytes))

teks = 'roket 🚀'
hasil = teks.encode('utf-8')

print('hasil :', hasil)

# 🔖 kebalikan dari encode adalah decode
teks_bytes = b'roket \xf0\x9f\x9a\x80'
hasil = teks_bytes.decode()
print('hasil :', hasil)

#- menggunakan parameter errors
teks = 'roket 🚀'
hasil = teks.encode('ascii', errors='ignore') # hapus karakter yang tra didukung
print('hasil penangan error :', hasil)

hasil = teks.encode('ascii', errors='replace') # ganti karakter yang tra didukung
print('hasil penangan error :', hasil)

hasil = teks.encode('ascii', errors='xmlcharrefreplace') # ganti deng entitas xml/HTML
print('hasil penangan error :', hasil)

# ⚡ endswith()
'''
metode ini digunakan untuk memeriksa apakah sebuah string diakhiri deng kata
atau karakter tertentu. hasilnya selalu berupa boolean (True untuk benar, False untuk salah).
sintaks : str.endswith(suffix, start, end)

suffix : teks atau tuple berisi beberapa teks yang ingin di cek
start(optional) : posisi awal pencarian
end (optional) : posisi akhir pencarian
'''
situs = 'www.kodingcendrawasih.com'
hasil = situs.endswith('.com')
print('hasil :', hasil)

hasil = situs.endswith('www', 0, 4)
print('hasil :', hasil)

nama_file = 'laporan.xlsx'
hasil = nama_file.endswith(('.xlsx', '.xls', '.csv'))
print('hasil :', hasil)

# ⚡ expandtabs() :
'''
mengubah semua karakter tab ('\t') di dalam string menjadi
karakter spasi.
sintaks : str.expandtabs(tabsize = 8) 
'''
teks = '1\t2\t3\t'
hasil = teks.expandtabs()
print(hasil)

teks = 'Nama\tUsia\tBahasa'
hasil = teks.expandtabs(10)
print(hasil)

# ---- penggunaan sederhana
dataHeader = 'NAMA\tUSIA\tBAHASA'
data1 = 'Andreas\t25\tPython'
data2 = 'Andi\t25\tPython'
data3 = 'Andre\t25\tJavaScript'
print(f'''==================================
{dataHeader.expandtabs(10)}
----------------------------------
{data1.expandtabs(10)} 
{data2.expandtabs(10)} 
{data3.expandtabs(10)} 
==================================''')

# ⚡ find()
'''
metode ini digunakan untuk mencari posisi index pertama
dari sebuah subtring
sintak : str.find(substring, start, end).

jika subtring ada, maka python akan kas kembali posisi index,
kalo trda berarti -1
'''
teks = '''Sa suka python. kalo ko suka kh trada? 
kam yang lain juga suka kh trada?'''
hasil = teks.find('suka')
cariSubStr = teks.find('javascript')

print('hasil find :', hasil)
print('hasil pencarian find :', cariSubStr)

# ⚡ format()
'''
metode ini metode klasik untuk menyisipkan variabel atau nilai 
kedalam string. cara moderennya adalah format string yang muncul
di python 3.6 ke atas.
ada 3 cara penggunaan.
'''
#- cara 1 (menggunakan urutan posisi):
# str1 = 'Hai sobat, sa pu nama {}, sa pu zodiak {}, sa berusia {}'.format('KodingCen', 'Virgo', 25)
str1 = 'Hai sobat, sa pu nama {}, sa pu zodiak {}, sa berusia {} tahun'
hasil = str1.format('KodingCen', 'Virgo', 25)
print('cara 1:', hasil)

#- cara 2 (menggunakan index posisi)
str2 = 'Hai sobat, sa pu nama {0}, sa pu zodiak {1}, sa berusia {2} tahun'
hasil = str2.format('KodingCen', 'Virgo', 27)
print('cara 2:', hasil)

#- cara 3 (menggunakan kata kunci)
str3 = 'Hai sobat, sa pu nama {nama}, sa pu zodiak {zodiak}, sa berusia {usia} tahun'
hasil = str3.format(nama='KodingCen', zodiak='Virgo', usia=24)
print('cara 3:', hasil)

# ⚡ format_map()
'''
metode ini digunakan untuk mengsisi nilai placeholder deng
kunci atay key dari sebuah objek pemetaan (dictionary)
'''
myObj = dict({
    "nama": "kodingcen",
    "usia": 24,
    "hobi": "belajar"
})

teks = 'Hai sobat, sa pu nama {nama}, sa pu usia {usia}, sa pu hobi {hobi}'
hasil = teks.format_map(myObj)
print('Hasil :', hasil)

# ⚡ index()
'''
metode ini digunakan untuk mencari posisi pertama suatu kata atau karakter.
sama seperti find tapi de akan kas kembali error kalo tra dapat kata atau 
karakter yang tong cari.
'''
teks = 'Python3'
cek1 = teks.index('Py')
# cek2 = teks.index('py') -> error

print('Cek 1 :', cek1)
# print('Cek 2 :', cek2) -> error (program berhenti)

# ⚡ isalnum()
'''
isalnum atau kepanjangan dari alphanumeric, digunakan untuk memeriksa
apakah semua karakter di dalam sebuah string adalah karakter gabungan dari huruf
dan/atau angka. de akan mengembalikan hasil boolean.
True : jika semuanya adalah huruf(A-z) dan angka (0-9)
False : jika terdapat spasi, tanda baca, simbol, atau string kosong

- metode ini tra pu parameter
'''
teks1 = 'abc123'
teks2 = 'abc 123'
teks3 = '@bc'

print('Hasil 1 :', teks1.isalnum())
print('Hasil 2 :', teks2.isalnum())
print('Hasil 3 :', teks3.isalnum())


# ⚡ isalpha()
'''
metode ini digunakan untuk mengecek apakah string hanya huruf
'''
print('abc'.isalpha()) # True
print('abc1'.isalpha()) # False

# ⚡ isascii()
'''
mengecek apakah string berada dalam jangkauan ASCII(0-127)
'''
print('abc'.isascii()) # True
print('@abc'.isascii()) # True
print('a b c'.isascii()) # True
print('roket 🚀'.isascii()) # False

# ⚡ isdecimal()
'''
mengecek apakah string berupa angka desimal murni (angka 0 - 9 dalam
sistem desimal standar)
'''
print('123'.isdecimal()) # True
print('0000'.isdecimal()) # True
print('12.39'.isdecimal()) # False

# ⚡ isdigit()
'''
memeriksa apakah string berupa merupakan angka / digit
'''
print('001'.isdigit())  # True
print('101'.isdigit()) # True
print('1.10'.isdigit()) # False
print('-12'.isdigit()) # False

# ⚡ isindetifier()
'''
memeriksa apakah string merupakan nama pengenal (indetifier) yang valid
menurut sintaksis python. 
hasil akan true jika mengikuti aturan penamaan variabel, deng catatan:
kata kunci resmi yang seharusnya dilarang seperti "def", "class", "if", dll-
akan mengembalikan true.
untuk mengatasi hal tersebut butuh kombinasi modul "keyword" biar hasilnya False
'''
teks1 = '_namaPrivat'
teks2 = 'namaLengkap'
teks3 = 'nama_depan'
teks4 = 'nama2'

teks5 = 'nama belakang'
teks6 = '1nama'

teks7 = 'class'
teks8 = 'def'
teks9 = 'if'

print(teks1.isidentifier()) # True
print(teks2.isidentifier()) # True
print(teks3.isidentifier()) # True
print(teks4.isidentifier()) # True

print(teks5.isidentifier()) # False
print(teks6.isidentifier()) # False

print(teks7.isidentifier()) # True
print(teks8.isidentifier()) # True
print(teks9.isidentifier()) # True

import keyword 

print(teks7.isidentifier() and not keyword.iskeyword(teks7)) # False
print(teks8.isidentifier() and not keyword.iskeyword(teks8)) # False
print(teks9.isidentifier() and not keyword.iskeyword(teks9)) # False

# ⚡ islower()
'''
mengecek apakah ada karakter huruf kecil didalam string. 
kalo ada 1 karakter huruf kecil saja hasilnya akan true, deng
syarat trada 1 katakter huruf besar. kalo ada de akan error

'''
print('abc'.islower()) # True
print('--*#^@)$*$&a'.islower()) # True
print('1274832048a'.islower()) # True

print('aBC'.islower()) # False
print('123a123A'.islower()) # False
print('1245@#$@'.islower()) # False

# ⚡ isnumeric()
'''
metode ini digunakan untuk mengecek apakah seluruh karakter
di dalam string berupa karakter numeric (angka). dibandingkan
kedua metode lain yang menangani hal yang sama isdigit() dan 
isdecimal(), metode ini jauh lebih luas dan akurat dalam mengenal
berbagai bentuk numerik

isdecimal() akan mengasilkan false jika:
    - angkanya superskrip atau pangkat
    - angka pecahan atau unicode pecahan
    - karakter numerik lain (mandarin, kanji, dll)
    - angkanya decimal atau minus (12.4, -3)
isdigit() akan false jika :
    - angka pecahan atau unicode pecahan
    - karakter numerik lain (mandarin, kanji, dll)
    - angkanya decimal atau minus (12.4, -3)
sedangkan isnumeric() :
    - angkanya decimal atau minus (12.4, -3)
'''

# ⚡ isprintable()
'''
digunakan untuk memeriksa apakah seluruh karakter di dalam string
merupakan karakter yang dapat dicetak.
aturannya :
True : jika semua karakter bisa ditampilkan (angka, huruf, simbol, tanda baca, 
       spasi biasa, dan string kosong)
False : jika terdapat minimal 1 karakter escape unicode (\n, \t, \r, dll)
'''
teks1 = '12a - &8.⚡'
teks2 = 'a\nb'

print(teks1.isprintable()) # True
print(teks2.isprintable()) # False

# ⚡ isspace()
'''
digunakan untuk memeriksa apakah seluruh karakter string merupakan karakter
spasi. karakter spasi antara lain :
- spasi biasa (' ')
- tab ('\t')
- baris baru ('\n')
- tab vertikal ('\v')
- umpan formulir ('\f')

string kosong ("") akan menghasilkan false
'''
print(' '.isspace()) # True
print('\t'.isspace()) # True
print('\n\t'.isspace()) # True

print (' x '.isspace()) # False
print(''.isspace()) # False

# ⚡ istitle()


# ⚡ isupper()
'''
memeriksa apakah semua karakter adalah huruf besar. 
akan true jika hanya ada 1 saja huruf besar didalamnya.
dan false jika ada 1 saja huruf kecil
'''
print('12E5'.isupper()) # True
print('- E$#'.isupper()) # True
print(' A B 2 * () =-=-98'.isupper()) # True

print(' a - B - c '.isupper()) # False
print('abcdE'.isupper()) # False

# ⚡ join()
# ⚡ ljust()
# ⚡ lower()
# ⚡ lstrip()
# ⚡ maketrans()
# ⚡ partition()
# ⚡ replace()
# ⚡ rfind()
# ⚡ rindex()
# ⚡ rjust()
# ⚡ rpatition()
# ⚡ rsplit()
# ⚡ rstrip()
# ⚡ split()
# ⚡ splitlines()
# ⚡ strip()
# ⚡ swapcase()
# ⚡ title()
# ⚡ translate()
# ⚡ upper()
# ⚡ zfill()
