# 🔰🔰 SETS
'''
set atau himpunan adalah koleksi yang tra terurut, 
tra pu index, dan itemnya tra bisa diubah kalo su 
ditetapkan. tapi kitong bisa menghapus dan menambahkan item
baru. dan juga itemnya unik, duplikasi tra diizinkan.
'''

himpunan1 = {'Andika', 'Dimas', 'Chika', 'Kevin', 'Dimas'}
print(himpunan1)

himpunan1 = {1, 3, 4, 2, 6, 1, 2, 2} # otomatis terurut kalo angka
print(himpunan1)

'''
🚩 Catatan :
    - True dan 1 dianggap sama (duplikat)
    - False dan 0 dianggap sama (duplikat)
'''

himpunan = {True, 1, False, 0}
print(himpunan)

# ⚡ Menghitung Panjang Set

print(len(himpunan)) # 2

# ⚡ Buat Set Deng Fungsi Konstruktor

himpunan = set({1, 2, 3, 4})
print(himpunan)

# ⚡ Mengakses Item Di Himpunan (Set)
'''
kitorang tra bisa mengangkes item melalui index,
karena hal itu memang tra bisa dilakukan untuk data set
atau himpunan. cara yang bisa kitong lakukan adalah
deng perulangan
'''
himpunan = {'Jesika', 'Nita', 'Nelly', 'Erna'}

for i in himpunan:
    print('item :', i)

# 🔖 mengubah item menggunakan trik sebelumnya
daftarSementara = list(himpunan)
daftarSementara.append('Yerikho')

print(daftarSementara)

himpunan = set(daftarSementara)

print(himpunan)

# 🔖 mengecek item
print('Yerikho' in himpunan) # True
print('Yerikho' not in himpunan) # False

# ⚡ Menambah Item 

himpunan = {'Andi', 'Bernad'}
himpunan.add('Kevin')

print(himpunan)

# 🔖 menambah item dari item himpunan lain

himpunan1 = {'Ronal', 'Renal'}
himpunan2 = {'Rolan', 'Rein'}

# himpunan3 = himpunan1 + himpunan2 -> error
# print(himpunan3) -> error
# himpunan2 += himpunan1  -> error

himpunan1.update(himpunan2)

print(himpunan1)

# 🔖 menambah item dari iterable lainnya

daftarSobat = ['Renata', 'Reni', 'Rena', 'Rido']
himpunan1.update(daftarSobat)

# ⚡ Menghapus Item dan Himpunan

# 🔖 mengguankan remove()

himpunan1 = {1,2,3}
himpunan1.remove(2)
# himpunan1.remove(5) - error
print(himpunan1)

# 🔖 mengguankan discard()

himpunan1 = {1,2,3}
himpunan1.discard(1)
himpunan1.discard(5)

print(himpunan1)

'''
bisa juga menggunakan pop(), tapi
nan de hapus item secara acak, karena
set tidak terurut
'''

himpunan1 = {'Ronal', 'Renal', 'Rey'}
himpunan1.pop()

print(himpunan1)

# ⚡ Mengosongkan Himpunan
himpunan1 = {'Ronal', 'Renal', 'Rey'}
himpunan1.clear()

print(himpunan1)

# ⚡ Menghapus Himpunan
himpunan1 = {'Ronal', 'Renal', 'Rey'}
del himpunan1

# print(himpunan1) - error

# ⚡ Perulangan Pada Himpunan
himpunan1 = {'Ronal', 'Renal', 'Rey'}

for nama in himpunan1:
    print('Nama :', nama)
