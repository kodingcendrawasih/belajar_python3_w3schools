# #🧶🎫🚀🔰🔰⚡🏷🔖📖❗🚩✔❌ 

# 🔰🔰 TIPE DATA ( DATA TYPES )
'''
Tipe data adalah konsep yang sangat penting di dalam dunia pemrograman.
variabel dapat menyimpan data dengan tipe yang berbeda. dan tipe yang berbeda
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
str = 'string'
print('Data String :', str)

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

