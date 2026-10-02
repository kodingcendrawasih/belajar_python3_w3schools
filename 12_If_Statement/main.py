# 🔰🔰 IF STATEMENTS (PERNYATAAN IF)
'''
if (kondisi terpenuhi):
    pernyataan 1
    pernyataan 2
    pernyataan n
else: # tidak terpenuhi
    pernyataan 1
    pernyataan 2
    pernyataan n
'''

if (True):
    print('jalankan statement ini')


if 1 > 0:
    print('yaps, 1 lebih besar dari 0')

nama = 'KodingCen'

if nama == 'KodingCen':
    print(f'Halo {nama}')

if nama:
    print(f'Hello {nama}')


diaAdmin = True

if diaAdmin:
    print('Hai Admin')

'''
Falsy Values :
    - angka -> 0
    - string kosong -> ""
    - None
    - Koleksi Kosong -> [], {}, (), dict({}) 

selain yang di atas semua masuk Truthy Values
'''
if (1):
    print('satu...')

if (10):
    print('sepuluh...')

if (-1):
    print('mines 1')

if (-0): # >>> 0 -> flasy 
    print('mines 0') # tidak eksekusi

if (" "):
    print('string dengan karakter space...')

if ("teks"):
    print('teks...')

if (['a', 'b']):
    print('daftar atau list...')

# ⚡ if...else

angka1 = 2
angka2 = 3
angka3 = 1

if(angka1 > angka2): # False
    print(f'{angka1} lebih besar dari {angka2}') 
else:
    print(f'{angka1} lebih kecil dari {angka2}') # >>> eksekusi

if(angka1 > angka3): # True
    print(f'{angka1} lebih besar dari {angka3}') # >>> eksekusi
else:
    print(f'{angka1} lebih kecil dari {angka3}')

# ⚡ pernyataan elif 

nilai = 80

if nilai == 100:
    print('predikat: A++')
elif nilai >= 90:
    print('predikat: A')
elif nilai >= 80:
    print('predikat: B')
elif nilai >= 70:
    print('predikat: C')
elif nilai >= 60:
    print('predikat: D')
else:
    print('predikat: E')

# ⚡ short hand

nama = 'kodingcen'

print ('hai sobat') if nama == 'kodingcen' else print('maaf, kamu sypa ya?')

angka = 1

if angka == 1: print(angka) 

diaSobat = True if nama == 'kodingcen' else False
print('dia sobat :', diaSobat) 

n = 32
o = 86
nilaiTerbesar = n if n > o else o
print('nilai terbesar :', nilaiTerbesar)

'''
gunakan sort hand untuk menangani kasus sederhana.
kalo de pu kasus kompleks, gunakan if..else, atau elif lebih good
'''

# ⚡ Operator Logika Untuk Menangani Kondisi

nama = 'KODINGCEN'

if nama == 'KodingCen' or nama == 'kodingcen':
    print(f'Hai {nama}, poster?...')

if (nama == 'kodingcen' or 'KodingCen') or (nama == 'KODINGCEN' or 'KODING_CEN'):
    print('sobat, poster....')

nama = 'kodingcen'
usia = 17
suratIjin = True
diaMahasiswa = True

if usia > 17 and (suratIjin or diaMahasiswa):
    print('Boleh Masuk')
else:
    print('Kamu Dilarang Masuk')

# ⚡ If Bersarang

pesan = ""

if usia > 17:
    if suratIjin:
        if diaMahasiswa: pesan = 'Diizinkan'
else:
    pesan = 'Ditolak'

print('pesan :', pesan)

# ⚡ pass (dieksekusi tapi tra ditampilkan)

usia = 17

if usia == 17:
    pass

# if usia > 15:
#     # pass -> error (if butuh pernyatan atau statement)


