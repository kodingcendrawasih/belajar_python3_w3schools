# 🔰🔰 TIPE DATA ( DATA TYPES )
'''
Tipe data adalah konsep yang sangat penting di dalam dunia pemrograman.
variabel dapat menyimpan data deng tipe yang berbeda. dan tipe yang berbeda
dapat melakukan hal berbeda pula. 
'''

# Dari w3schools kitong bisa liat tipe data bawaan yang -
# dibagi menjadi beberapa kategori

'''
⚡ Tipe Data Bawaan :
- Text Type (tipe teks) : str
- Numberic Types (tipe numerik) : int, float, complex
- Sequence Types (tipe urutan/daftar) : list, tuple, range
- Mapping Type : dict
- Set Types : set, frozenset
- Boolean Type : bool
- Binary Types : bytes, bytearray, memoryview
- None Type : NoneType
'''

# ⚡ Text Type
#- str
str1 = 'string'
print('Data String :', str1)

# ⚡ Numeric Types
#- int
numInt = 25
print('Data Integer :', numInt)
#- float
numFloat = 2.5
print('Data Float :', numFloat)
#- complex
numComplex = 2 + 3j
print('Data Complex :', numFloat)

# ⚡ Squence Types
# 🔖 List (Daftar)
daftarSobat = ['Andreas', 'Bernika', 'Chia', 'Denia']

print('-----------------------')
print('Daftar Sobat')
print(daftarSobat)
print('-----------------------')

# 🔖 Tupel
daftarNilai = (80,85,88,82,85,85)
print('-----------------------')
print('Daftar Nilai')
print(daftarNilai)
print('-----------------------')

# 🔖 Range
daftarRange = range(10)
print('-----------------------')
print('Daftar Range')
print(daftarRange)
print('-----------------------')

# 🔖 Dict
objek1 = {'nama': 'KodingCen', 'usia': 25, 'sudahMenikah': False}
print(objek1)

# 🔖 Set
kumpulanDataUnik = {1, 2, 3, 2, 4, 5, 3, 2}
print(kumpulanDataUnik)

# 🔖 Frozenset
dataTetap = frozenset({1, 4, 3, 5, 3, 2, 3})
print(dataTetap)

# ⚡ Boolean Type
diaAktif = True
sudahMenikah = False
print('Dia Aktif :', diaAktif)
print('Sudah Menikah :', sudahMenikah)

# ⚡ Binary Types
tipeByte = b'Pyhton'
tipeByteArr = bytearray(5)
tipeMemoryView = memoryview(bytes(5))
print('Tipe Byte :', tipeByte)
print('Tipe ByteArray :', tipeByteArr)
print('TIpe Memory View :', tipeMemoryView)

# ⚡ None Type
noType = None
print('No Type :', noType)


# ⚡ Mendapatkan Tipe Dari Suatu Data

nama = 'KodingCen'
usia = 27
sudahMenikah = False

print('Tipe var nama :', type(nama))
print('Tipe var usia :', type(usia))
print('Tipe var sudah menikah :', type(sudahMenikah))

# ⚡ Menetapkan Tipe Data Spesifik
# untuk menentukan tipe data secara spesifik kitong bisa pake fungsi konstuktor

a = str('Nama')
b = int(20)
c = float(1.2)
d = complex(3j)
e = list(['python', 'javascript', 'c'])
f = tuple(('HTML', 'CSS', 'JS'))
g = range(1, 10)
h = dict({'nama' : 'KodingCen', 'hobi': 'belajar'})
i = set((1, 2, 3,2 ,3))
j = frozenset((1, 2, 4, 2, 3,))
k = bool(0)
l = bytes(3)
m = bytearray(3)
n = memoryview(bytes(3))

print(k)