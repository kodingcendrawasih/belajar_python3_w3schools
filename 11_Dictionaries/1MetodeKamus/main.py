# 🔰🔰 METODE KAMUS

# ⚡ Metode clear()

kamus1 = dict({'nama':'kodingcen', 'usia':25})
kamus1.clear()
print('Kamus 1:', kamus1)

# ⚡ Metode copy()

kamus1 = dict({'nama':'kodingcen', 'usia':25})
kamus2 = kamus1.copy()
print('Kamus 2:', kamus2)

# ⚡ Metode fromkeys()

kunci = ['nama', 'usia']
nilaiAwal = 0
kamus3 = dict.fromkeys(kunci, nilaiAwal)
print('Kamus 3:', kamus3)

# ⚡ Metode get()

kamus4 = dict({'nama':'kodingcen', 'usia':25})

print('Kamus 4 [\'nama\'] >>>', kamus4['nama'])
# print('Kamus 4 [\'name\'] >>>', kamus4['name'])  >>> error
print('Kamus 4 get(nama) >>>', kamus4.get('nama'))
print('Kamus 4 get(name) >>>', kamus4.get('name')) # >>> None (tra eror)

# ⚡ Metode keys(), values(), items()

kamus5 = dict({'nama':'kodingcen', 'usia':25})
print(kamus5.keys())
print(kamus5.values())
print(kamus5.items())

itemKamus5 = kamus5.items()

for n,o in itemKamus5:
    print(f'{n} : {o}')

# ⚡ Metode pop() dan popitem()

kamus6 = dict({'nama':'kodingcen', 'usia':25, 'hobi':'belajar'})
# kamus6.pop() >>> error
kamus6.pop('usia')
print('kamus 6 :', kamus6)

kamus7 = dict({'nama':'kodingcen', 'usia':25, 'hobi':'belajar'})
kamus7.popitem()
print('kamus 7 :', kamus7)

# ⚡ Metode setdefault()
kamus8 = dict({'nama':'kodingcen', 'usia':25})
kamus8.setdefault('nama','kodcen')
kamus8.setdefault('zodiak','virgo')
print('kamus 8 :', kamus8)

