# 🔰🔰 LIST COMPREHENSION
'''
List Comprehension menawarkan sintaks yang lebih 
singkat ketika kitorang ingin membuat daftar baru
dari nilai-nilai daftar yang su ada. bisa dibilang
ini adalah cara singkat menulis pernyataan for
di dalam list. dan hasilnya adalah daftar atau list baru
'''

# 🔖 Tanpa List Comprehension
daftar = [1,2,3,4,5,6,7,8,9,10]
daftarBaru = []

for i in daftar:
    if i % 2 == 0:
        daftarBaru.append(i)

print(daftarBaru)

# 🔖 Deng List Comprehension
daftar = [1,2,3,4,5,6,7,8,9,10]
daftarBaru = [i for i in daftar if i % 2 == 0]

print(daftarBaru)

# 🔖 Sintaksis
'''
newList = [expression for item in iterable if condition == True]

- niali yang dikembalikan adalah daftar baru, tanpa
mengubah daftar lama.
'''

# 🔖 Kondisi (Condition)
'''
kondisi ini seperti filter yang hanya menerima item
yang memenuhi syarat yang ditentukan
'''

daftarBuah = ['apel', 'jeruk', 'semangka', 'mangga']
daftarBuahBaru = [buah for buah in daftarBuah if buah != 'apel']
print(daftarBuah)
print(daftarBuahBaru)

# 🔖 Iterable (Dapat Diulang)
'''
iterable dapat berupa objek apapun yang penting
de dapat diiterasi seperti: list, tuple, set, dll.
'''

daftarBaru = [x for x in range(1, 11)]
print(daftarBaru)

# 🔖 Expression (Ekspresi)
'''
ekspresi merupakan item saat ini dalam iterasi,
item ini bisa kitong manipulasi sebelum akhirnya
menjadi item dalam daftar baru
'''

daftarBaru2 = [angka ** 2 for angka in daftarBaru]
print(daftarBaru2)

daftarBaru3 = [angka if angka != 5 else 50 for angka in daftarBaru]
print(daftarBaru3)
