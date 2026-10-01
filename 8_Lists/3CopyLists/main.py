# 🔰🔰 COPY LISTS (MENYALIN DAFTAR)

daftar1 = [1,2,3]
daftar2 = daftar1 # hanya menyalin referensi

daftar2[-1] = 5 # item daftar1 ikut terubah

print(daftar1)
print(daftar2)

# 🔖 Gunakan Metode copy()
daftar1 = [1,2,3]
daftar2 = daftar1.copy()

daftar2[-1] = 5

print('----------')
print('copy()')
print(daftar1)
print(daftar2)
print('----------')

# 🔖 Gunakan Fungsi Konstruktor list()
daftar1 = [1,2,3]
daftar2 = list(daftar1)

daftar2[-1] = 5

print('----------')
print('list()')

print(daftar1)
print(daftar2)
print('----------')

# 🔖 Gunakan slice()

daftar1 = [1,2,3]
daftar2 = daftar1[:]

daftar2[-1] = 5

print('----------')
print('slice[:]')
print(daftar1)
print(daftar2)
print('----------')

