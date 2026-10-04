# 🔰🔰 SCOPE (LINGKUP)

# ⚡ Lingkup Lokal

def f1():
    nama = 'kodingCen'
    print(nama)

# print(nama) -> error

name = "koding cendrawasih"

def f2():
    print(name)


# ⚡ Variabel Dengan Nama Sama 
usia = 25

def f3():
    usia = 27
    print('usia lokal :', usia)

print('usia global :', usia)

# ⚡ Keyword Global
def f4():
    global angka
    angka = 2

f4()
print(angka) # error kalo tra panggil fungsi

hobi = 'belajar'

def f5():
    global hobi
    hobi = 'koding'

f5()
print(hobi) # hobi tetap belajar kalo tra panggil fungsi


# ⚡ Keyword NonLokal

def fungsi1():
    n = 'Kodingcen'
    def subFungsi():
        nonlocal n
        n = 'KODINGCEN'

    subFungsi()
    return n

print(fungsi1())

# ⚡ Aturan LEGB

'''
1. Local (Lokal) : Di dalam fungsi saat ini
2. Enclosing (Mengelilingi) : Fungsi-Fungsi yang mengelilingi 
   bagian dalam (dari dalam ke luar)
3 Built-in (Bawaan) : Dalam namesapce bawaan python
'''

n = 'global'

def fungsiLuar():
    n = 'encolsing'

    def fungsiDalam():
        n = 'lokal'
        print('Fungsi Dalam :', n)

    fungsiDalam()
    print('Fungsi Luar :', n)

fungsiLuar()
print('Global :', n)    



