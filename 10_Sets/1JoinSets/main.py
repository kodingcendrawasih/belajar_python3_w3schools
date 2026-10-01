# 🔰🔰 JOINT SETS (MENGGABUNGKAN HIMPUNAN)

# ⚡ Metode union()

set1 = {1,2,3}
set2 = {4,5,6}
set3 = set1.union(set2)

print('set3 :', set3)

# ⚡ Operator (|)
set4 = set1 | set2

print('set4 :', set4)

# 🔖 menggabungkan beberapa set
set1 = {1,2,3}
set2 = {4,5,6}
set3 = {7,8,9}
set4 = {10,11,12}
set5 = set1.union(set2, set3, set4)
set6 = set1 | set2 | set3 | set4

print('set5 :', set5)
print('set6 :', set6)

'''
kitong juga bisa menggabungkan dengan tipe data
lain seperti tuple dan list, tapi deng catatan
operator (|) tra bisa digunakan
'''
set1 = {1,2,3}
list1 = [4,5,6]
set2 = set1.union(list1)
# set3 = set1 | list1 -> error

print('set2 :', set2)

# ⚡ Metode intersection()
'''
metode ini hanya mengambil nilai duplikat,
jika kita mencoba menggabungan dua buah himpunan
yang memiliki nilai yang sama
'''
set1 = {1,2,3}
set2 = {3,4,5}
set3 = set1.union(set2) # {1, 2, 3, 4, 5}
set4 = set1.intersection(set2)

print('set 4:', set4) # {3}

# 🔖 hasil yang sama deng operator (&)
set5 = set1 & set2

print('set 5:', set5)

# ⚡ Metode difference()
'''
akan mengembalikan himpunan baru yang berisikan
item dari himpunan pertama yang trada di himpunan 
lainnya
'''
set1 = {1, 2, 3, 4}
set2 = {2, 4, 6, 8}
set3 = set1.difference(set2) # {1, 3}

print('set3 :', set3)

# 🔖 hasil yang sama deng operator (-)
set4 = set1 - set2
print('set4 :', set4)

# ⚡ Metode difference()
'''
untuk menyimpan item dari himpunan pertama yang trda
di dalam himpunan lainnya. sekalian mengupdate 
himpunan pertama
'''
set1 = {1, 2, 3, 4}
set2 = {2, 4, 6, 8}
set1.difference_update(set2)
print('SET1 :', set1)

# ⚡ Metode symmetric_difference()
'''
akan menyimpan item-item yang trada di 
kedua himpunan
'''
set1 = {1, 2, 3, 4}
set2 = {5, 6, 2, 1}
set3 = set1.symmetric_difference(set2)
print('set3 :', set3)

# 🔖 hasil yang sama deng operator (^)
set4 = set1 ^ set2
print('set4 :', set4)

# ⚡ Metode symmetric_difference_update()
'''
akan menyimpan semua item, kecuali duplikat 
dan merubah himpunan asli
'''
set1 = {1, 2, 3, 4}
set2 = {5, 6, 2, 1}
set1.symmetric_difference_update(set2)

print('SET2 :', set2)