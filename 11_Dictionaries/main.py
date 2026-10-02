# 🔰🔰 DICTIONARY

'''
dictionary atau kamus digunakan untuk menyimpan kumpulan
pasangan kunci dan nilai atau key dan value.
kamus adalah kumpulan data terurut, dapat diubah, tapi 
tra boleh ada kunci duplikat
'''

# ⚡ Membuat Kamus
# 🔖 kamus literal
kamus1 = {
    'nama': 'KodingCen',
    'usia': 25,
    'sudahMenikah': False,
}

print(kamus1, ' >>> Tipe >>> ' , type(kamus1))

# 🔖 fungsi kontruktor
kamus2 = dict({
    'nama': 'KodingCendrawasih',
    'usia': 26,
    'sudahMenikah': False
})

print(kamus2, ' >>> Tipe >>> ' , type(kamus2))


# ⚡ Mengakses Item Kamus

# 🔖 akses kunci (bukan index)
nama = kamus2['nama']
print(f'Nama {' :'.rjust(12,'.')} {nama}')
print(f'Usia {' :'.rjust(12,'.')} {kamus2['usia']}')

# 🔖 metode get()
print(f'Sudah Menikah {' :'.rjust(3,'.')} {kamus2.get('sudahMenikah')}')

# ⚡ Metode keys() >>> list baru

listKunci = kamus2.keys()
print(listKunci)

# listKunci[0] = 'KODINGCEN' >>> error 

kamus2['bahasa'] = 'Python'
print(listKunci) # kunci otomatis diupdate

# ⚡ Metode values() >>> list baru

listNilai = kamus2.values() 
print(listNilai)

kamus2['nama'] = 'KODING|CEN'
print(listNilai)

# ⚡ Metode items() >>> setiap item jadi tupel 
#                        di dalam list.

daftarItemKamus = kamus2.items()
print(daftarItemKamus)

kamus2['nama'] = 'Koding Cendrawasih' # mengubah nilai nama
kamus2['hobi'] = 'Belajar' # menambah kunci dan nilai baru
print(daftarItemKamus)


# ⚡ Periksa Kunci

print('sudahMenikah' in kamus2) # True

# ⚡ Update Kamus

kamus2.update({'zodiak' : 'Virgo'})
print(kamus2)
print(daftarItemKamus)

# ⚡ Menghapus Item Dan Kamus

# 🔖 metode dict.pop(nilai)

# kamus2.pop() >>> error (harus ada argumen)
kamus2.pop('zodiak')
print(kamus2)

# 🔖 metode dict.popitem()

kamus2.popitem() # hapus item terakhir (kalo di python
#                  versi sebelum 3.7. item dihapus secara acak)

print(kamus2)

# 🔖 metode dict.popitem()

kamus2.clear() # membersikan kamus
print(kamus2)

del kamus2 # menghapus kamus
# print(kamus2) >>> error

# ⚡ Perulangan Kamus

kamus3 = {'nama':'kodingcen', 'bahasa':'Python'}

# 🔖 mengulang semua kunci di dalam kamus 1 per 1
for kunci in kamus3:
    print('kunci :', kunci)

# 🔖 mengulang semua nilai di dalam kamus 1 per 1
for nilai in kamus3:
    print('nilai :', kamus3[nilai])

# 🔖 metode kamus.keys()
print(kamus3.keys())
# 🔖 metode kamus.values()
print(kamus3.values())
# 🔖 metode kamus.items()
print(kamus3.items())

print('------------------')
for item in kamus3.items():
    print(item)
print('------------------')

for kunci, nilai in kamus3.items():
    print(f'{kunci} : {nilai}')

# ⚡ Menyalin Kamus 

kamus4 = {'nama': 'KodingCen', 'bahasa': 'Python'}
kamus5 = kamus4
kamus5.popitem()
kamus5.clear()

print('Kamus 4 :', kamus4) # terubah karena 1 referensi
print('Kamus 5 :', kamus5) 

# 🔖 metode kamus.copy()

kamus6 = {'nama': 'KodingCen', 'bahasa': 'Python'}
kamus7 = kamus6.copy() 
kamus7.popitem() 
kamus7.clear() 

print('Kamus 6 :', kamus6) # tetap 
print('Kamus 7 :', kamus7) 

# 🔖 fungsi konstruktor

kamus8 = {'nama': 'KodingCen', 'bahasa': 'Python'}
kamus9 = dict(kamus8)
kamus9.clear()

print('Kamus 8 :', kamus8) # tetap 
print('Kamus 9 :', kamus9) 

# ⚡ Kamus Bersarang

daftarKoleksiPython = {
    "list": {
        'alias': 'daftar'
    },
    "tuple": {
        "alias": 'tuple'
    },
    "set": {
        "alias": "himpunan"
    },
    "dictionary": {
        "alias": "kamus"
    }
}

print(daftarKoleksiPython)

kamus_1 = {'nama': 'Hery', 'usia': 24}
kamus_2 = {'nama': 'Kelvin', 'usia': 25}
kamus_3 = {'nama': 'Rian', 'usia': 23}
kamus_4 = {'kamus1': kamus_1, 'kamus2': kamus_2, 'kamus3':kamus_3}

print(kamus_4)

# ⚡ Mengakses Item Kamus Bersarang

print(kamus_4['kamus2']['nama'])

print('------------')
for kunci, nilai in kamus_4.items():
    print(kunci)
    for kunci in nilai:
        print(f'{kunci} : {nilai[kunci]}')
print('------------')

