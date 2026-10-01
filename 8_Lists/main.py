# 🔰🔰 LISTS (DAFTAR)

'''
sama seperti de pu nama, list 
digunakan untuk menyimpan beberapa nilai ke dalam variabel
. nilai yang kitong simpan ini
disebut item. dan setiap item de pu index masing-masing.
dan indexnya selalu diawali dari index 0.
de pu item bebas boleh tipe apa sa, mu item deng nilai sama juga
aman-aman sa
'''

myList = ['item1', 'item2', 'item3']
print(myList)

daftarNilai = [80,81,82,83]
print(daftarNilai)

daftarBoolean = [True, False]
print(daftarBoolean)

# ⚡ Buat List Deng Fungsi Konstruktor
# selain literal, kitong juga bisa buat list deng-
#   fungsi konstruktor.

dataSobat1 = list(['Andika', 23, True])
print(dataSobat1)

# ⚡ Mendapatkan Jumlah Item
print(len(dataSobat1))

# ⚡ Mengkases Item
myList = ['item1', 'item2', 'item3', 'item4', 'item5']

# 🔖 item pertama (0), kedua (1) dan seterusnya
item1 = myList[0]
# itemTraDapaTau = myList[12] # error, index de lewat batas

print('item pertama di daftar :', item1)
# print(itemTraDapaTau) # error

# 🔖 item terakhir
itemTerakhir1 = myList[-1]
itemTerakhir2 = myList[len(myList) - 1] 


print('item terakhir :', itemTerakhir1)
print('item terakhir :', itemTerakhir2)

# ⚡ Rentang Index
'''
kitong bisa menentukan rentang index deng
cara-tentukan rentang awal dan rentang akhir. nan python
de kas kembali daftar baru deng item yang berada di
antar rentang index yang tadi tong berikan. 

contoh:
    myList[1:5] - berarti kitong akan mendapatkan
    item di index1, index2, index3 dan index sebelum 
    index5(berarti index4)
'''

# index  ->  0        1        2        3        4        5
# i.negf -> -6       -5       -4       -3       -2       -1
myList = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']
List2 = myList[1:5]

print(List2)

'''
kalo kas hilang rentang awal berarti, item akan diambil
dari index pertama (index0) sampai rentang akhir yang di
berikan. sebaliknya, kalo kas hilang rentang akhir; item akan
diambil dari rentang awal sampe item terakhir dalam daftar
'''
List3 = myList[:4]
print(List3)

List4 = myList[2:]
print(List4)

# ⚡ Rentang Index Negatif
'''
buat index menjadi negatif kalo mau mengawali rentang
dari akhir daftar
'''
List5 = myList[-4:-1]
print(List5)

# ⚡ Memeriksa Item di Dalam List

daftarSobat = ['Yordan', 'Ester', 'Bernad', 'Frans']
cariSobat = 'Ester'

print(cariSobat in daftarSobat) # True

# ⚡ Ubah Nilai Item
'''
tentukan nomor indexnya lalu ubah deng
nilai pegganti
'''
daftarSobat[1] = 'Enjel'

print(daftarSobat)


daftarSobat = ['Bernad', 'Frans', 'Erika']
daftarSobat[1:2] = ['Ferlin', 'Demas']

print(daftarSobat)

daftarSobat = ['Andika', 'Berto', 'Cinta', 'Denis']
daftarSobat[1:3] = ['Hendrik']

print(daftarSobat)

# ⚡ Menyisipkan Item
'''
kalo mau menyisipkan item tanpa mengganti nilai
yang su ada, kitong boleh pake metode insert()
-> insert(index, nilai)
'''
daftarSobat = ['Bernad', 'Frans', 'Erika']
daftarSobat.insert(2, 'Jesika')
print(daftarSobat)

# ⚡ Menambahkan Item
'''
untuk menambahkan item, kitong bisa juga pake
metode append(). metode ini de akan menambahkan
item baru ke akhir daftar 
'''
daftarSobat = ['Bernad', 'Frans', 'Erika']
daftarSobat.append('Kevin')
print(daftarSobat)

# 🔖 menambahkan item dengan item dari daftar lain
'''
pake metode extend() untuk mencapai hasil tersebut
'''

daftar1 = [1,2,3]
daftar2 = [11,22,33]
daftar1.extend(daftar2)

print(daftar1)
print(daftar2)

'''
selain item dari daftar lain. kitong bisa juga
menambahkan item dari iterable lainnya
'''

daftar3 = [1,2,3]
daftarTuple = (4,5,6)
myObj = dict({0: 1, 1: 2})
daftar3.extend(daftarTuple)
daftar3.extend(myObj)

print(daftar3)

# ⚡ Menghapus Item
# remove(), pop(), del

daftar1 = [1,2,3,4,5]
daftar1.remove(2) # hapus berdasarkan nilai
print(daftar1)

daftar2 = [1,2,3,4,5]
daftar2.pop(2) # hapus berdasarkan index
daftar2.pop() # hapus index terakhir
print(daftar2)

daftar3 = [1,2,3,4,5]
del daftar3[3] # hapus berdasarkan index
print(daftar3)

# ⚡ Menghapus Daftar
del daftar3 # hapus daftar3
# print(daftar3) -> error -> daftar3 tra didefinisikan
#                            karna su terhapus

# ⚡ Membersihkan Daftar
daftar4 = [101,102,103]
daftar4.clear()

print(daftar4) # -> []

# ⚡ Perulangan Pada List (Daftar)

# 🔖 perulangan for
daftar5 = [101,102,103]

for item in daftar5:
    print('item :', item)

# 🔖 perulangan for in range 

for item in range(len(daftar5)):
    print(daftar5[item], end=' | ')

print()

daftarSobat = ['Yordan', 'Ester', 'Bernad', 'Frans']

for sobat in range(len(daftarSobat)):
    print(f'sobat {sobat} -> {daftarSobat[sobat]}')

# 🔖 perulangan while

counter = 0

while counter < len(daftarSobat):
    print(f'sobat {counter} : {daftarSobat[counter]}')
    counter += 1

# 🔖 perulangan menggunakan List Comprehension
[print(sobat) for sobat in daftarSobat]

# ⚡ Membongkar Daftar 
dataSobat = ['KodingCen', 25, False]

[nama, usia, sudahMenikah] = dataSobat
print('Nama Sobat :', nama)
print('Usia :', usia)
print('Sudah Menikah :', sudahMenikah)

