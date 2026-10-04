# 🔰🔰 LAMBDA FUNCTION (FUNGSI LAMBDA)

# Lamda >>> anonymous function (fungsi anonimus)
# sintaks >>> lambda arguments : expression

n = lambda o : o + 10
print(n(5)) # 15

o = lambda o, i : o * i
print(o(2, 3)) # 6

i = lambda n, o, i : (n + o) * 2
print(i(2, 3, 2)) # 10

def fungsi1(n):
    return lambda a : a * n

doubler = fungsi1(2)
tripler = fungsi1(3)

print(doubler(2))
print(tripler(2))

# ⚡ Lambda Dengan Fungsi Bawaan

# 🔖 Lamda deng map()

numbers = [1,2,3,4,5]
doubledA = tuple(map(lambda a : a * 2, numbers))
doubledB = set(map(lambda a : a * 2, numbers))
doubledC = list(map(lambda a : a * 2, numbers))
doubledD = frozenset(map(lambda a : a * 2, numbers))

print(doubledA)
print(doubledB)
print(doubledC)
print(doubledD)

# 🔖 Lamda deng filter()

daftarAngka = [1,2,3,4,5,6,7,8,9,10]
daftarAngkaGanjil = list(filter(lambda item : item % 2 != 0, daftarAngka))

print(daftarAngkaGanjil)

# 🔖 Lamda deng sorted()
daftarKontak = [('Jesika', '081323454321'), ('Bernad', '082356748986'), ('Delia', '082123465984')]
urutkanDaftarKontak = sorted(daftarKontak, key = lambda item : item[0])
print(urutkanDaftarKontak)

daftarNama = ['Ana', 'Anata', 'EL', 'Adi', 'Anastasya']
urutkanNama = sorted(daftarNama, key= lambda item: len(item))
print(urutkanNama)

