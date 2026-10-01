# 🔰🔰 Join List (Penggabungan List)

'''
Ada beberapa cara menggabungkan dua buah list atau lebih
'''

# 🔖 menggunkan operator (+) -> paling muda
daftar1 = [1,2,3]
daftar2 = [4,5,6]

daftar3 = daftar1 + daftar2

print(daftar3)

# 🔖 menggunakan metode extend() 

daftar4 = []
daftar4.extend(daftar1)
daftar4.extend(daftar2)

print(daftar4)

# 🔖 menggunakan metode append() 

daftar5 = [10, 20, 30]
daftar6 = [40, 50, 60]

for i in daftar6:
    daftar5.append(i)

print(daftar5)