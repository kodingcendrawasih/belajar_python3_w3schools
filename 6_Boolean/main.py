# 🔰🔰 BOOLEAN
'''
Boolean adalah tipe data logika yang hanya
mempunyai 2 kemungkinan nilai. 
True jika benar, False Jika salah.
Nilai logika sering kitong dapatkan
jika melakukan perbandingan 2 buah nilai
'''

a = 2
b = 3

print(f'apakah {a} > {b} : {a > b}')
print(f'apakah {a} < {b} : {a < b}')
print(f'apakah {a} == {b} : {a == b}')

# ⚡ Mengevaluasi Nilai dan Variabel
#- gunakan fungsi bool() untuk evaluasi

print(bool('KodingCen')) # true
print(bool(101)) # True

c = 'Python3'
d = 101
print(bool(c)) # True
print(bool(d)) # True

# ⚡ Truthy Values
'''
- semua string adalah True, kecuali string kosong
- semua angka adalah True, kecuali 0
- semua list, tuple, dan dictionary adalah true, kecuali kosong
'''
print(bool('a')) # True
print(bool(10)) # True
print(bool(-1)) # True
print(bool((1,2,3,4))) # True
print(bool([1,2,3,4])) # True

# ⚡ Falsy Values
'''
- string kosong
- angka 0
- ()
- []
- {}
- None
- objek yang dibuat dengan class deng fungsi __len__ yang
  mengembalikan 0 atau False
'''
print(bool(0)) # False
print(bool("")) # Fasle
print(bool(())) # False
print(bool([])) # False
print(bool({})) # False
print(bool(None)) # False

class myClass():
    def __len__(self):
        return 0

print(bool(myClass())) # False

# ⚡ Fungsi dapat mengembalikan nilai boolean

def f1():
    return True

print(f1()) # True

# ⚡ Menjalankan intruksi berdasarkan kondisi

a = True
if a:
    print('benar')
else:
    print('salah')

# ⚡ Fungsi bawaan yang mengembalikan boolean
'''
ada banyak fungsi bawaan di python yang akan
mengembalikan hasil berupa boolean. contoh
fungsi isistance()
'''

#- mengecek apakah suatu objek merupakan bilangan bulat
n = 12.3
print(isinstance(n, int)) # False

