# 🔰🔰 TUPLES
'''
sama seperti list yang berfungsi untuk menyimpan
kumpulan data dalam 1 variabel. tapi yang membedakannya
de simpan nilai secara berurutan, dan nilainya tra bisa diubah
'''

tuple1 = (1,2,3,1,2)

print(tuple1)

# 🔖 tuple bisa dibuat tanpa tanda kurung
tuple2 = 1,2,3

print(tuple2, end= ' tipe -> ')
print(type(tuple2))

# 🔖 itemnya tra bisa diubah kalo su ditetapkan
tuple3 = (1,2,3)
# tuple3.append(2) -> error

# 🔖 mengecek jumlah item
print('jumlah item tuple :', len(tuple3))

# 🔖 tuple kosong dan tuple deng item cuman 1 biji
tupleKosong = ()
tupleJomblo = (1,) # harus ada titik koma, klo tra kasih
#                      bukan tuple namanya sobat
print(tupleKosong, end= ' -> type ')
print(type(tupleKosong))

tuple4 = (1)

print(tupleJomblo, end= ' -> type ')
print(type(tupleJomblo))
print(tuple4, end= ' -> type ')
print(type(tuple4))

# 🔖 membuat tuple dengan fungsi kontruktor

tuple5 = tuple((1, 2, 3))
print(tuple5)

# ⚡ Mengakses Tuple

# 🔖 akses item deng index
print(tuple5[0])
print(tuple5[-1])

# 🔖 rentang index
tuple1 = (1,2,3,4,5,6,7)

print(tuple1[1:4])
print(tuple1[-4:-1])
print(tuple1[:5])
print(tuple1[3:])

# 🔖 cek item
print(4 in tuple1) # True
print(10 in tuple1) # False

# ⚡ Trik Mengubah Nilai Tuple
'''
karan tong tra bisa mengubah item tuple secara
langsung, jadi kitong boleh pake cara ini. caranya
dengan merubah tuple menjadi list. setelah semuanya seles,
jang lupa kas kembali de ke tipe awal (yaitu tuple)
'''
tuple1 = (1,2,3)
print('Tuple Awal :', tuple1)

daftarSementara = list(tuple1)
daftarSementara.append(4)
daftarSementara.append(5)
daftarSementara.append(6)
daftarSementara.pop(2)
# print(daftarSementara)

tuple1 = tuple(daftarSementara) # ubah kembali ke tuple
print('Tuple Update :', tuple1)

# ⚡ Menambahkan Tuple ke Tuple

tuple1 = (1,2,3)
tuple2 = (4,5)
tuple3 = (6,) # jang lupa tanda koma

tuple1 += tuple2 + tuple3

print(tuple1)

# ⚡ Menghapus Tuple
del tuple1
# print(tuple1) -> error : tupe su dihapus

# ⚡ Membongkar Tuple
daftarSobat = ('Andrea', 'Bernad', 'Chika', 'Denis')
(sobat1, sobat2, sobat3, sobat4) = daftarSobat

print('Sobat 1:', sobat1)
print('Sobat 2:', sobat2)
print('Sobat 3:', sobat3)
print('Sobat 4:', sobat4)

# 🔖 menggunakan asterik (*)
tuple1 = (1,2,3,4,5,6,7)
(satu, dua, tiga, *nums) = tuple1

print(satu) # 1
print(dua) # 2
print(tiga) # 3
print(nums) # [4,5,6,7]
print(nums[0]) # 4
print(nums[-1]) # 7

tuple1 = (1,2,3,4,5,6,7)
(one, *nums, seven) = tuple1

print(one) # 1
# print(two) -> error
print(nums[0]) # 2
print(nums[-1]) # 6
print(seven) # 7

# ⚡ Perulangan Tuple

for i in tuple1:
    print('item :', i)

counter = 0

while counter < len(tuple1):
    print('ITEM :', tuple1[counter])
    counter += 1

# ⚡ Metode Tuple
'''
ada 2 metode bawaan tuple yaitu :
- count()
- index()
'''