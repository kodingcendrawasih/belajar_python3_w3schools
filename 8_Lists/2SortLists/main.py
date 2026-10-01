# 🔰🔰 SORT LIST (MENGURUTKAN DAFTAR)

# 🔖 sort() : mengurutkan menaik

daftarSobat = ['Kevin', 'Leona', 'Intan', 'Andreas', 'Denis', 'Erwin']
daftarSobat.sort()
print(daftarSobat)

# 🔖 sort(resverse = True) : mengutkan menurun
daftarSobat = ['Kevin', 'Leona', 'Intan', 'Andreas', 'Denis', 'Erwin']
daftarSobat.sort(reverse = True)
print(daftarSobat)

# 🔖 mengurutkan daftar numeric/angka
daftarAngka = [3,5,7,8,1,10,2,15]
# daftarAngka.sort()
daftarAngka.sort(reverse = True)
print(daftarAngka)

# 🔖 Sesuaikan deng Fungsi Pengurutkan 
'''
key = function

- fungsi atau function ini akan mengembalikan angka
yang akan digunakan untuk mengurutkan daftar (angka
kecil duluan baru angka besar)
'''

def f1(n):
    return abs(n - 10)

myList = [1, 5, 9, 2, 10, 15, 7, 20, 11, 14]
myList.sort(key = f1)
print(myList)

# 🔖 Pengurutan Case Insensitive
'''
secara bawaah sort() tidak peka terhadap
huruf besar atau huruf kecil, sehingga huruf besar
yang akan didahulukan baru huruf kecil
'''

myList = ['andika', 'Zilvia', 'chika', 'ana']
myList.sort()
print(myList)

# cara mengatasi hal diatas
myList = ['andika', 'Zilvia', 'chika', 'ana']
myList.sort(key = str.lower)
print(myList)

# 🔖 Membalikan Urutan Daftar 
myList = ['andika', 'Zilvia', 'chika', 'ana']
myList.reverse()
print(myList)